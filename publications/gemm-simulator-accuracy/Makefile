.PHONY: all clean docx-setup docx docx-check docx-preview

all:
	latexmk -pdf -pdflatex='pdflatex %O %S' -no-shell-escape \
		-interaction=nonstopmode -halt-on-error -file-line-error -outdir=build article.tex
	cp build/article.pdf ../gemm-simulator-accuracy.pdf

docx-setup:
	python3 scripts/setup_docx.py

docx: all
	python3 scripts/export_docx.py

docx-check:
	python3 scripts/check_docx.py ../gemm-simulator-accuracy.docx

docx-preview: all
	python3 scripts/export_docx.py --preview

clean:
	latexmk -C -outdir=build article.tex
	$(RM) ../gemm-simulator-accuracy.pdf
	$(RM) ../gemm-simulator-accuracy.docx ../gemm-simulator-accuracy-docx-preview.pdf
	$(RM) -r build/docx
