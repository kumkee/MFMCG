pdf:
	pdflatex hamiltonian-all.tex
	rm -f hamiltonian-all.{aux,log}

profile:
	python -m cProfile -s time profmf.py > profmf.log

all:
	pdf
