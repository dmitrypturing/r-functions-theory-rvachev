# make: собрать конспект -> ../rvachev-theory-of-r-functions.pdf
PDF = ../rvachev-theory-of-r-functions.pdf

$(PDF): *.tex
	pdflatex -interaction=nonstopmode -halt-on-error main.tex
	pdflatex -interaction=nonstopmode -halt-on-error main.tex
	cp main.pdf $(PDF)

clean:
	rm -f *.aux *.log *.out *.toc main.pdf
