# Setup Step 3: Git And Assignments

Git and GitHub are how you will receive, save, and submit programming work.

For this course, students should use **HTTPS** clone links.

## What You Need First

Complete these before this step:

- [GitHub account setup](./01-github-account.md)
- [Thonny setup](./02-thonny.md)

## Step 1: Install Git

Go to:

https://git-scm.com/downloads

Download and install Git for your computer.

Windows students should keep the default installer options unless the instructor says otherwise.

## Step 2: Open A Terminal

Windows:

- Open PowerShell.

macOS:

- Open Terminal.

## Step 3: Check Git

Run:

```powershell
git --version
```

You should see a version number.

## Step 4: Set Your Name And Email

Use your own name and email:

```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.edu"
git config --global init.defaultBranch main
```

Check your settings:

```powershell
git config --global --list
```

## Step 5: Find Your Assignment Repository

Your instructor will give you a repository link.

It will look like this:

```text
https://github.com/principia-business-cs/fa26-csci171-i01-profile-yourusername
```

Open the link in your browser.

## Step 6: Clone The Repository

On the GitHub repository page:

1. Click the green `Code` button.
2. Choose `HTTPS`.
3. Copy the link.
4. Open PowerShell or Terminal.
5. Move to the folder where you want class work.

Example:

```powershell
mkdir CSCI171
cd CSCI171
git clone https://github.com/principia-business-cs/fa26-csci171-i01-profile-yourusername.git
cd fa26-csci171-i01-profile-yourusername
```

## Step 7: Work On The Assignment

Open the files in Thonny or your assigned editor.

Read the `README.md` first.

Then work on the Python file.

## Step 8: Save, Commit, And Push

Check what changed:

```powershell
git status
```

Stage your files:

```powershell
git add .
```

Commit your work:

```powershell
git commit -m "Complete assignment"
```

Push to GitHub:

```powershell
git push
```

## Step 9: Confirm Your Submission

Open your assignment repository in GitHub.

Refresh the page.

Confirm that your latest files appear online.

## Success Check

You are done when:

- `git --version` works.
- You can open your assignment repository.
- You can clone the repository.
- You can commit and push.
- Your changed files appear on GitHub.

## Common Problems

`git` is not recognized:

Git is not installed, or you opened the terminal before installation finished. Install Git, then close and reopen PowerShell or Terminal.

I cannot see the repository:

Make sure you are signed in to GitHub with the username you gave your instructor.

Git asks for login:

Use the browser login flow if it appears. Do not share your password with anyone.

GitHub does not show my changes:

Run:

```powershell
git status
git push
```

## Asking For Help

Include:

- Your GitHub username
- The repository link
- A screenshot or exact error message
- The command you ran
- The output of `git status`
