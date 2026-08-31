# Git And GitHub Setup Guide

Use this guide for CSCI171 and future programming classes that use GitHub. Follow the steps in order. If something on your screen does not match the instructions, stop and ask for help early. Clear is kind, and screenshots are very helpful.

## Already Completed In Class

Most CSCI171 students have already completed these steps in class. If you missed one, use this section to catch up. You may reuse these same setup habits in future classes.

### A. Create Or Check Your GitHub Account

1. Go to <https://github.com>.
2. Sign in or create a free account.
3. Use a username your instructor can recognize.
4. Add your Principia email in `Settings` > `Emails`.
5. Send your GitHub username to your instructor.
6. Open the course organization: <https://github.com/principia-business-cs>.

Done when: you can sign in, your instructor has your username, and you can open the organization page.

### B. Install Thonny

1. Download Thonny: <https://thonny.org/>.
2. Install and open it.
3. Type this program:

```python
print("Hello, CSCI171!")
```

4. Click `Run`.
5. If Thonny asks where to save the file, create a folder named `CSCI171`.

Done when: Thonny prints `Hello, CSCI171!`.

### C. Install Or Confirm Git

This has already been checked in class:

- Windows students downloaded Git and now have Git Bash.
- Mac students opened Terminal and confirmed that `git --version` shows a version number.

Catch-up links:

- Windows Git download: <https://git-scm.com/download/win>
- Mac Git download: <https://git-scm.com/download/mac>

Done when: Windows students can open Git Bash, and Mac students can run `git --version` in Terminal.

## Before You Continue

For CSCI171, you need:

- A GitHub account
- Git installed
- Windows students: Git Bash installed
- Mac students: Terminal can run `git --version`
- Thonny installed for Python programming
- Your assignment repository created from the class template

CSCI171 course links:

- Course organization: <https://github.com/principia-business-cs>
- Assignment template: <https://github.com/principia-business-cs/template-csci171-assignments>
- Instructor GitHub username: `anthonyackahnyanzu`

## 1. Check Git

Open the correct terminal:

- Windows: open `Git Bash`
- Mac: open `Terminal`

Run:

```bash
git --version
```

Done when you see a version number.

## 2. Tell Git Who You Are

