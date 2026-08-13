# Setup Step 3: Git And Assignments

Git and GitHub are how you will get and submit programming work.

Students should use **HTTPS** links.

## Install Git

Download Git:

https://git-scm.com/downloads

Then open PowerShell on Windows or Terminal on macOS.

Check Git:

```powershell
git --version
```

## Configure Git

Use your own name and email:

```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.edu"
git config --global init.defaultBranch main
```

## Clone Your Semester Repository

Your instructor will give you one semester repository link like:

```text
https://github.com/principia-business-cs/fa26-csci171-yourusername
```

On GitHub, click `Code`, choose `HTTPS`, and copy the link.

Then run:

```powershell
mkdir CSCI171
cd CSCI171
git clone https://github.com/principia-business-cs/fa26-csci171-yourusername.git
cd fa26-csci171-yourusername
```

## Work On Assignments

Your semester repo will have folders like:

```text
week-01-profile/
week-02-calculator/
week-03-decision-quiz/
```

Open the current week's folder and read its `README.md` first.

## Submit Work

After editing and saving your files:

```powershell
git status
git add .
git commit -m "Complete assignment"
git push
```

Then refresh GitHub and confirm your files appear online.

## Group Builds

Most Wednesday group builds are practice, not GitHub turn-ins.

If your instructor asks for a reflection, submit it in Canvas.

## Done When

- `git --version` works.
- You can clone your semester repo.
- You can push your work.
- Your latest file appears on GitHub.

## Need Help?

Send your instructor:

- your GitHub username
- the repository link
- a screenshot or exact error message
- the command you ran
- the output of `git status`
