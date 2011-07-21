profmflog=profmf.log
profmfpy=profmf.py


pdf:
	pdflatex hamiltonian-all.tex
	rm -f hamiltonian-all.{aux,log}

saveprofile:
	mv $(profmflog).1 $(profmflog).2
	mv $(profmflog) $(profmflog).1

profile:
	python -m cProfile -s time $(profmfpy) > $(profmflog)

all:
	pdf
