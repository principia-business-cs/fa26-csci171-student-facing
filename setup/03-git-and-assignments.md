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

## Clone An Assignment

Your instructor will give you a repository link like:

```text
https://github.com/principia-business-cs/fa26-csci171-i01-profile-yourusername
```

On GitHub, click `Code`, choose `HTTPS`, and copy the link.

Then run:

```powershell
mkdir CSCI171
cd CSCI171
git clone https://github.com/principia-business-cs/fa26-csci171-i01-profile-yourusername.git
cd fa26-csci171-i01-profile-yourusername
```

## Submit Work

After editing and saving your files:

```powershell
git status
git add .
git commit -m "Complete assignment"
git push
```

Then refresh GitHub and confirm your files appear online.

## Done When

- `git --version` works.
- You can clone your assignment repo.
- You can push your work.
- Your latest file appears on GitHub.

## Need Help?

Send your instructor:

- your GitHub username
- the repository link
- a screenshot or exact error message
- the command you ran
- the output of `git status`
