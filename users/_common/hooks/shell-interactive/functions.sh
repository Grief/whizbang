search() { eval "find . -type f -exec grep -isHn --color=always \"$@\" {} \;" }

numerate-tracks(){ls *.mp3 -1rt|awk '{printf("\"%s\" \"%02d - %s\"\n",$0,NR,$0)}'|xargs -L1 mv -v}