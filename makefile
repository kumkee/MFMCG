pdf:
	pdflatex hamiltonian-all.tex
	rm -f hamiltonian-all.{aux,log}

profile:
	python -m cProfile -s time -o profmf.log profmf.py

all:
	pdf
