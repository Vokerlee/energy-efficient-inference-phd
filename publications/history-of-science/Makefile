.PHONY: all clean

all:
	latexmk -xelatex -no-shell-escape \
		-interaction=nonstopmode -halt-on-error -file-line-error -outdir=build report.tex
	cp build/report.pdf ../history-of-science.pdf

clean:
	latexmk -C -outdir=build report.tex
	$(RM) ../history-of-science.pdf
