# Project 0 GitHub Setup Guide

Use this guide to get ready for every programming assignment in CSCI171. Follow the steps in order. If your screen does not match the guide, stop and ask for help with a screenshot.

## GitHub In Plain English

- GitHub is a website that stores your code online.
- A repository, or repo, is a project folder on GitHub.
- Your local repo is the copy on your computer.
- `main` is the clean branch of your repo.
- A feature branch is where you do one assignment.
- A commit is a saved checkpoint.
- A push sends your commits to GitHub.
- A pull request, or PR, is the link you submit so your instructor can review your work.

For this class, you will use one private repo for the semester. Each assignment gets its own branch and pull request.

## What You Need First

- GitHub account
- Git installed
- Windows: Git Bash
- Mac: Terminal with `git --version` working
- Your instructor's GitHub username: `anthonyackahnyanzu`

## 1. Check Git

Open the right terminal:

- Windows: open `Git Bash`
- Mac: open `Terminal`

Run:

```bash
git --version
```

You should see a version number.

## 2. Tell Git Who You Are

Use your real name and Principia email.

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

## 3. Set Up SSH For GitHub

SSH lets your computer connect to GitHub without using your GitHub password for every push.

Create a key. Replace the email first.

```bash
ssh-keygen -t ed25519 -C "your.email@principia.edu"
```

When asked where to save it, press `Enter`.

When asked for a passphrase, press `Enter` twice for no passphrase, or choose a passphrase you will remember.

Start the SSH agent:

```bash
eval "$(ssh-agent -s)"
```

Add your key:

```bash
ssh-add ~/.ssh/id_ed25519
```

Show your public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the whole line that starts with `ssh-ed25519`.

## 4. Add The SSH Key To GitHub

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

If asked if you want to continue connecting, type:

```bash
yes
```

Success looks like this:

```text
Hi yourgithubusername! You've successfully authenticated...
```

It is okay if GitHub also says it does not provide shell access.


## SSH Reset Option: Delete Old Keys And Start Fresh

Use this section only if SSH is still broken after you try `ssh -T git@github.com`, or if your instructor tells you to reset your SSH setup.

### A. Delete The Old Key From GitHub

1. Go to <https://github.com>.
2. Click your profile picture.
3. Click `Settings`.
4. Click `SSH and GPG keys`.
5. Find the old class/laptop key.
6. Click `Delete` for that key.

If you are not sure which key to delete, ask for help before deleting it.

### B. Move The Old Local Key Out Of The Way

In Git Bash or Mac Terminal, run:

```bash
mkdir -p ~/.ssh/old-keys
mv ~/.ssh/id_ed25519 ~/.ssh/old-keys/id_ed25519_old
mv ~/.ssh/id_ed25519.pub ~/.ssh/old-keys/id_ed25519_old.pub
```

If one of those files does not exist, that is okay. Continue with the next command.

### C. Create And Add A New Key

Run the SSH setup again:

```bash
ssh-keygen -t ed25519 -C "your.email@principia.edu"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
```

Copy the new public key and add it to GitHub using Step 4 above.

Test again:

```bash
ssh -T git@github.com
```

Success means you can continue with cloning or pushing.

## 5. Create Your Private Class Repo

1. Go to <https://github.com/new>.
2. Owner: choose your GitHub account.
3. Repository name: `fa26-csci171-yourgithubusername`.
4. Visibility: `Private`.
5. Do not choose a template.
6. Check `Add a README file`.
7. Click `Create repository`.

Example for a student named River:

```text
fa26-csci171-riverstudent
```

## 6. Share The Repo With Your Instructor

1. Open your new repo on GitHub.
2. Click `Settings`.
3. Click `Collaborators` or `Collaborators and teams`.
4. Click `Add people`.
5. Search for `anthonyackahnyanzu`.
6. Send the invitation.

## 7. Clone The Repo To Your Computer

On your repo page:

1. Click the green `Code` button.
2. Choose `SSH`.
3. Copy the link. It should look like this:

```text
git@github.com:yourgithubusername/fa26-csci171-yourgithubusername.git
```

Now use Git Bash or Terminal.

### Windows Git Bash

```bash
cd ~
pwd
mkdir -p CSCI171
cd CSCI171
git clone git@github.com:yourgithubusername/fa26-csci171-yourgithubusername.git
cd fa26-csci171-yourgithubusername
git status
```

Your first `pwd` should look like `/c/Users/YourName`.

### Mac Terminal

