
all: install 

install: 
	if test ! -d ~/bin ; then mkdir ~/bin ; fi
	ln -s $(PWD)/EVi.py ~/bin/EVi.py
	ln -s $(PWD)/EVi.py ~/bin/evi.py

clean:
	rm *.pyc

uninstall: 
	rm ~/bin/EVi.py
	rm ~/bin/evi.py

refresh: uninstall install

