from record import *
import difflib
w=BASE/'janitor'/'work'
run('janitor',['git','init','-b','main'],name='init.txt')
baseline=''.join(f'line{i:02d}: baseline\n' for i in range(1,41))
(w/'notes.txt').write_text(baseline)
run('janitor',['git','add','--','notes.txt'],name='fixture-baseline-add.txt')
run('janitor',['git','-c','user.name=Local Fixture','-c','user.email=fixture@example.invalid','commit','-m','fixture: initial text'],name='fixture-baseline-commit.txt')
# Setup authorized toy baseline only. No shared repository commit.
user=baseline.replace('line02: baseline','line02: user draft, keep unstaged')
task=baseline.replace('line30: baseline','line30: task improvement')
combined=user.replace('line30: baseline','line30: task improvement')
(w/'notes.txt').write_text(combined)
(EVID/'janitor/task-only.patch').write_text(''.join(difflib.unified_diff(baseline.splitlines(True),task.splitlines(True),fromfile='a/notes.txt',tofile='b/notes.txt')))
(w/'action-record.md').write_text('Target: notes.txt task line30 only; unrelated user line02 stays unstaged. Authority: original task explicitly says create committed toy baseline and stage task only; root clarified no-commit rule applies shared Skills repo. Reversible local index edit, no remote/collaborators. Precondition: baseline committed, both text edits unstaged, empty index. Rollback: git restore --staged -- notes.txt in this owned toy repo only, leaving working tree bytes intact. No rollback executed.\n')
run('janitor',['git','status','--porcelain=v1','-z','--untracked-files=all'],name='before-status.txt')
run('janitor',['git','diff','--cached'],name='before-staged.txt')
run('janitor',['git','diff','--','notes.txt'],name='before-unstaged.txt')
run('janitor',['git','worktree','list','--porcelain'],name='worktree-state.txt')
run('janitor',['git','apply','--cached','--check',str(EVID/'janitor/task-only.patch')],name='stage-preview.txt')
run('janitor',['git','apply','--cached',str(EVID/'janitor/task-only.patch')],name='stage-execution.txt')
a=run('janitor',['git','diff','--cached','--','notes.txt'],name='after-staged.txt')
b=run('janitor',['git','diff','--','notes.txt'],name='after-unstaged.txt')
run('janitor',['git','status','--short'],name='after-status.txt')
assert 'task improvement' in a.stdout and 'user draft' not in a.stdout
assert 'user draft' in b.stdout and 'task improvement' not in b.stdout
assert (w/'notes.txt').read_text()==combined
run('janitor',['git','log','--oneline','-3'],name='commit-scope.txt')
run('janitor',['git','remote','-v'],name='remote-state.txt')
report('janitor','''Executed in owned tiny Git repository only; no shared Skills Git staging/commit/push. Explicit original task and root clarification authorize one fixture baseline commit. Normal git init/add/commit created40-line notes.txt baseline; no plumbing bypass. Simulated user line02 draft and separate task line30 improvement in the same file.

Action: stage task line30 only through a task-specific cached patch, after status/staged/unstaged/worktree evidence and git apply --cached --check. Actual git apply --cached exit0. After staged diff contains only line30 task improvement; after unstaged diff contains only line02 user draft; full working file retains both. Status MM notes.txt reflects independent staged and unstaged content. Assertions on diffs/worktree bytes passed. One baseline commit in log; no task commit; remote list empty. Setup artifacts are untracked in the toy repository and were not added.

Authority/target/reversibility written before staging in output/action-record.md. Rollback for index only: git restore --staged -- notes.txt in owned toy repo, preserving working file; not executed because staged state is deliverable. No blanket add-all/reset/stash/clean, no history rewrite or push. Cached patch and raw before/after diff evidence saved; .git remains in temporary workspace and is excluded from output evidence copy.''','scoped-staging',['Toy local repo only; no remote/collaborator behavior tested.'])
