#!/bin/bash

git add *
git commit -m deploy.sh
git push
ssh biolab@biolab git clone https://github.com/maxigas/biolab.git
echo READY
