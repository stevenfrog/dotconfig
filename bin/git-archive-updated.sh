#!/bin/bash
#

git archive -o ../updated.zip HEAD $(git diff --name-only $1)