```bash
cd ~
pwd
mkdir -p CSCI171
cd CSCI171
git clone git@github.com:yourgithubusername/fa26-csci171-yourgithubusername.git
cd fa26-csci171-yourgithubusername
git status
```

Your first `pwd` should look like `/Users/YourName`.

Done when `git status` says you are on branch `main`.

## 8. Check The Remote

Run this inside your repo folder:

```bash
git remote -v
```

`origin` should point to your own repo:

```text
git@github.com:yourgithubusername/fa26-csci171-yourgithubusername.git
```

Do not connect the class template repo as a remote.

## 9. Create The Project 0 Branch

Run these commands inside your repo folder:

```bash
git switch main
git pull origin main
git switch -c project-00-github-setup
```

Check your branch:

```bash
git branch
```

The branch with `*` should be `project-00-github-setup`.

## 10. Add Your Setup Notes

Create or edit `notes.md` in your repo. Include:

```text
Name:
Repository URL:
One setup issue I solved or one command I practiced:
```

Then save your work with Git:

```bash
git status
git add .
git commit -m "Complete project 0 setup"
git push -u origin project-00-github-setup
```

## 11. Open And Submit A Pull Request

On GitHub:

1. Open your repo.
2. Click `Compare & pull request`.
3. Base branch: `main`.
4. Compare branch: `project-00-github-setup`.
5. Title: `Project 0 GitHub Setup`.
6. Write one sentence about what works.
7. Click `Create pull request`.
8. Copy the PR link.
9. Submit the PR link in Canvas.

Do not merge your own PR unless your instructor tells you to.

## Starting A New Assignment

Use this same pattern every time a new assignment is posted. The branch name matters because it helps your instructor find and grade the correct work.

1. Open Git Bash or Terminal.
2. Go to your class repo:

```bash
cd ~/CSCI171/fa26-csci171-yourgithubusername
```

3. Make sure you are starting from `main`:

```bash
git switch main
```

4. Get your latest saved work from GitHub:

```bash
git pull origin main
```

5. Create a new branch for the assignment. Use the exact branch name listed in the assignment README.

```bash
git switch -c assignment-week-03-individual
```

6. Copy or download any starter file linked from the assignment directions, if the assignment uses one.
7. Work on the assignment in VS Code or Thonny.
8. Test your program before submitting:

```bash
python your_file_name.py
```

9. Check what changed:

```bash
git status
```

10. Add, commit, and push your work:

```bash
git add .
git commit -m "Complete week 03 individual assignment"
git push -u origin assignment-week-03-individual
```

11. Open your repo on GitHub and create a pull request from your assignment branch into `main`.
12. Submit the pull request link in Canvas.

If you accidentally start work on `main`, stop and ask for help. That is fixable, and it is much easier to fix before you keep working.

## Terminal Cheat Sheet

| Goal | Command |
|---|---|
| Show current folder | `pwd` |
| List files | `ls` |
| Go to user folder | `cd ~` |
| Make class folder | `mkdir -p CSCI171` |
| Enter folder | `cd folder-name` |
| Go up one folder | `cd ..` |
| Clear screen | `clear` |

## Git Cheat Sheet

| Goal | Command |
|---|---|
| Check status | `git status` |
| Check branch | `git branch` |
| Check remote | `git remote -v` |
| Switch to main | `git switch main` |
| Pull latest main | `git pull origin main` |
| Create branch | `git switch -c project-00-github-setup` |
| Stage files | `git add .` |
| Commit files | `git commit -m "Complete project 0 setup"` |
| Push branch first time | `git push -u origin project-00-github-setup` |
| Push later changes | `git push` |

## Common Problems

### `Permission denied (publickey)`

GitHub does not recognize your SSH key. Recheck Steps 3 and 4, then run:

```bash
ssh -T git@github.com
```

If SSH still fails after that, use the SSH Reset Option above to remove the old key from GitHub and create a fresh one.

### `not a git repository`

You are in the wrong folder. Run:

```bash
pwd
ls
```

Then `cd` into your repo folder.

### `origin` points to the wrong repo

Fix it like this, replacing your username:

```bash
git remote remove origin
git remote add origin git@github.com:yourgithubusername/fa26-csci171-yourgithubusername.git
git remote -v
```

## What To Send If You Need Help

Send your instructor:

- your GitHub username
- your repo link
- a screenshot or exact error message
- the command you ran
- the output of `pwd`
- the output of `git status`
- the output of `git remote -v`

Do not send your GitHub password.


