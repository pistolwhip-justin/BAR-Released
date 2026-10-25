#!/usr/bin/env python3
"""Apply Bar Released display-name and version metadata to the pinned upstream source."""
from pathlib import Path
import re

ROOT = Path("upstream/BAR")
STRING_FILES = [
    "app/src/main/res/values/strings.xml",
    "app/src/main/res/values-es/strings.xml",
    "app/src/main/res/values-fr/strings.xml",
    "app/src/main/res/values-iw/strings.xml",
    "app/src/main/res/values-pl/strings.xml",
    "app/src/main/res/values-ru/strings.xml",
    "app/src/main/res/values-sk/strings.xml",
    "app/src/main/res/values-tr/strings.xml",
    "app/src/main/res/values-zh-rCN/strings.xml",
]


def replace_once(source: str, old: str, new: str, label: str) -> str:
    count = source.count(old)
    if count != 1:
        raise SystemExit(
            f"Branding patch safety check failed for {label}: expected one match, found {count}"
        )
    return source.replace(old, new, 1)


for relative_path in STRING_FILES:
    path = ROOT / relative_path
    source = path.read_text(encoding="utf-8")
    source = replace_once(
        source,
        '<string name="app_name">BAR</string>',
        '<string name="app_name">Bar Released</string>',
        f"{relative_path}: app_name",
    )

    # Use the product name consistently even where upstream translated the generic app name.
    source, count = re.subn(
        r'<string name="app_name_full">.*?</string>',
        '<string name="app_name_full">Bar Released</string>',
        source,
        count=1,
    )
    if count != 1:
        raise SystemExit(
            f"Branding patch safety check failed for {relative_path}: "
            f"expected one app_name_full element, found {count}"
        )

    # Replace user-facing references to the app name. Keep the project-origin
    # statement's upstream BAR reference intact so source attribution remains accurate.
    lines = []
    for line in source.splitlines(keepends=True):
        if 'name="pref_project_origin_desc"' not in line:
            line = line.replace("BAR", "Bar Released")
        lines.append(line)
    path.write_text("".join(lines), encoding="utf-8")

gradle_path = ROOT / "app/build.gradle.kts"
gradle = gradle_path.read_text(encoding="utf-8")
gradle = replace_once(
    gradle,
    "        versionCode = 1\n",
    "        versionCode = 3\n",
    "app/build.gradle.kts: versionCode",
)
gradle = replace_once(
    gradle,
    "        versionName = versionCode.toString()\n",
    '        versionName = "1.0.2"\n',
    "app/build.gradle.kts: versionName",
)
gradle_path.write_text(gradle, encoding="utf-8")

print("Applied Bar Released branding to all supported app-name resources and set version 1.0.2 (versionCode 3).")
