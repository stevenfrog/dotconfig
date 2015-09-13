#!/bin/sh
 
#export LD_PRELOAD=/opt/sublime_text/libsublime-imfix.so
#exec /opt/sublime_text/sublime_text "$@"

# start python3.4 first
. /home/stevenfrog/py34/bin/activate

sh -c "LD_PRELOAD='/opt/sublime_text/sublime_text_fcitx.so' '/opt/sublime_text/sublime_text' --class=sublime-text '$@'"
