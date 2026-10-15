#!/usr/bin/env python3
"""Weekly monitor: verify every repo linked in README is alive and active.

- Parses all github.com links from README.md
- Checks each repo via GitHub REST API (stars, pushed_at, archived)
- Refreshes the 'updated' badge date in README
- Files a consolidated GitHub issue listing stale/broken entries (dedup by title)

Env: GITHUB_TOKEN (optional, avoids rate limits), MONITOR_TODAY (YYYY-MM-DD, defaults to today), GITHUB_REPOSITORY (CI).
"""

import json
import os
import re
import sys
import urllib.request
from datetime import date

README = os.path.join(os.path.dirname(__file__), "..", "README.md")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
TODAY = os.environ.get("MONITOR_TODAY") or date.today().isoformat()
HEADERS = {"Accept": "application/vnd.github+json"}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"

STALE_DAYS = 180  # no push for 6 months = stale


def api(url: str, method: str = "GET", payload: dict | None = None):
    data = json.dumps(payload).encode() if payload else None
    req = urllib.request.Request(url, headers=HEADERS, data=data, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except Exception as e:  # noqa: BLE001
        print(f"WARN: {url} -> {e}", file=sys.stderr)
        return None


def main() -> int:
    readme_path = os.path.abspath(README)
    with open(readme_path, encoding="utf-8") as f:
        text = f.read()

    repos = sorted(
        set(
            re.findall(
                r"github\.com/([\w.-]+/[\w.-]+?)(?=[/)\s#\"'`])", text
            )
        )
    )
    print(f"found {len(repos)} repo links")

    stale, broken = [], []
    for slug in repos:
        data = api(f"https://api.github.com/repos/{slug}")
        if not data or "pushed_at" not in data:
            broken.append(slug)
            continue
        pushed = data["pushed_at"][:10]
        archived = data.get("archived", False)
        print(f"  {slug}: stars={data['stargazers_count']} pushed={pushed} archived={archived}")
        if archived:
            stale.append(f"{slug} (archived)")
        else:
            days = (date.fromisoformat(TODAY) - date.fromisoformat(pushed)).days
            if days > STALE_DAYS:
                stale.append(f"{slug} (last push {pushed}, {days}d ago)")

    text = re.sub(
        r"updated-\d{4}--\d{2}--\d{2}", f"updated-{TODAY.replace('-', '--')}", text
    )
    text = re.sub(
        r"alt=\"Updated \d{4}-\d{2}-\d{2}\"", f'alt="Updated {TODAY}"', text
    )
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(text)

    title = "Weekly monitor: stale or broken entries"
    if (stale or broken) and TOKEN:
        body_lines = ["以下条目需要人工复核(自动巡检,每周一运行):", ""]
        if stale:
            body_lines.append("**停滞/归档**")
            body_lines += [f"- {s}" for s in stale]
        if broken:
            body_lines.append("**API 查询失败(可能已删除或改名)**")
            body_lines += [f"- {b}" for b in broken]
        repo_slug = os.environ.get("GITHUB_REPOSITORY", "")
        existing = api(
            f"https://api.github.com/repos/{repo_slug}/issues?state=open"
        )
        if existing is not None and any(i["title"] == title for i in existing):
            print("issue already open, skip")
        elif repo_slug:
            r = api(
                f"https://api.github.com/repos/{repo_slug}/issues",
                method="POST",
                payload={"title": title, "body": "\n".join(body_lines)},
            )
            print(f"filed issue: {r['html_url'] if r else 'FAILED'}")

    print(f"done: {len(repos)} checked, {len(stale)} stale, {len(broken)} broken")
    return 0


if __name__ == "__main__":
    sys.exit(main())