Use your real name and your Principia email.

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@principia.edu"
git config --global init.defaultBranch main
```

Check it:

```bash
git config --global user.name
git config --global user.email
```

## 3. Quick Thonny Check

Open Thonny and run `print("Hello, CSCI171!")`. If it works, continue. If not, go back to the Thonny setup note at the top of this guide.

## 4. Create An SSH Key

SSH lets your computer talk to GitHub without using your GitHub password every time.

Run this command. Replace the email with your Principia email.

```bash
ssh-keygen -t ed25519 -C "your.email@principia.edu"
```

When it asks where to save the key, press `Enter`.

When it asks for a passphrase, press `Enter` twice if you want no passphrase. A passphrase is more secure, but no passphrase is simpler for this class.

Start the SSH agent:

```bash
eval "$(ssh-agent -s)"
```

Add your key:

```bash
ssh-add ~/.ssh/id_ed25519
```

## 5. Add Your SSH Key To GitHub

This SSH setup can be reused for future classes. Once your laptop is connected to GitHub, you usually do not need to create a new SSH key for every course.

Copy your public key.

Windows Git Bash or Mac Terminal:

```bash
cat ~/.ssh/id_ed25519.pub
```

Select and copy the entire line that starts with `ssh-ed25519`.

Then in GitHub:

1. Go to <https://github.com>.
2. Click your profile picture in the top-right corner.
3. Click `Settings`.
4. Click `SSH and GPG keys`.
5. Click `New SSH key`.
6. Title: `CSCI171 laptop`.
7. Key type: `Authentication Key`.
8. Paste the key.
9. Click `Add SSH key`.

Test it:

```bash
ssh -T git@github.com
```

If GitHub asks if you want to continue connecting, type:

```bash
yes
```

Success looks like this:

```text
Hi yourgithubusername! You've successfully authenticated...
```

It is okay if it also says GitHub does not provide shell access.

## 6. Create Your Assignment Repository

For CSCI171, you will use one personal assignment repo for the whole semester.

1. Open <https://github.com/principia-business-cs/template-csci171-assignments>.
2. Click `Use this template`.
3. Click `Create a new repository`.
4. Owner: choose your GitHub account.
5. Repository name: `fa26-csci171-yourgithubusername`.
6. Visibility: choose `Private`.
7. Click `Create repository`.

Example: if your GitHub username is `riverstudent`, your repo name is:

```text
fa26-csci171-riverstudent
```

## 7. Share Your Repo With Your Instructor

Do this once.

1. Open your assignment repo on GitHub.
2. Click `Settings`.
3. Click `Collaborators` or `Collaborators and teams`.
4. Click `Add people`.
5. Search for `anthonyackahnyanzu`.
6. Send the invitation.
7. Tell your instructor the invitation was sent.

## 8. Clone Your CSCI171 Repo To Your Computer

On your GitHub repo page:

1. Click the green `Code` button.
2. Click `SSH`.
3. Copy the link. It should look like this:

```text
git@github.com:yourgithubusername/fa26-csci171-yourgithubusername.git
```

In Git Bash or Terminal, choose a place for your class work:

```bash
mkdir CSCI171
cd CSCI171
```

Clone your repo. Replace `yourgithubusername` with your actual GitHub username.

```bash
git clone git@github.com:yourgithubusername/fa26-csci171-yourgithubusername.git
cd fa26-csci171-yourgithubusername
```

Check that it worked:

```bash
git status
```

Done when Git says you are on branch `main`.

## 9. Connect Your Repo To The CSCI171 Class Template

This lets you get new starter files when the instructor updates the template.

Important vocabulary:

- `origin` should be your own GitHub assignment repo.
- `template` should be the class starter-code repo.

Run this from inside your assignment repo folder:

```bash
git remote -v
```

You should already see `origin`. It should point to your repo, like this:

```text
git@github.com:yourgithubusername/fa26-csci171-yourgithubusername.git
```

Now add the class template as a second remote:

```bash
git remote add template git@github.com:principia-business-cs/template-csci171-assignments.git
git remote -v
```

You should see both `origin` and `template`.

If Git says `remote template already exists`, that is okay. Run `git remote -v` and continue.

If you do not see `origin`, add it with your own repo link. Replace `yourgithubusername` first:

```bash
git remote add origin git@github.com:yourgithubusername/fa26-csci171-yourgithubusername.git
git remote -v
```

Do not use the template repo as `origin`. `origin` is your repo.

## 10. Update A Repo You Already Created Earlier

Some students created their assignment repo before the latest starter files were added. Use this section to update your repo.

Run these commands from inside your assignment repo folder:

```bash
git switch main
git pull origin main
git remote -v
```

If you do not see `template`, add it:

```bash
git remote add template git@github.com:principia-business-cs/template-csci171-assignments.git
```

Now bring in the latest template files:

```bash
git fetch template
git merge template/main --allow-unrelated-histories
git push origin main
```

If Git says `Already up to date`, you already have the newest starter files.

If Git opens a text editor during the merge, ask for help. That is normal, but it is confusing the first time.

If Git reports a merge conflict, stop and ask for help before guessing.

## 11. Get Future Updates From The CSCI171 Template

Use this when the instructor says new CSCI171 starter files are available later in the semester.

```bash
git switch main
git pull origin main
git fetch template
git merge template/main --allow-unrelated-histories
git push origin main
```

## 12. Start Each Assignment On A Feature Branch

Each assignment gets its own branch. Use the exact branch name in the assignment instructions.

The pattern is:

```text
week-##-short-assignment-name
```

Examples:

```text
week-01-profile
week-02-calculator
week-03-decision-quiz
```

Start Week 1 like this:

```bash
git switch main
git pull origin main
git switch -c week-01-profile
```

Check your branch:

```bash
git branch
```

The branch with the `*` is the branch you are on.

Important: do not do your assignment work directly on `main`. Your assignment work goes on the assignment branch.

## 13. Work, Save, Commit, Push

After you edit your files and test your Python code, run:

```bash
git status
git add .
git commit -m "Complete week 01 profile"
git push -u origin week-01-profile
```

For later pushes on the same branch, you can use:

```bash
git push
```

## 14. Submit Your Assignment With A Pull Request

On GitHub:

1. Open your assignment repo.
2. Click `Compare & pull request`.
3. Base branch: `main`.
4. Compare branch: your assignment branch, such as `week-01-profile`.
5. Title: `Week 01 Profile`.
6. In the description, write one sentence about what works.
7. Click `Create pull request`.
8. Copy the PR link.
9. Submit the PR link in Canvas.

Do not merge your own assignment PR unless your instructor tells you to.

## Terminal Navigation Cheat Sheet

Use these in Git Bash or Mac Terminal.

| Goal | Command |
|---|---|
| Show your current folder | `pwd` |
| List files and folders | `ls` |
| Go into a folder | `cd folder-name` |
| Go up one folder | `cd ..` |
| Make a folder | `mkdir folder-name` |
| Clear the screen | `clear` |
| Show hidden files too | `ls -a` |

Helpful notes:

- Run Git commands from inside your repo folder.
- If `git status` says `not a git repository`, you are in the wrong folder. Use `cd` to move into your repo.
- Folder names are easier if you avoid spaces.

## Git Command Cheat Sheet

| Goal | Command |
|---|---|
| Check status | `git status` |
| See your branch | `git branch` |
| Switch to main | `git switch main` |
| Download latest main | `git pull origin main` |
| Create a feature branch | `git switch -c week-01-profile` |
| See changed lines | `git diff` |
| Stage changes | `git add .` |
| Commit changes | `git commit -m "Message here"` |
| Push first time | `git push -u origin week-01-profile` |
| Push after first time | `git push` |
| Check remote links | `git remote -v` |
| Add template remote | `git remote add template git@github.com:principia-business-cs/template-csci171-assignments.git` |
| Get template updates | `git fetch template` |
| Merge template updates | `git merge template/main --allow-unrelated-histories` |

## Common First Assignment Flow

```bash
cd CSCI171/fa26-csci171-yourgithubusername
git switch main
git pull origin main
git fetch template
git merge template/main --allow-unrelated-histories
git push origin main
git switch -c week-01-profile
# edit and test your Python files
git status
git add .
git commit -m "Complete week 01 profile"
git push -u origin week-01-profile
```

Then open a pull request on GitHub and submit the PR link in Canvas. In future classes, the repo name, template remote, and branch names may change, but this same workflow will still be useful.

## Common Problems

### `Permission denied (publickey)`

GitHub does not recognize your SSH key yet. Try:

```bash
ssh -T git@github.com
```

If that fails, go back to Step 4 and Step 5.

### `not a git repository`

You are probably in the wrong folder. Run:

```bash
pwd
ls
```

Then use `cd` to move into your assignment repo folder.

### `remote template already exists`

This is okay. Check it:

```bash
git remote -v
```

If you see `template`, continue.

### `fatal: a branch named ... already exists`

You already created that branch. Switch to it:

```bash
git switch week-01-profile
```

Use the correct branch name for your assignment.

## If Something Goes Wrong

Send your instructor:

- your GitHub username
- your repo link
- a screenshot or exact error message
- the command you ran
- the output of `git status`

Do not send your GitHub password.
