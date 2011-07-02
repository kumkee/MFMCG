pdf:
	pdflatex hamiltonian-all.tex
	rm -f hamiltonian-all.{aux,log}

all:
	pdf
