#!/bin/bash
echo $1 > commit.msg
make git_upload
