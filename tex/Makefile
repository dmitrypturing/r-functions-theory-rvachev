# Сборка: make  (нужен pdflatex с babel-russian, T2A/cm-super, tikz, tcolorbox)
main.pdf: *.tex
	pdflatex -interaction=nonstopmode -halt-on-error main.tex
	pdflatex -interaction=nonstopmode -halt-on-error main.tex
	cp main.pdf ../rvachev-ch1-pp1-29.pdf

clean:
	rm -f *.aux *.log *.out *.toc main.pdf
