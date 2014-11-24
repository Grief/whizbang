#!/usr/bin/python


def esc(fg=None, bg=None, bold=False, italic=False, underline=False, blink=False, reverse=False, code=False, escape=None, message=None):
    seq = []
    if bold          : seq.append('1')
    if italic        : seq.append('3')
    if underline     : seq.append('4')
    if blink         : seq.append('5')
    if reverse       : seq.append('7')
    if fg is not None: seq.append('38;2;%s;%s;%s' % fg if len(fg) == 3 else '38;%s' % fg)
    if bg is not None: seq.append('48;2;%s;%s;%s' % bg if len(bg) == 3 else '48;%s' % bg)
    value = ';'.join(seq)
    if code: return value
    if escape == 'tmux': value = '\033Ptmux;\033\033[{0}m\033\\'.format(value)
    else: value = '\033[{0}m'.format(value)
    if message is not None: value = ''.join((value, message, esc()))
    return value

def log(color, message, *names):
    print esc(fg=c[color], message=message.format(*[name.join((esc(fg=c['name']), esc(fg=c[color]))) for name in names]))

c = {'name': ( 42, 161, 152),
     'info': (133, 153,   0),
     'pass': (181, 137,   0),
     'warn': (203,  75,  22)}
