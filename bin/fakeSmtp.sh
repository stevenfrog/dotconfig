#!/bin/sh

echo "Starting a python SMTP server!!!"
python -m smtpd -n -c DebuggingServer localhost:5025
