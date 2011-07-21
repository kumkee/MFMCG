profmflog=profiles/profmf.log
profmfpy=profmf.py
profmetrpl=profiles/profmetrp.log
profmetrpp=profmetrp.py


pdf:
	pdflatex hamiltonian-all.tex
	rm -f hamiltonian-all.{aux,log}

saveprofile:
	mv $(profmflog).1 $(profmflog).2
	mv $(profmflog) $(profmflog).1

profile:
	python -m cProfile -s time $(profmfpy) > $(profmflog)


saveprofilemtp:
	mv $(profmetrpl).1 $(profmetrpl).2
	mv $(profmetrpl) $(profmetrpl).1

profilemtp:
	qsub profile.pbs

all:
	pdf
