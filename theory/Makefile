# make: собрать конспект; результат копируется в ../rvachev-theory-of-r-functions.pdf
main.pdf: *.tex
	pdflatex -interaction=nonstopmode -halt-on-error main.tex
	pdflatex -interaction=nonstopmode -halt-on-error main.tex
	cp main.pdf ../rvachev-theory-of-r-functions.pdf

clean:
	rm -f *.aux *.log *.out *.toc main.pdf
