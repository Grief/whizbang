search() { eval "find . -type f -exec grep -isHn --color=always \"$@\" {} \;" }