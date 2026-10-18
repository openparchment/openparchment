#!/usr/bin/env python3
"""Validate Open Parchment example records against their schema version.

Usage: python3 tools/validate.py [version ...]   (default: all versions)
Requires: pip install jsonschema referencing
"""
import glob, json, os, sys
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TYPE_TO_SCHEMA = {"Producer": "producer", "Harvest": "harvest", "Lot": "lot", "Roast": "roast",
                  "Tasting": "tasting", "IdentityLink": "identity-link"}

def validate_version(v):
    sdir = os.path.join(ROOT, "schema", v)
    registry, schemas = Registry(), {}
    for f in sorted(glob.glob(os.path.join(sdir, "*.schema.json"))):
        s = json.load(open(f, encoding="utf-8"))
        Draft202012Validator.check_schema(s)
        registry = registry.with_resource(s["$id"], Resource.from_contents(s))
        schemas[os.path.basename(f).replace(".schema.json", "")] = s
    failures = 0
    for f in sorted(glob.glob(os.path.join(ROOT, "examples", v, "*.json"))):
        rec = json.load(open(f, encoding="utf-8"))
        name = TYPE_TO_SCHEMA.get(rec.get("type"))
        if name not in schemas:
            print(f"  ? {os.path.basename(f)}: no schema for type {rec.get('type')!r}"); failures += 1; continue
        errs = list(Draft202012Validator(schemas[name], registry=registry, format_checker=FormatChecker()).iter_errors(rec))
        for e in errs:
            print(f"  x {os.path.basename(f)} {'/'.join(map(str, e.path))}: {e.message}")
        if not errs:
            print(f"  ok {os.path.basename(f)} ({name})")
        failures += len(errs)
    return failures

if __name__ == "__main__":
    versions = sys.argv[1:] or sorted(os.path.basename(d) for d in glob.glob(os.path.join(ROOT, "schema", "v*")))
    total = 0
    for v in versions:
        print(v); total += validate_version(v)
    for f in glob.glob(os.path.join(ROOT, "vocabulary", "*.json")):
        json.load(open(f, encoding="utf-8"))
    print("all valid" if total == 0 else f"{total} problem(s)")
    sys.exit(1 if total else 0)
