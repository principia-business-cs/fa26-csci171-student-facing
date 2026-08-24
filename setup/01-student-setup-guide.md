# CSCI171 Student Setup Guide

Follow these steps in order. Stop and ask for help as soon as something does not match the instructions.

## 1. Create Or Check Your GitHub Account

1. Go to <https://github.com>.
2. Sign in or create a free account.
3. Use a username your instructor can recognize.
4. Add your Principia email in `Settings` > `Emails`.
5. Send your GitHub username to your instructor.
6. Open the course organization: <https://github.com/principia-business-cs>.

Done when: you can sign in, your instructor has your username, and you can open the organization page.

## 2. Install Thonny

1. Download Thonny: <https://thonny.org/>.
2. Install and open it.
3. Type this program:

```python
print("Hello, CSCI171!")
```

4. Click `Run`.
5. If Thonny asks where to save the file, create a folder named `CSCI171`.

Done when: Thonny prints `Hello, CSCI171!`.

## 3. Install Git

Download Git: <https://git-scm.com/downloads>

Open PowerShell on Windows or Terminal on macOS and check it:

```powershell
git --version
```

Tell Git your name and email:

```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@principia.edu"
git config --global init.defaultBranch main
```

Done when: `git --version` shows a version number.

## 4. Create Your Assignment Repository

You will use one personal assignment repo for the semester. This avoids having a new repo every week.

1. Open the assignment template repo: <https://github.com/principia-business-cs/template-csci171-assignments>.
2. Click `Use this template`.
3. Choose `Create a new repository`.
4. Name it `fa26-csci171-yourgithubusername`.
5. Set visibility to `Private` if GitHub asks.
6. Create the repository.
7. Add your instructor as a collaborator using the steps below.

### Share Your Student-Owned Repo With Your Instructor

If the repo is under your own GitHub account, invite your instructor so they can review your pull requests.

1. Open your assignment repo on GitHub.
2. Click `Settings`.
3. Click `Collaborators` or `Collaborators and teams`.
4. Click `Add people`.
5. Search for your instructor's GitHub username: `anthonyackahnyanzu`.
6. Choose `anthonyackahnyanzu` and send the invitation.
7. Tell your instructor when the invitation is sent.

Use the same repo for the whole semester. You only need to invite the instructor once.

Your repo will already contain assignment folders like:

```text
individual-projects/week-01-profile/
individual-projects/week-02-calculator/
group-builds/week-01-error-detective/
```

Done when: you have your own repo, not just the template repo.

## 5. Clone Your Repo To Your Laptop

On your GitHub repo page, click `Code`, choose `HTTPS`, and copy the link.

Then run:

```powershell
mkdir CSCI171
cd CSCI171
git clone https://github.com/principia-business-cs/fa26-csci171-yourgithubusername.git
cd fa26-csci171-yourgithubusername
```

Replace `yourgithubusername` with your actual GitHub username.

Done when: the repo folder is on your laptop.

## 6. Start Each Assignment On A Branch

Each assignment gets its own feature branch. This lets your instructor fetch and grade one assignment at a time. Use the exact branch name listed in the assignment README.

From inside your assignment repo folder, run:

```powershell
git checkout main
git pull
git checkout -b week-01-profile
```

Branch names must match the assignment folder name exactly. Examples:

```text
week-01-profile
week-02-calculator
week-03-decision-quiz
```

Done when: `git status` shows you are on the exact branch named in the assignment README.


### Why Branch Names Must Match

Your instructor may clone your repo once, then use commands like these while grading:

```powershell
git fetch --all
git checkout week-01-profile
git pull
```

That only works smoothly if everyone uses the same branch name for the same assignment.

## 7. Complete The Assignment

1. Open the current assignment folder.
2. Read its `README.md` first.
3. Edit the starter Python file.
4. Run and test your code in Thonny.
5. Save your work.

For Friday individual projects, your work must be your own. You can ask questions, but you must understand and explain your code.

## 8. Push Your Branch

From inside your assignment repo folder, run:

```powershell
git status
git add .
git commit -m "Complete week 01 profile"
git push -u origin week-01-profile
```

Replace `week-01-profile` with the exact branch name from the assignment README.

Done when: GitHub shows your branch online.

## 9. Open A Pull Request

1. Go to your assignment repo on GitHub.
2. Click `Compare & pull request` for your branch.
3. Set `base` to `main`.
4. Set `compare` to your assignment branch.
5. Title the PR with the assignment name, such as `Week 01 Profile`.
6. In the PR description, write one sentence about what works and one question or note if you have one.
7. Click `Create pull request`.
8. Copy the PR link.
9. Submit the PR link in Canvas.

Do not merge your own assignment PR unless your instructor tells you to. Do not delete the branch until the assignment has been graded.

Done when: Canvas has the PR link and your PR is open on GitHub.

## 10. Group Builds

Wednesday group builds are usually practice, not a full code turn-in.

You should still keep your own copy of useful group code or notes in your repo. If Canvas asks for a group reflection, submit the reflection in Canvas.

## Git Command Cheat Sheet

Use these commands from inside your assignment repo folder.

| Goal | Command |
|---|---|
| Check where you are | `pwd` |
| List files | `dir` on Windows, `ls` on macOS |
| Check Git status | `git status` |
| See what changed | `git diff` |
| Download latest changes | `git pull` |
| Switch to main | `git checkout main` |
| Create an assignment branch | `git checkout -b week-01-profile` |
| Stage all changed files | `git add .` |
| Save a checkpoint | `git commit -m "Message here"` |
| Upload first push of a branch | `git push -u origin week-01-profile` |
| Upload later commits | `git push` |
| See recent commits | `git log --oneline -5` |
| Check your remote link | `git remote -v` |

Common first-assignment sequence:

```powershell
cd CSCI171\fa26-csci171-yourgithubusername
git checkout main
git pull
git checkout -b week-01-profile
# edit and save your files
git status
git add .
git commit -m "Complete week 01 profile"
git push -u origin week-01-profile
```

Then open a pull request on GitHub and submit the PR link in Canvas. Your instructor will grade the branch named in that PR. For the next assignment, start again from `main` after your instructor has reviewed or merged the previous PR.

## If Something Goes Wrong

Send your instructor:

- your GitHub username
- the repo link
- a screenshot or exact error message
- the command you ran
- the output of `git status`

Do not send your password.
