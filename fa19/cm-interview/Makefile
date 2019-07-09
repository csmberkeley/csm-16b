tex = pdflatex
ink = inkscape

alltex = $(wildcard *.tex)
probin = $(wildcard prob*.tex)
prob = $(probin:.tex=.pdf)
solin = $(wildcard sol*.tex)
sol = $(solin:.tex=.pdf)
wsin = $(wildcard tech.tex)
wspdf = $(wsin:.tex=.pdf)
ws = $(wsin:.tex=)
metain = $(wildcard meta*.tex)
meta = $(metain:.tex=)
testin = $(wildcard test.tex)
test = $(testin:.tex=.pdf)

imagein = $(wildcard figures/*.svg)
image = $(imagein:.svg=.png)
latexmaintex = $(wildcard latexmain*.tex)
latexmainpdf = $(latexmaintex:.tex=.pdf)

all: $(image) $(alltex) ws sol meta

%.png : %.svg
	(type $(ink) && ($(ink) --export-png=$@ --export-dpi=400 $<)) || echo 'Not compiling png'

prob%.pdf : prob%.tex $(alltex) $(image)
	$(tex) $<
	$(tex) $<
	$(RM) prob$*.log prob$*.aux prob$*.out prob$*.annotations

sol : $(solin) $(alltex) $(image)
	$(tex) $<
	$(RM) sol*.log sol*.aux sol*.out sol*.annotations
	mkdir -p build
	mv $(sol) build

ws : $(wsin) $(alltex) $(image)
	$(tex) $<
	$(RM) tech.log tech.aux tech.out tech.annotations

meta : $(metain) $(alltex) $(image)
	$(tex) $<
	$(RM) $(meta).log $(meta).aux $(meta).out $(meta).annotations
	mkdir -p build
	mv meta.pdf $(ws)-meta.pdf
	mv $(ws)-meta.pdf build

test : $(testin) $(alltex) $(image)
	$(tex) $<
	$(RM) $(test).log $(test).aux $(test).out $(test).annotations

clean:
	- $(RM) *.dvi *.log *.out *.aux *.annotations *.fdb_latexmk *.fls *.synctex.gz 
	- (cd ..; $(RM) *.dvi *.log *.out *.aux *.annotations *.fdb_latexmk *.fls *.synctex.gz)

cleanpdfs:
	$(RM) -r $(prob) $(sol) $(ws) $(meta) $(latexmainpdf) build
