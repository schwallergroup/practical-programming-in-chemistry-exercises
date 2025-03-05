# Week 5: Numerical operations, data handling, data visualization


# Setup

## Checking our conda environment

Welcome to week 5! Before running the exercise, we need to do a bit of set up. This week
we'll be learning about the Python packages `numpy`, `pandas`, and `matplotlib`.

Think back to exercise session 3 when we set up a conda environment. You'll remember that
we installed certain packages. More specifically, in the file
[Lecture03/README.md](../Lecture03/README.md), we ran the following commands:

```
conda create -n ppchem python=3.10
conda activate ppchem
pip install pandas  # installs numpy as dependency
pip install rdkit==2022.09.5
```

You can see that by running these, in our environment `ppchem`, we should already have
`numpy` and `pandas` installed. 

Open your terminal, activate your environment with `conda activate ppchem` and run the command `conda list`. The output should look something like this (output shortened):

```
# packages in environment at /opt/miniforge3/envs/ppchem:
#
# Name                    Version                   Build  Channel
anyio                     4.2.0                    pypi_0    pypi
appnope                   0.1.4                    pypi_0    pypi
...
numpy                     1.26.4                   pypi_0    pypi
...
pandas                    2.2.0                    pypi_0    pypi
pandocfilters             1.5.1                    pypi_0    pypi
parso                     0.8.3                    pypi_0    pypi
pexpect                   4.9.0                    pypi_0    pypi
pillow                    10.2.0                   pypi_0    pypi
pip                       24.0               pyhd8ed1ab_0    conda-forge
...
websocket-client          1.7.0                    pypi_0    pypi
wheel                     0.42.0             pyhd8ed1ab_0    conda-forge
xz                        5.2.6                h57fd34a_0    conda-forge
```

and you should be able to see `numpy` and `pandas` there. A better way to this, instead of manually searching this list would be to use the `grep` command.

For instance:

```bash
conda list | grep numpy
```
will output something like: `numpy    2.2.3  pypi_0    pypi`

while
```bash
conda list | grep pandas
```
will output something like: `pandas   2.2.3  pypi_0    pypi`

<details>
<summary>Explanation</summary>

* `grep` is used to search for text patterns. Here we are searching for the text pattern "numpy" or "pandas" in the output of the command `conda list`
* The pipe symbol `|` connects two commands, sending the output of the first command as input to the second command.
* When you run `conda list | grep numpy`, you're taking all your installed packages (from conda list) and filtering to only show lines containing "numpy".
* This approach is much faster than scanning through a long list manually, as it instantly shows you if and which versions of numpy or pandas are installed in your environment.

</details>

## Installing new packages and updating the environment file

**Note**: this section assumes that you have pushed your exported environment file to your personal
`ppchem` repository, as in the section "Export the environment to a file" in exercise 3. If this is not the case,
make sure you have followed all of the instructions before proceeding.

Next, we will install a new package in our environment and re-export the environment file. We will then push the updated `env.yml` to your personal `ppchem` repository.

In this step you will learn how to create a development branch in your repository, and merge your changes to the main branch via a *pull request*.

This can be done as follows:

1. In your terminal, navigate to your personal `ppchem` repository on your computer. This will be in the folder you created in a previous exercise, for example at `~/git/ppchem/`.
1. Make sure you have activated your conda environment (which is probably also called "ppchem"!): `conda activate ppchem`
1. Install matplotlib as follows: `pip install matplotlib`
1. Create a new branch: `git checkout -b update-env`
1. Export the environment file: `conda env export > env.yml`
1. Inspect the changes to the environment file compared to the last commit. This can be done by running `git diff env.yml`. Use your arrow keys to scroll. There may be a few changes, but most importantly you should see a line like: `+ - matplotlib==3.8.3`. This tells us that, relative to the last commit, matplotlib has been installed in the environment, at version number `3.8.3`. Press `q` to quit the git diff viewer.
1. Add the changes: `git add env.yml`
1. Commit them with a meaningful message: `git commit -m "Updated environment to include matplotlib"`
1. Push to your repository. As the remote doesn't yet know that we have created the branch `update-env` locally, we need to push with: `git push --set-upstream origin update-env`
   
Navigate to your repository on Github, at URL:
`https://github.com/<username>/ppchem`. You should
see a page like this:

![Pull Request 1](../assets/Lecture05/1.png)

Click the branch drop down menu where it says "main" to select a branch, and select the
branch "update-env":

![Pull Request 2](../assets/Lecture05/2.png)

You should see that your branch `update-env` is 1 commit ahead of main. We want to
create a pull request for this branch, so will click on the "contribute" button, and
select "Open pull request":

![Pull Request 3](../assets/Lecture05/3.png)

this will open a new page for opening a pull request:

![Pull Request 4](../assets/Lecture05/4.png)

Make sure you add a title and a short description of your pull request - i.e the changes
you have made and want to merge. Then, select "Create pull request". This will take you
to the pull request page.

On this page, this is typically where code reviews will be posted. Usually, if you are
contributing to an open source package, and want to merge some of your changes into the
main branch of the code, someone will review your work, request changes and leave
comments. This all happens on this page. 

As this is just your personal repository and the changes to the code weren't
significant, for now we will not do any review and just merge into main. Select "Merge
pull request":

![Pull Request 5](../assets/Lecture05/5.png)

and "Confirm merge":


![Pull Request 6](../assets/Lecture05/6.png)

then your pull request is merged! You can safely delete the branch associated with the
PR, as all the changes are now in main:

![Pull Request 7](../assets/Lecture05/7.png)

The pull request is accessible in the "Pull Requests" tab of the main repository page,
but will be in the 'closed' section.

Navigate back to your main repository landing page, i.e.
`https://github.com/<username>/ppchem` and check that the changes are there:

![Pull Request 8](../assets/Lecture05/8.png)

Finally, update the "Open a pull request" row of your Personal Milestones table with the
URL of the pull request.

For example, the URL of my (Joe's) PR was:
[https://github.com/jwa7/ppchem/pull/3](https://github.com/jwa7/ppchem/pull/3)

Good job! Now onto the exercises...