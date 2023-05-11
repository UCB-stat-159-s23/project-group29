.ONESHELL:
SHELL = /bin/bash

.PHONY : all
all : env html clean

.PHONY : env 
env :
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml 
	conda activate project
	conda install ipykernel
	python -m ipykernel install --user --name project --display-name "IPython - project"

.PHONY : html 
html: 
	jupyter-book build . 

.PHONY : clean
clean: 
	rm -f games/*.csv
	rm -f games_model/*.csv
	rm -rf _build/html/

.PHONY : help
## help: prints documentation
help : Makefile
	@sed -n '/^##/p' $<