# Setup Step 4: Fresh Assignment Repo Creation

Use this guide after deleting your old assignment repo. Your SSH key should already be set up.

Goal: create a new empty assignment repo, clone it into a folder named `CSCI171` inside your user profile, and submit assignments with branches and pull requests.

Important: do **not** create your repo from the template, and do **not** connect the template repo as a Git remote. When starter files are needed, your instructor will tell you which files to download or copy.

## Links You Need

- Course organization: <https://github.com/principia-business-cs>
- Starter/template files, when assigned: <https://github.com/principia-business-cs/template-csci171-assignments>
- Instructor GitHub username: `anthonyackahnyanzu`

## 1. Create Your New Empty Repo

1. Go to <https://github.com/new>.
2. Owner: choose your own GitHub account.
3. Repository name: `fa26-csci171-yourgithubusername`.
4. Visibility: choose `Private`.
5. Do not choose a template.
6. Check `Add a README file`.
7. Click `Create repository`.

Example: if your GitHub username is `riverstudent`, your repo name is:

```text
fa26-csci171-riverstudent
```

## 2. Share Your Repo With Your Instructor

Do this once.

1. Open your new assignment repo on GitHub.
2. Click `Settings`.
3. Click `Collaborators` or `Collaborators and teams`.
4. Click `Add people`.
5. Search for `anthonyackahnyanzu`.
6. Send the invitation.
7. Tell your instructor the invitation was sent.

## 3. Copy The SSH Clone Link

On your new GitHub repo page:

1. Click the green `Code` button.
2. Click `SSH`.
3. Copy the link.

It should look like this:

```text
git@github.com:yourgithubusername/fa26-csci171-yourgithubusername.git
```

If the link starts with `https://`, switch to the `SSH` tab before copying.

## 4. Open The Correct Terminal

Use the terminal for your computer:

- Windows: open `Git Bash`
- Mac: open `Terminal`

Type one command at a time and press `Enter` after each command.

Helpful notes:

- Do not type the `$` or `%` prompt if you see one in examples online.
- Spelling, spaces, and punctuation matter.
- Use the up arrow to reuse a command you already typed.
- If you feel lost, run `pwd` and `ls`, then ask for help with a screenshot.

## 5. Go To Your User Profile Folder

Your repo should be cloned inside a folder named `CSCI171` in your user profile.

### Windows Git Bash

Run:

```bash
cd ~
pwd
```

Your `pwd` output should look something like:

```text
/c/Users/YourName
```

### Mac Terminal

Run:

```bash
cd ~
pwd
```

Your `pwd` output should look something like:

```text
/Users/YourName
```

`~` means your user profile folder. Starting here keeps everyone's class files in a predictable place.

## 6. Create And Enter The CSCI171 Folder

Run these commands in Git Bash or Mac Terminal:

```bash
mkdir -p CSCI171
cd CSCI171
pwd
```

Your `pwd` output should now end with:

```text
CSCI171
```

That means you are inside the class folder.

## 7. Clone Your New Repo

Replace `yourgithubusername` with your actual GitHub username.

```bash
git clone git@github.com:yourgithubusername/fa26-csci171-yourgithubusername.git
cd fa26-csci171-yourgithubusername
git status
```

Done when `git status` says you are on branch `main`.

## 8. Check Your Remote

Your repo should have only one remote for normal class work:

- `origin`: your own assignment repo

Check it:

```bash
git remote -v
```

`origin` should look like this, with your username:

```text
git@github.com:yourgithubusername/fa26-csci171-yourgithubusername.git
```

Do not add the class template repo as a remote.

If `origin` accidentally points to the template repo, fix it:

```bash
git remote remove origin
git remote add origin git@github.com:yourgithubusername/fa26-csci171-yourgithubusername.git
git remote -v
```

Replace `yourgithubusername` before running the command.

## 9. Download Starter Files When Assigned

When starter files are needed, your instructor will tell you exactly which folder or file to use from:

<https://github.com/principia-business-cs/template-csci171-assignments>

Do **not** use `git remote add template`, `git fetch template`, or `git merge template/main`.

Instead, use one of these simple options when your instructor tells you to:

- Download the needed file from GitHub and move it into your repo folder.
- Download the needed folder as a `.zip`, unzip it, and copy the assignment folder into your repo.
- Copy code from a class file only when your instructor says that is allowed.

After copying starter files into your repo, save them with Git:

```bash
git status
git add .
git commit -m "Add starter files"
git push origin main
```

## 10. Start An Assignment Branch

Each assignment should be done on its own branch.

Branch name pattern:

```text
week-##-assignment-name
```

Examples:

```text
week-01-profile
week-02-calculator
week-03-decision-quiz
```

Start from `main`, then create the branch:

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

## 11. Save, Commit, And Push Your Work

After you edit and test your assignment files:

```bash
git status
git add .
git commit -m "Complete week 01 profile"
git push -u origin week-01-profile
```

For later pushes on the same branch, use:

```bash
git push
```

## 12. Submit With A Pull Request

On GitHub:

1. Open your assignment repo.
2. Click `Compare & pull request`.
3. Base branch: `main`.
4. Compare branch: your assignment branch, such as `week-01-profile`.
5. Title: `Week 01 Profile`.
6. Write one sentence about what works.
7. Click `Create pull request`.
8. Copy the PR link.
9. Submit the PR link in Canvas.

Do not merge your own pull request unless your instructor tells you to.

## Quick Terminal Commands

| Goal | Command |
|---|---|
| Go to your user profile folder | `cd ~` |
| Show where you are | `pwd` |
| List files and folders | `ls` |
| Make the class folder | `mkdir -p CSCI171` |
| Enter the class folder | `cd CSCI171` |
| Go up one folder | `cd ..` |
| Clear the screen | `clear` |

## Quick Git Commands

| Goal | Command |
|---|---|
| Check repo status | `git status` |
| Check branch | `git branch` |
| Check remotes | `git remote -v` |
| Switch to main | `git switch main` |
| Pull latest main | `git pull origin main` |
| Create branch | `git switch -c week-01-profile` |
| Stage files | `git add .` |
| Commit files | `git commit -m "Complete week 01 profile"` |
| Push first time | `git push -u origin week-01-profile` |
| Push later changes | `git push` |

## Need Help?

Send your instructor:

- your GitHub username
- your repo link
- a screenshot or exact error message
- the command you ran
- the output of `pwd`
- the output of `git remote -v`
- the output of `git status`

Do not send your GitHub password.
