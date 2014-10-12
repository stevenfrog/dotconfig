#!/bin/bash

echo 'Transfer zh_CN to UTF8'
#enca -L zh_CN -x UTF-8 $1
enconv -L zh_CN -x UTF-8 $1
