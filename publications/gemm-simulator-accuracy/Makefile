.PHONY: all clean docx-setup docx docx-check docx-preview

DOCX_PYTHON := ../.tools/python/bin/python
export PUBLICATION_SOURCE := $(CURDIR)

all:
	latexmk -pdf -pdflatex='pdflatex %O %S' -no-shell-escape \
		-interaction=nonstopmode -halt-on-error -file-line-error -outdir=build article.tex
	cp build/article.pdf ../gemm-simulator-accuracy.pdf

docx-setup:
	python3 ../scripts/setup_docx.py

docx: all
	$(DOCX_PYTHON) ../scripts/export_docx.py

docx-check:
	$(DOCX_PYTHON) ../scripts/check_docx.py ../gemm-simulator-accuracy.docx

docx-preview: all
	$(DOCX_PYTHON) ../scripts/export_docx.py --preview

clean:
	latexmk -C -outdir=build article.tex
	$(RM) ../gemm-simulator-accuracy.pdf
	$(RM) ../gemm-simulator-accuracy.docx ../gemm-simulator-accuracy-docx-preview.pdf
	$(RM) -r build/docx
