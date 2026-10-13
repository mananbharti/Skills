$ ['python3', 'exercise_readme.py']
exit: 0
stdout:
{"command": "python3 notes.py --help", "exit": 0, "stdout": "usage: notes.py [-h] [action] [text]\n\nTiny file-backed notes CLI.\n\npositional arguments:\n  action      add or list\n  text        note text for add\n\noptions:\n  -h, --help  show this help message and exit\n", "stderr": ""}
{"command": "python3 notes.py add \"hello\"", "exit": 0, "stdout": "added note #1\n", "stderr": ""}
{"command": "python3 notes.py list", "exit": 0, "stdout": "1. hello\n", "stderr": ""}

stderr:
