# ETERNITY-Calculator

## Context

Calculator application made using tkinter and custom tkinter in python for the course COMP 354.

## Basic Guidelines

Few things to consider to make the work easy for everyone!

### When You Work on Something

If you work on your button or any feature, create a branch locally (on your machine) and work on it. Do not directly work inside the main branch [please 🙂]. Make sure your branch name is explicit about what you are working on.

    git branch YourBranchName
    git switch YourBranchName

You should be familiar with these two commands or use the visual studio code interface:

    git add
    git commit -m

If you need to learn about them, search on google or ask the team.

### When You Want to Share Your Work

Before you decide to share your fantastic calculator button with the world and acquire the fame and the notoriety that you are waiting for. You must ensure you develop your work on the project's latest version, aka what is inside the main branch in the GitHub repo. You can run these commands to update your main branch locally:

    git switch main
    git pull

If new changes were added to your main branch, it means it was outdated. The world moves so fast it's crazy. You must merge the new changes of the main branch on your local branch to update your branch. Run these commands:

    git switch YourBranchName
    git merge main

⚠️
Merge conflict can occur. It means that you changed something that was changed in the main branch. You have to resolve these conflicts to make the merge successful. If you are uncertain, ask someone.
⚠️
You can bring your branch code into the GitHub repo when everything is correctly merged and committed.

    git push origin YourBranchName

On GitHub, create a merge request, then ping someone to review your code (respect the agreed design patterns) and test it (you can ask this person to do the test cases you wrote for your feature). If the review is good, push your code into the main branch using the GitHub user interface. Then ping the team that you made the change into the main branch.

### When You Want to Test the Branch of Someone Because You Are Serious and Dedicated

Before explaining to you how to do it, I want to first thank you for considering doing this.
If you want to test run a branch that is present on the GitHub repo, you have to import it on your computer. Run these commands to do so:

    git pull

And move inside the branch with (make sure you have committed the change you made on your current branch before moving to the other branch) :

    git switch NameOfTheBranchYouImported

## Set Up

To run the application, you must set up the pipenv virtual environment. This will allow us to share the same library version and ensure that everybody uses the same software.

For the Set Up, I assume that you have installed the following on your machine:

- Git
- Python version 3 or above

### 1 Clone The Repo

Navigate to a folder of your choice on your computer where you are comfortable storing the project using the command line interface (CLI) and Run:

    git clone https://github.com/alessioamo/ETERNITY-Calculator.git

A folder named "ETERNITY-Calculator" should be present in your chosen folder.

You have to be inside the project repo to do the next part. Make sure to navigate inside the folder "ETERNITY-Calculator" with your CLI.

    cd ETERNITY-Calculator

### 2 Installing Pipenv and Project Dependencies

If you do not already have pipenv in your machine. Run this command in your CLI:

    pip install pipenv

Install the dependencies of the project. Run this command in your CLI:

    pipenv install

### 3 Running the Application

In your VSCode CLI, run the command [Make sure you are at the same file location as the "app" file]:

    pipenv run python ./app.py

A window with the calculator should appear. Whenever you want to run the application locally for
testing/developing/etc. You just have to run the command above. You don't need to do steps 1 and 2 again.
