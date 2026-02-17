# Lecture 01: Setting Up Your Computer

This lecture focuses on setting up the essential tools you'll need throughout the course. We'll walk through installing the necessary software and getting comfortable with the command line.

## Required Software Installation

### 1. Terminal Setup
- **Windows Users**: Install Git Bash
  1. Download Git Bash from the [official website](https://git-scm.com/download/win)
     ![Downloading git bash](/assets/git_bash_download.png)
  3. Run the installer, accepting default settings
  4. Verify installation by opening Git Bash and typing `git --version`

- **macOS Users**: Use the built-in Terminal
  1. Press `Cmd + Space`, type "Terminal", and press Enter
  2. Update your command line tools by running: `xcode-select --install`
  3. Check that Git is installed by typing `git --version` in your terminal.

### 2. Visual Studio Code
1. Download VS Code from the [official website](https://code.visualstudio.com/)
2. Open VS Code and install the following extensions:
   - Python (by Microsoft)
   - Jupyter
   ![Install Extensions in VS Code](/assets/vscode_extensions.png)

More about VS Code extensions from the [official documentation](https://code.visualstudio.com/docs/editor/extension-marketplace).

### 3. Anaconda Installation

**macOS users**
1. Download Anaconda from the [official website](https://www.anaconda.com/download/success))
   - [Check your processor type](https://support.apple.com/en-us/HT211814) (Intel or Apple Silicon:  > `About This Mac` > Check `Chip` line) 
2. Run the installer
3. Verify installation by opening your terminal (`Cmd + Space`, type "Terminal") and running:
   ```bash
   conda --version
   ```
**Windows users**
1. Download Anaconda from the [official website](https://www.anaconda.com/download/success))
   - Choose the appropriate installer (64-bit recommended)
2. Run the installer
   - ⚠️ Folder destination: Do **not** accept the default path (`C:\Users\<your-username>\Anaconda3\`) **if** your path contains spaces (e.g. `C:\Name Surname`) or characters outside the 7-bit ASCII character set like accents (e.g. `C:\Joëlle-Françoise L’Héritier`). Instead, **save it here**: `C:\anaconda`
   - ⚠️ When prompted, check "Add Anaconda to my PATH environment variable"
      ![Add conda to PATH](../assets/windows_conda_path.png)
4. Verify installation by opening git bash (might have to reopen for changes to take effect) and running:
   ```bash
   conda --version
   ```

<details>
<summary>Some help for Windows installation</summary>
  
  These are mostly for the TAs to help you
  
- [Detailed Anaconda installation instructions](https://docs.anaconda.com/working-with-conda/reference/faq/#installing-anaconda)
- [conda: command not found on Windows](https://stackoverflow.com/questions/54501167/anaconda-and-git-bash-in-windows-conda-command-not-found)
      
</details>

## GitHub Setup

### 1. Create a GitHub Account
1. Go to [GitHub](https://github.com) and click "Sign Up"
2. Use your academic email for potential benefits
3. Choose a professional username
4. Complete the verification process

<details>
<summary>Detailed steps</summary>

1. Open your web browser and navigate to https://github.com/.
2. Click on the `Sign Up` button located in the top right corner of GitHub’s homepage.
3. On the next page, provide the required details including a new `Username`, a `valid Email Address` (EPFL address recommended for step 8.), and a `Password`. Make sure to verify that the password is at least 15 characters long or at least 8 characters long with a combination of letters, numbers, and symbols.
4. Review GitHub’s Terms of Service and Privacy Statement, and if you agree, click on `Create an account`.
5. Next, you might be guided through a few survey questions. You can answer them or directly click on `Complete Setup`.
6. You’ll be sent an email to the address you provided. In that email, click `Verify email address`.
7. That’s it! You should now have a GitHub account.
8. (Optional) The GitHub Student Developer Pack is a free offer from GitHub specially for students. It provides access to a variety of premium development tools and services free of charge for as long as you’re a student. [GitHub Student Developer Pack](https://education.github.com/pack)
</details>

### 2. Configure GitHub locally (on your computer)
1. Configure your username and email address by typing the following commands in your terminal/Git Bash:
```bash
git config --global user.name "Your Name" # Replace with your GitHub username
git config --global user.email "user@epfl.ch" # Replace with the associated email address
```
2. Check that your configuration was successful by typing (leave file by pressing `q`):
```bash
git config --global --list
```

### 3. Log into GitHub on VS Code

1. Open VS Code
2. Insall the required extension `GitHub Pull Requests and Issues`
3. Sign in by clicking on the GitHub tab on the left (cat-like icon below the extensions tab)

## Terminal Commands Overview

Here are the essential terminal commands you'll need for navigating your computer and working with files:

| Function | macOS/Linux Command/Windows Git Bash |
|----------|------------------------|
| Navigate to home directory | `cd ~` | 
| Change directory | `cd directoryName` | 
| Go up one folder | `cd ..` | 
| Navigate to directory with spaces | `cd "directory Name"` |
| Show current directory | `pwd` | 
| List files in current directory | `ls` | 
| Make a new directory in the current directory | `mkdir directoryName` | 
| Remove a file | `rm fileName` | 
| Remove a directory | `rm -r directoryName` |
| Copy a file with path `source` to path `destination` | `cp source destination` | 
| Move or rename a file with name `source` to new name `destination` | `mv source destination` | 

## Terminal Exercises

### Exercise 1: Basic Navigation
1. Open your terminal (Git Bash for Windows)
2. Navigate to your home directory using `cd ~`
3. Check your current location using `pwd`
4. List all files in your current directory using `ls`
5. Create a new directory called `python-course` using `mkdir`
6. Navigate into that directory
7. Verify you're in the correct directory using `pwd`

### Exercise 2: Working with Files and Directories
1. Inside `python-course`, create three directories (using `mkdir`):
   - `exercises`
   - `notes`
   - `projects`
2. List the contents of `python-course` to verify the directories were created (using `ls`)
3. Navigate into `exercises`
4. Create a file called `week1.txt` (you can use `touch week1.txt` on Mac/Unix/Git Bash)
5. Move back up to the `python-course` directory (using `cd ..`)
6. Create another file called `todo.txt` in the `notes` directory
7. Copy `todo.txt` from `notes` to `projects` (using `cp`)

### Exercise 3: Advanced File Operations
1. Create a directory called `temp` in `python-course`
2. Create files called `file1.txt`, `file2.txt`, and `file3.txt` in `temp`
3. Create a new directory called `backup`
4. Copy all files from `temp` to `backup`
5. List the contents of both directories to verify the files were copied
6. Remove the `temp` directory and its contents
7. Verify the files still exist in `backup`

### Exercise 4: Play the bashcrawl game (optional)
This is a fun way to learn a lot more bash commands, play as long as you want (we don't expect you to finish it).

You can either download the game locally or play it through Binder online.

**Local game**
1. Download [BashCrawl game](https://gitlab.com/slackermedia/bashcrawl/-/archive/stable-2024.02.09/bashcrawl-stable-2024.02.09.zip).
2. Unzip it. 
3. In your terminal/Git bash using `cd`, navigate to the folder `bashcrawl-stable-2024.02.09`
4. cd `entrance`
5. `cat scroll` to read the instructions

**Through Binder (online)**
1. Open [https://mybinder.org/v2/gl/nthiery%2Fbashcrawl/HEAD](https://mybinder.org/v2/gl/nthiery%2Fbashcrawl/HEAD).
2. Wait for a minute or two
3. Once the interface has loaded, click on Terminal (bottom left)
4. Run `cat scroll` to read the instructions


## Common Issues and Solutions

1. **Git Bash not recognized in Windows**
   - Restart your computer after installation
   - Verify PATH variables in System Environment Variables

2. **Anaconda not found in terminal**
   - Restart your terminal
   - Check if PATH was properly set during installation

3. **GitHub authentication fails**
   - Make sure you're using your PAT as the password, not your GitHub password
   - Regenerate PAT if necessary

