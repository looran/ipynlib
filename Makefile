PREFIX=/usr/local
BINDIR=$(PREFIX)/bin

all:
	@echo "Run \"sudo make install\" to install ipynlib"
	@echo "(equivalent to \"sudo python setup.py install\""

install:
	python setup.py install

