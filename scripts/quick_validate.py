#!/usr/bin/env python3
"""Quick validation script for Claude skills.

Usage:
    python quick_validate.py <skill_dir>

Checks a skill directory for structural correctness:
  - SKILL.md exists with valid YAML frontmatter (name, description)
  - No unresolved git conflict markers (<<<<<<<, =======, >>>>>>>)
  - Required sections present in SKILL.md
  - Referenced files (references/, assets/) exist
  - No empty files
"""

import os
import re
import sys


def log_ok(msg: str) -> None:
    print(f"  [OK]   {msg}")


def log_warn(msg: str) -> None:
    print(f"  [WARN] {msg}")


def log_fail(msg: str) -> None:
    print(f"  [FAIL] {msg}")


def check_conflict_markers(path: str) -> list:
    """Return a list of conflict-marker lines found in a file."""
    markers = []
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if re.match(r"^(<<<<<<<|=======|>>>>>>>)", line.strip()):
                markers.append((i, line.strip()))
    return markers


def parse_frontmatter(path: str):
    """Return (frontmatter_dict, error) for a SKILL.md file."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        return None, "File does not start with '---' frontmatter delimiter"

    # Split on the closing '---'
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, "Frontmatter block is not closed with a second '---'"

    fm_text = parts[1]
    fm = {}
    for line in fm_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip()
    return fm, None


def validate_skill(skill_dir: str) -> int:
    """Validate a skill directory. Returns number of failures."""
    failures = 0
    skill_dir = os.path.abspath(skill_dir)
    print(f"\nValidating skill: {skill_dir}\n")

    if not os.path.isdir(skill_dir):
        log_fail(f"Skill directory does not exist: {skill_dir}")
        return 1

    # --- 1. SKILL.md exists + frontmatter ---
    skill_md = os.path.join(skill_dir, "SKILL.md")
    if not os.path.isfile(skill_md):
        log_fail("SKILL.md is missing")
        failures += 1
    else:
        log_ok("SKILL.md exists")
        fm, err = parse_frontmatter(skill_md)
        if err:
            log_fail(f"Frontmatter error: {err}")
            failures += 1
        else:
            log_ok("Frontmatter block is well-formed")
            for required in ("name", "description"):
                if required in fm and fm[required]:
                    log_ok(f"Frontmatter has '{required}'")
                else:
                    log_fail(f"Frontmatter missing or empty '{required}'")
                    failures += 1

        # --- 2. Conflict markers in SKILL.md ---
        markers = check_conflict_markers(skill_md)
        if markers:
            log_fail(f"Conflict markers found in SKILL.md: {markers}")
            failures += 1
        else:
            log_ok("No conflict markers in SKILL.md")

        # --- 3. Required step sections ---
        with open(skill_md, "r", encoding="utf-8") as f:
            content = f.read()
        steps = re.findall(r"^## Step (\d+):", content, re.MULTILINE)
        expected = [str(n) for n in range(1, 9)]
        missing = [s for s in expected if s not in steps]
        if missing:
            log_fail(f"SKILL.md missing Step sections: {missing}")
            failures += 1
        else:
            log_ok("SKILL.md contains Steps 1-8")

    # --- 4. References directory ---
    refs_dir = os.path.join(skill_dir, "references")
    if os.path.isdir(refs_dir):
        log_ok("references/ directory exists")
        for fname in os.listdir(refs_dir):
            fpath = os.path.join(refs_dir, fname)
            if os.path.isfile(fpath):
                if os.path.getsize(fpath) == 0:
                    log_fail(f"references/{fname} is empty")
                    failures += 1
                else:
                    log_ok(f"references/{fname} is non-empty")
                markers = check_conflict_markers(fpath)
                if markers:
                    log_fail(f"Conflict markers in references/{fname}: {markers}")
                    failures += 1
                else:
                    log_ok(f"No conflict markers in references/{fname}")
    else:
        log_warn("references/ directory missing (optional)")

    # --- 5. Assets directory ---
    assets_dir = os.path.join(skill_dir, "assets")
    if os.path.isdir(assets_dir):
        log_ok("assets/ directory exists")
        for fname in os.listdir(assets_dir):
            fpath = os.path.join(assets_dir, fname)
            if os.path.isfile(fpath) and os.path.getsize(fpath) == 0:
                log_fail(f"assets/{fname} is empty")
                failures += 1
    else:
        log_warn("assets/ directory missing (optional)")

    # --- 6. Tests directory ---
    tests_dir = os.path.join(skill_dir, "tests")
    if os.path.isdir(tests_dir):
        log_ok("tests/ directory exists")
    else:
        log_warn("tests/ directory missing (optional)")

    return failures


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python quick_validate.py <skill_dir>")
        return 2

    skill_dir = sys.argv[1]
    failures = validate_skill(skill_dir)

    print("\n" + "=" * 50)
    if failures == 0:
        print("RESULT: PASS — skill structure is valid")
        return 0
    else:
        print(f"RESULT: FAIL — {failures} issue(s) found")
        return 1


if __name__ == "__main__":
    sys.exit(main())