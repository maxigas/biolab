#!/bin/bash

git add *
git commit -m deploy.sh
git push
ssh biolab@biolab git clone git@github.com:maxigas/biolab.git
echo READY
