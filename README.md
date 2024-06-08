# CSM 16B Repository

This directory contains all the material developed for CSM 16B.

For developing, please read through [`LaTeX-best-practices.md`](./00-LaTeX-best-practices.md) for a list of guidelines for writing LaTeX, and the following guide on [`Git`](https://rogerdudler.github.io/git-guide/)

The documents here are written in LaTeX by a team. Adhering to these guidelines will help avoid conflict resolution
and allow the writing process to be collaborative.

# Organization of this repository

    fa19/               - Content for the Fa19 semester 
    questionBank/       - Central source for all questions
    testing/            - Testing directory

## `fa19/`
Inside each semester's directory, there are subfolders for each week's worksheets. Inside that folder, let's say 01/, there will be multiple LaTeX files: ws01.tex, meta01.tex, and sol01.tex. Compiling each and everyone of these files will output the worksheet, meta, and solutions respectively. The body.tex file is used to pick and choose which questions will go onto the worksheet.

## `questionBank/`
Inside the `questionBank/` directory, there are subfolders for each questions by topic. Inside a topic, let's say ode, there will be multiple LaTeX files such as rc_circuit.tex and mech_ode.tex. Each individual file corresponds to a single question. If you want to see what your LaTeX output looks like, the next section will explain how to do so. The reason for keeping the worksheets and the questions separate is so that the code is maintainable for future semesters. In addition, for future semesters, we can pick and choose questions that we want to reuse or to take out questions that are no longer in scope.

## `test/` and `testing/`
The sole purpose of the testing folder is to have an environment in which you can create test question.tex files and compile them in the `test` folder. For the purposes of the repository, please do not add/commit/or push your changes in this folder or the `test` folder. The `test` folder is an identical environment as the other numbered folders. You can pick and choose which questions to compile using the appropriate commands. It will make more sense on how to test code once looking at the repository.

# Installation Requirements
    git               - https://git-scm.com/downloads
    LaTeX             - https://www.latex-project.org/get/
    make              - You can download make through XCode on Mac, or through cygwin / cmake on Windows.

# Compiling Instructions

You can use pdflatex to compile the ws.tex, meta.tex, sol.tex, or test.tex files, or you can choose to just use the Makefiles. 

The current Makefile commands are:

 1. make ws: This makes the vanilla worksheet that the students will see.
 2. make sol: This will make the solutions for students to see after section.
 3. make meta: This will create the weekly metas that contain solutions along with step by step guides and teaching tips.
 4. make test: This will compile your test file in the testing directory.
 5. make all: This will make the worksheet, solutions, and meta, and create a final build folder with all three files inside. 
 6. make clean: This will remove any log/out files, and pdfs that were generated.
 7. make cleanpdfs: This will just remove the pdfs that were generated.

You can run these commands to compile your LaTeX files in an easier fashion. Remember to always run `make clean` before pushing anything to git.

# Short Guide to Git

## 1. Clone the Respository

    git clone https://Username@github.com/csmberkeley/csm-16b.git

## 2. Branch off master
After cloning the repository and setting up LaTeX, pull in any updates from Github origin.

    git checkout master
    git pull origin master

Then, create a new branch off master and give it a descriptive name.

    git checkout -b taejin/rlc_circuits

## 3. Making changes

Make changes as you would normally and commit them incrementally. Write descriptive commit messages and break larger changes into smaller parts.

Start in the `fa19` directory and edit the content in `questionBank`. Note that the repository has split up worksheets from their questions: all questions are stored in `questionBank` under topics for version control and maintainability.

After making a few changes, verify that the changes appear as expected by re-making the handouts. The handouts build to the published directory.

    make all

Once you've made some changes, add them to the staging area using `git add`

    git add file.tex or git add folder/
    
You can also add everything, but be careful you don't add binaries. You can configure these in `.gitignore`
    
    git add .
    
If you added something, but made a mistake, you can always remove it.

    git rm file.tex

Using patch mode is recommended when staging changes to ensure only that only the desired diffs are included in the commit.

    git add -p 

Once satisfied, you can commit your changes and give it a descriptive but short message.

    git commit -m "Finished RLC Circuit question"

clean and push the branch to Github origin.

    make clean
    git push origin taejin

## 4. Pull request
To integrate your changes into the codebase, come back to this online repo and create a new pull request for the branch. Then assign the current maintainers for review, apply relevant labels, and set the milestone to the current release target.
To avoid merge conflicts, it is important to keep in-sync with team members if you are working on the same piece of code.

