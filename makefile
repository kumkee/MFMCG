profmflog=profiles/profmf.log
profmfpy=profmf.py
profmetrpl=profiles/profmetrp.log
profmetrpp=profmetrp.py

#- MKL ---------------
MKLROOT=/opt/intel/mkl/10.2.5.035
#MKLROOT=/opt/intel/mkl/10.2.2.025
MKLINC=$(MKLROOT)/include/em64t/lp64
MPIINC=/opt/mvapich2/include/
MKLLIB=$(MKLROOT)/lib/em64t

LIBRARIES=-L$(MKLLIB)
INCLUDE=-I$(MKLINC)
LIBS=-lmkl_blas95 -lmkl_lapack95_lp64 -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core -liomp5 -lpthread
#-Wl,--start-group $(MKLLIB)/libmkl_lapack95_lp64.a -Wl,--end-group

pdf:
	pdflatex hamiltonian-all.tex
	rm -f hamiltonian-all.{aux,log}

saveprofile:
	mv $(profmflog).1 $(profmflog).2
	mv $(profmflog) $(profmflog).1

profile:
	python -m cProfile -s cum $(profmfpy) > $(profmflog)


saveprofilemtp:
	mv $(profmetrpl).1 $(profmetrpl).2
	mv $(profmetrpl) $(profmetrpl).1

profilemtp:
	qsub profile.pbs

all:
	pdf

omp:
	f2py -c -m flapack flapack.f95 -lgomp --f90flags="$(LIBRARIES) $(INCLUDE) $(LIBS)" --fcompiler=intelem

f95:
	gfortran -c $(LIBRARIES) $(INCLUDE) $(LIBS) flapack.f95
