#!/usr/bin/env python3
"""
gen_config_h.py — Generate config.h for Windows MSVC build from bareos config.h.in
Usage: python gen_config_h.py <config.h.in> <output/config.h>
"""
import sys
import os
import re

src = sys.argv[1]
dst = sys.argv[2]

os.makedirs(os.path.dirname(dst), exist_ok=True)

# Values to define for a Windows x64 MSVC build
# Everything not listed here will be #undef'd
DEFINES = {
    "BAREOS": '"bareos"',
    "FD_DEFAULT_PORT": '"9102"',
    "SD_DEFAULT_PORT": '"9103"',
    "DIR_DEFAULT_PORT": '"9101"',
    "HAVE_WIN32": "1",
    "HAVE_MSVC": "1",
    "HAVE_SOURCE_LOCATION": "1",
    "BAREOS_VERSION": '"25.0.4"',
    "kVersionString": '"25.0.4"',
    "kBareosVersionStrings": '"25.0.4"',
}

lines = open(src).readlines()
out = []

for line in lines:
    # #cmakedefine01 VAR  →  #define VAR 1 or 0
    m = re.match(r'#cmakedefine01\s+(\w+)', line)
    if m:
        var = m.group(1)
        val = "1" if var in DEFINES else "0"
        out.append(f"#define {var} {val}\n")
        continue

    # #cmakedefine VAR VALUE  →  #define VAR VALUE or /* #undef VAR */
    m = re.match(r'#cmakedefine\s+(\w+)(.*)', line)
    if m:
        var = m.group(1)
        rest = m.group(2).strip()
        if var in DEFINES:
            val = DEFINES[var]
            out.append(f"#define {var} {val}\n")
        else:
            out.append(f"/* #undef {var} */\n")
        continue

    # @VAR@ substitutions
    def replace_at(m2):
        key = m2.group(1)
        return DEFINES.get(key, "")

    line = re.sub(r'@(\w+)@', replace_at, line)
    out.append(line)

with open(dst, 'w') as f:
    f.writelines(out)

print(f"Generated {dst} ({len(out)} lines)")
