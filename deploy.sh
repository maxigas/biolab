#!/bin/bash

source Makefile
$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
git add *
git commit -m deploy.sh
git push
ssh biolab@biolab git pull
echo READY
