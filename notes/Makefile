SOURCES := $(wildcard *.tex)
PDFS := $(SOURCES:.tex=.pdf)

.PHONY: all clean

all: $(PDFS)

%.pdf: %.tex Makefile
	latexmk -pdf -pdflatex='pdflatex %O %S' -no-shell-escape \
		-interaction=nonstopmode -halt-on-error -file-line-error -outdir=build $<
	cp build/$@ $@

clean:
	latexmk -C -outdir=build $(SOURCES)
	$(RM) $(PDFS)
