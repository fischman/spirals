#!/usr/bin/env python3
"""Extract all user prompts from the Shelley conversation DB and write prompts.md."""

import json
import os
import sqlite3
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

DB_PATH = os.path.expanduser("~/.config/shelley/shelley.db")
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts.md")
TZ = ZoneInfo("America/Los_Angeles")

# Prompts that are repo/git housekeeping rather than product intent.
SKIP_PHRASES = [
    "what is your system prompt",
    "set the global git config",
    "rewrite history to drop all co-authored",
]


def should_skip(text: str) -> bool:
    lower = text.lower().strip()
    if lower in ("", "continue", "continue."):
        return True
    for phrase in SKIP_PHRASES:
        if phrase in lower:
            return True
    return False


def main():
    conn = sqlite3.connect(DB_PATH)
    # Get all conversations, filtering out secret ones
    convos = conn.execute(
        "SELECT conversation_id, slug FROM conversations ORDER BY created_at"
    ).fetchall()

    prompts: list[tuple[datetime, str, str]] = []  # (dt, slug, text)

    for cid, slug in convos:
        if slug and slug.lower().startswith("secret"):
            continue
        rows = conn.execute(
            """
            SELECT created_at, json_extract(llm_data, '$.Content[0].Text')
            FROM messages
            WHERE conversation_id = ?
              AND type = 'user'
              AND json_extract(llm_data, '$.Content[0].Type') = 2
              AND json_extract(llm_data, '$.Content[0].Text') != ''
            ORDER BY sequence_id
            """,
            (cid,),
        ).fetchall()
        for created_at, text in rows:
            if should_skip(text):
                continue
            # DB stores UTC timestamps
            dt = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S").replace(
                tzinfo=timezone.utc
            )
            prompts.append((dt, slug or "", text))

    conn.close()
    prompts.sort(key=lambda x: x[0])

    lines = ["# Prompts that built this project\n\n---\n"]
    for dt, slug, text in prompts:
        local = dt.astimezone(TZ)
        ts = local.strftime("%Y-%m-%d %H:%M %Z")
        lines.append(f"\n### `{ts}`\n")
        # Use a code block for the prompt text
        lines.append("```\n")
        lines.append(text.strip() + "\n")
        lines.append("```\n")

    with open(OUTPUT, "w") as f:
        f.writelines(lines)

    print(f"Wrote {len(prompts)} prompts to {OUTPUT}")


if __name__ == "__main__":
    main()
