.PHONY: all clean

all:
	latexmk -pdf -pdflatex='pdflatex %O %S' -no-shell-escape \
		-interaction=nonstopmode -halt-on-error -file-line-error -outdir=build article.tex
	cp build/article.pdf ../gemm-simulator-accuracy.pdf

clean:
	latexmk -C -outdir=build article.tex
	$(RM) ../gemm-simulator-accuracy.pdf
