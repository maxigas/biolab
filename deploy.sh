#!/bin/bash

git add *
git commit -m deploy.sh
git push
ssh biolab@biolab git pull
echo READY
