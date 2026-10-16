# make: собрать решения упражнений -> ../rvachev-exercises.pdf
PDF = ../rvachev-exercises.pdf

$(PDF): *.tex ../theory/macros.tex
	pdflatex -interaction=nonstopmode -halt-on-error main.tex
	pdflatex -interaction=nonstopmode -halt-on-error main.tex
	cp main.pdf $(PDF)

clean:
	rm -f *.aux *.log *.out *.toc main.pdf
