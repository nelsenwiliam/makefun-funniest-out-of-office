#!/usr/bin/env python3
"""The Funniest Out-of-Office -- make.fun entry.

Writes one line of an out-of-office auto-reply to /output/entry.txt,
where the program/v1 harness reads it. Pure standard library.

The line was picked from 10 candidates scored against the judge's
brief, in the judge's own order: a reply a real person would set,
a genuine surprise, a voice of its own, freshness, and no wasted word.
The winner turns the medium itself into the joke: an auto-reply is
the one reply nobody waits for, so bragging that it is the fastest
reply ever sent is both true and absurd -- the twist lands because
the reader realises the "reply" they just got required no one at all.
"""

import os

# Ten candidates, scored against the judge's brief in its own order
# (real OOO feel, surprise, own voice, freshness, no wasted word).
# 1. "fastest reply" -- the winner: the medium itself is the joke.
# 2. "unread, unloved" -- good rhythm, but the twist is only mild.
# 3. "on reflection, no" -- sharp punchline, weak as a real OOO.
# 4. "longer than my handover" -- relatable, twist too gentle.
# 5. "subject line 'I read your auto-reply'" -- meta, slightly wordy.
# 6. "so I wouldn't have to talk to anyone" -- strong voice, long.
# 7. "we're both ignoring you" -- cute, personification is familiar.
# 8. "in the order it was ignored" -- queue jokes are well-worn.
# 9. "lower your standards" -- strong voice, "ask someone else" is a trope.
# 10. "forwarded to Future Me" -- Future Me is a known joke format.
CANDIDATES = (
    "I'm out until Monday. This auto-reply is the fastest reply I've ever sent you.",
    "I'm out of office. Your email is safe with me -- unread, unloved, and exactly where I left it.",
    "I'm away until Friday. I read your email, and on reflection, no.",
    "I'm on annual leave. This auto-reply took longer to write than my handover.",
    "I'm away. If this is urgent, please resend it with the subject line 'I read your auto-reply'.",
    "I'm out until Tuesday. I wrote this auto-reply so I wouldn't have to talk to anyone, and honestly, it's working.",
    "I'm on holiday until the 9th. My inbox came with me and we're both ignoring you.",
    "I'm out of office until Monday. My inbox will be answered in the order it was ignored.",
    "I'm away until Monday. If you need me urgently, lower your standards and ask someone else.",
    "I'm out. Your email has been forwarded to Future Me, who also doesn't want to deal with it.",
)

LINE = CANDIDATES[0]


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 140, "entry must be 1 to 140 characters, got %d" % len(line)
    assert "\n" not in line, "entry must be a single line"
    assert line.endswith("."), "entry must end with a period"
    assert all(1 <= len(c.strip()) <= 140 for c in CANDIDATES), "all candidates must fit 140 chars"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == line, "read-back mismatch: file differs from entry"


if __name__ == "__main__":
    main()
