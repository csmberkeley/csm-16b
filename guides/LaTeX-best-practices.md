# Guidelines for LaTeX Documents
---

A set of conventions for avoiding conflicting definitions by different people, keeping the document structure easy to use and maintainable (ie, avoiding bitrot), giving documents a more uniform look, easing merge conflict resolution, and making typing in LaTeX more convenient.

0. **USE pdflatex TO COMPILE BEFORE COMMIT**: Those of you who use sublime, latexmk or other high level convenient latex wrappers: make sure you **run pdflatex to compile latex documents before committing**. These higher level wrappers forgive many errors, which pdflatex will catch.
  Note: You can use make (if supported by your OS/installation -- linux and OSX do support, Windows might not) to run pdflatex on prob, sol, ans, etc.. "make clean" will clean the directory of latex temporaries. "make cleanpdfs" will remove prob/sol/ans etc pdfs. You should run "make clean cleanpdfs" before running make if you want it to re-run pdflatex even if you have not changed anything. Recommend learn about makefiles and the make system - there is plenty of info on Google.  
  If you make changes to any files that are included in many documents (like `newcommands*.tex`, `ee16.sty`, `course-notes/notes.tex`, `hws/prob.tex`, etc. -- also see below) please **check that every existing document still compiles without errors**. Best to make such changes in a separate branch (not master) and ask others to test the branch before merging back to master. Shell scripts like the following (which work on linux and should work on OSX; might work on Windows if you have its recent linux subsystem, or cygwin, installed) can be helpful for testing that everything still compiles:

        cd hws; for i in {0,1,2,3,4}; do echo $i; (cd $i; make clean cleanpdfs; make 1>/dev/null; make clean cleanpdfs); done
        cd discussion; for i in {0,1,2}{A,B} {3,4}A; do echo $i; (cd $i; make clean cleanpdfs; make 1>/dev/null; make clean cleanpdfs); done

    The above should finish without errors. If anything hangs or does not complete, there's a problem.
    
0. **DO NOT COPY AND MODIFY ee16.sty**: There should be only **ONE** [`ee16.sty`](./ee16.sty), pulled in by every Spring 2019 EE16B document. Please do not make copies -- this will lead very quickly to a proliferation of many inconsistent versions.

2. **Definitions and newcommands**: Please do not put definitions and newcommands anywhere except in the `newcommand*.tex` files in the `sp19/` directory.  
  Currently, the following `newcommand*.tex` files are there.<sup>1</sup> Please put any of your own newcommands in the appropriate one, and also make it  a point to read through them every now and then and make use of the pre-defined newcommands there:
   - [`newcommands-eg-ie-etc.tex`](./newcommands-eg-ie-etc.tex): defines `\ie`, `\etc`, and so on.
   - [`newcommands-labels-refs.tex`](./newcommands-labels-refs.tex): defines `\eqnlabel`, `\eqnref`, and so on.
   - [`newcommands-math.tex`](./newcommands-math.tex): defines many mathematical newcomands, such as `\ddt`, `\be`/`\ee` (begin and end equation), and so on.

   Note that for legacy reasons, there are some defs/newcommands in `ee16b.sty`. These will be moved out and better organized as we go along. Please do not add more defs/newcommands in `ee16b.sty`.

1. **ONE SENTENCE PER LINE rule**: Please type exactly one sentence per line - don't break a sentence over multiple lines, or put multiple sentences in a line. This simple convention helps greatly with easing merge conflicts and also makes complicated diffs easier to see on the github website.  
  See [`./00-ONE-LINE-PER-SENTENCE-rule.txt`](./00-ONE-LINE-PER-SENTENCE-rule.txt) for examples.

3. **Preferred math commands**: 
   - `\widetilde` over `\tilde`(use for phasors, over capital letters)
   - `\overline` over `\bar` (for complex conjugation, logical negation)

3. **Footnotes go after punctuation**: 
   - AVOID: Go on\footnote{my footnote}, why not.
   - USE: Go on,\footnote{my footnote} why not.

<sup>1</sup>: If it seems really necessary, create other such `newcommand*.tex` files, making sure to name them clearly; then include them in `hws/prob.tex`,`hws/sol.tex`, `discussion/dis.tex`, `discussion/ans.tex`, `discussion/sol.tex`, etc..
