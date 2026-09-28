# Semester helper -- run these from this folder (fa26/).
#
#   make new N=04              create worksheet folder 04/ with a blank body.tex
#   make new N=04 FROM=03      same, but start from 03's body.tex and figures
#   make all                   build every worksheet folder
#   make clean                 clean every worksheet folder
#
# To build a single worksheet:  cd 04 && make

WORKSHEETS := $(sort $(patsubst %/Makefile,%,$(wildcard */Makefile)))

.PHONY: help new all clean

help:
	@echo "Run from $(notdir $(CURDIR))/:"
	@echo "  make new N=04            create worksheet folder 04/"
	@echo "  make new N=04 FROM=03    create 04/ starting from a copy of 03/"
	@echo "  make all                 build every worksheet ($(WORKSHEETS))"
	@echo "  make clean               clean every worksheet"
	@echo "Build one worksheet:  cd 04 && make"

# Safe to re-run: it only fills in what's missing and never overwrites an
# existing body.tex (so it also repairs a folder that's missing its Makefile).
new:
	@test -n "$(N)" || { echo "*** Say which number, e.g.:  make new N=04"; exit 1; }
	@test -z "$(FROM)" || test -f "$(FROM)/body.tex" || { echo "*** FROM=$(FROM): no $(FROM)/body.tex to copy"; exit 1; }
	@test -z "$(FROM)" || test ! -f "$(N)/body.tex" || { echo "*** $(N)/body.tex already exists -- not overwriting it with $(FROM)'s."; exit 1; }
	@mkdir -p "$(N)/figures"
	@printf 'include ../Makefile-common\n' > "$(N)/Makefile"
	@printf '\\input{../ws}\n'   > "$(N)/ws$(N).tex"
	@printf '\\input{../sol}\n'  > "$(N)/sol$(N).tex"
	@printf '\\input{../meta}\n' > "$(N)/meta$(N).tex"
	@if [ -f "$(N)/body.tex" ]; then \
	  echo "$(N)/ already had a body.tex -- kept it, (re)created the Makefile."; \
	else \
	  num=$$(expr "$(N)" + 0 2>/dev/null || echo "$(N)"); \
	  if [ -n "$(FROM)" ]; then \
	    src="$(FROM)/body.tex"; \
	    cp -R "$(FROM)/figures/." "$(N)/figures/" 2>/dev/null || true; \
	  else \
	    src="body-template.tex"; \
	  fi; \
	  sed '/def.title[{]/s/title[{].*[}]/title{Worksheet '"$$num"'}/' "$$src" > "$(N)/body.tex"; \
	  echo "Created $(N)/  -- edit $(N)/body.tex, then build with:  cd $(N) && make"; \
	fi

all:
	@for d in $(WORKSHEETS); do $(MAKE) --no-print-directory -C $$d all || exit 1; done

clean:
	@for d in $(WORKSHEETS); do $(MAKE) --no-print-directory -C $$d clean; done
