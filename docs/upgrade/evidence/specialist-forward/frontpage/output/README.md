# Tiny Notes CLI

Add and list notes in a local JSON file with the Python standard library. This is a single-file tool for trying a simple file-backed notes workflow.

From the directory containing `notes.py`, run:

```bash
python3 notes.py --help
```

Quickstart in a disposable copy of this directory:

```bash
python3 notes.py add "hello"
python3 notes.py list
```

Expected output:

```text
added note #1
1. hello
```

The example assumes the copy has no existing `notes.json`. Repeated runs append notes and increment the count. With no action, `python3 notes.py` lists notes.

Notes are stored in `notes.json` alongside [notes.py](notes.py). No package installation is required. This checkout has no declared minimum Python version or platform support matrix; the local verification runtime is recorded with the evidence, not a compatibility guarantee.

This tool has add/list commands only. It has no edit/delete, sync, authentication, SSO, audit log or AI summarization. Writes are plain JSON without locking or atomic replacement; avoid concurrent writers and protect the file yourself. Invalid JSON is not recovered automatically. This fixture supplies no package declaration, test suite or benchmark.
