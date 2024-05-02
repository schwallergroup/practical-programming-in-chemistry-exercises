# Week 5: Setup

Welcome to week 5! The first thing we need to do for this week is sync our repository with the upstream repository, so you have access to the week 5 exercises. 

Here are the steps: 
1. Commit your changes
2. Push your changes 
3. Go on the Github website and hit the button that says "Sync to Upstream Repository"
4. Pull the updated repository 

It would be good practice for you to try and write the commands yourselves. If you get stuck, you can find some hints below. 

<details>
<summary>Hints</summary>

1. Make sure you're in your practical-programming-in-chemistry-exercises folder
2. `git add .` to stage all your changes 
3. `git commit -m "changes so far"`  to commit your changes
4. `git push` to push your changes to remote
5. Go on the Github website. There should be a nice button that says something like "Sync to upstream repository"
6. Go back to your terminal and type `git pull` to get the new exercises. 
</details>


Next, we need to change the versions of rdkit and pandas to make sure everything works properly. To do this, activate your ppchem conda environment (`conda activate ppchem`). We installed a slightly older version of rdkit and we want the newest one. Uninstall rdkit with `pip uninstall rdkit`. Now, reinstall rdkit with `conda install -c conda-forge rdkit` which will take the more recent version. We will repeat with pandas. Since we installed pandas with pip, we will uninstall it with pip: `pip uninstall pandas`. Now, we want version 2.1.4. Let's install it with `pip install pandas==2.1.4`. 

**Happy coding** :star_struck:
