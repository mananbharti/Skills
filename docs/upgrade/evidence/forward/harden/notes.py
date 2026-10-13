"""Tiny notes app. Stdlib only (sqlite3, in-memory — no stray files).

Owner-scoped reads/deletes; configuration supplied through the environment.
"""

import os
import sqlite3

_CON = None


def _db():
    global _CON
    if _CON is None:
        _CON = sqlite3.connect(":memory:")
        _CON.execute(
            "CREATE TABLE notes (id INTEGER PRIMARY KEY, owner TEXT, body TEXT)"
        )
    return _CON


def get_secret():
    secret = os.environ.get("NOTES_SECRET")
    if not secret:
        raise RuntimeError("NOTES_SECRET must be configured")
    return secret


def seed():
    con = _db()
    con.execute("DELETE FROM notes")
    con.executemany(
        "INSERT INTO notes (owner, body) VALUES (?, ?)",
        [("amy", "amy private"), ("bob", "bob private")],
    )
    con.commit()


def get_note(username, note_id):
    con = _db()
    rows = con.execute(
        "SELECT id, owner, body FROM notes WHERE owner=? AND id=?",
        (username, note_id),
    ).fetchall()
    return rows


def delete_note(username, note_id):
    con = _db()
    cursor = con.execute("DELETE FROM notes WHERE owner=? AND id=?",
                         (username, note_id))
    con.commit()
    return cursor.rowcount == 1
