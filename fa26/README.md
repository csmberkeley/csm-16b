# EE 64 worksheets (Fall 2026)

Each numbered folder (`01/`, `02/`, ...) is one worksheet. Its `body.tex` picks
questions from `questionBank/`; everything else is shared from this folder.

## Make a new worksheet

From this folder (`fa26/`):

```
make new N=04              # blank worksheet in 04/
make new N=04 FROM=03      # start from a copy of 03's questions + figures
```

Then edit `04/body.tex` — add one line per question, with `\newpage` between them:

```latex
\begin{qunlist}
\input{\bank/resistor/q_voltage_divider.tex}
\newpage
\input{\bank/resistor/q_supernode.tex}
\end{qunlist}
```

`make new` is safe to re-run: it never overwrites an existing `body.tex`, so it
also fixes a folder you created by hand that's missing its `Makefile`.

## Build

```
cd 04
make            # ws04.pdf, sol04.pdf, meta04.pdf  (copies also go in build/)
make ws         # just the worksheet   (also: make sol, make meta)
make clean      # delete generated files
```

`make all` from `fa26/` builds every worksheet.

## When it fails

`make` prints the first error and the line it happened on, e.g.

```
*** LaTeX error while building ws04.pdf
    error: ! LaTeX Error: File `../../questionBank/resistor/q_nope.tex' not found.
    at line 19 \input{\bank/resistor/q_nope.tex}
```

Common causes:

- **File not found** — typo in an `\input` path. Check the file exists under `questionBank/`.
- **Undefined control sequence** — a typo'd command, or `\itemFoo` with no space after `\item`.
- **Error only in `sol`/`meta`, not `ws`** — the problem is inside an `\ans{...}` / `\sol{...}` /
  `\meta{...}` block, since those only print in the solutions/meta versions.

The full log is left in the worksheet folder (e.g. `04/ws04.log`) when a build fails.

## Setup

You need `make` and a LaTeX install with `pdflatex`.

- **Mac:** `xcode-select --install` (make) and [MacTeX](https://tug.org/mactex/).
- **Linux:** `make` and TeX Live from your package manager (`texlive-full` is simplest).
- **Windows:** [TeX Live](https://tug.org/texlive/) or MiKTeX, plus make
  (`winget install ezwinports.make`). Run the commands from **Git Bash**, which
  provides the Unix tools the Makefiles use. If your make is called
  `mingw32-make`, use that in place of `make`.
