#!/bin/bash

echo "Start ssh proxy to threefcata.com ..."
ssh -D 7070 -p 2222 stevenfrog@threefcata.com 
