.PHONY: validate paper clean

validate:
	python validation/fbdg_structured_validate.py

paper:
	pandoc paper/fbdg.md --citeproc --bibliography=paper/references.bib --standalone -o paper/fbdg.tex
	pandoc paper/fbdg.md --citeproc --bibliography=paper/references.bib --standalone -o paper/fbdg.docx
	pandoc paper/fbdg.md --citeproc --bibliography=paper/references.bib --pdf-engine=xelatex -V geometry:margin=1in -V fontsize=10pt -o paper/fbdg.pdf

clean:
	rm -f paper/*.aux paper/*.log paper/*.out paper/*.toc
