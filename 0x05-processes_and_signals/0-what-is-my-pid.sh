#!/usr/bin/env bash
# a Bash script that displays its own PID.
#pgrep "$0"
name=$(echo $0 | cut -d '/' -f 2)
echo "$(pgrep -o -f "$name")"
