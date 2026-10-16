# make: собрать решения упражнений; результат копируется в ../rvachev-exercises.pdf
main.pdf: *.tex ../theory/macros.tex
	pdflatex -interaction=nonstopmode -halt-on-error main.tex
	pdflatex -interaction=nonstopmode -halt-on-error main.tex
	cp main.pdf ../rvachev-exercises.pdf

clean:
	rm -f *.aux *.log *.out *.toc main.pdf
