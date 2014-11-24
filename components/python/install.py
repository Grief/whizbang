#!/usr/bin/python
import os, shutil
from color import log

def symlink(link, target, backup=None):
    if os.path.islink(link) and os.readlink(link) == target:
        log('pass', '{} is already installed', link)
        return
    if os.path.exists(link):
        if backup is not None: shutil.copy(link, backup)
        os.remove(link)
    os.symlink(target, link)
    log('info', '{} has been installed', link)

def ini_config(name, changes, backup):
    log('info', '\nChanging ini configuration in {}', name)
    if not os.path.exists(name): log('warn', 'File {} does not exist', name)  #TODO: create parent dirs
    else:
        orig = name + '-original'
        os.rename(name, orig)
        with open(name, 'w') as ini:
            section = None
            if None not in changes: changes[None] = {}
            for line in open(orig):
                line = line[:-1]
                skip = False
                if line in changes: section = line
                else:
                    for param, value in changes[section].iteritems():
                        if line.startswith(param):  # vvv TODO more careful (strip middle and compare to '=')
                            if line == param + '=' + value: log('pass', '{} is already set to {} in {} section', param, value, section)
                            else:
                                ini.write((''.join((param, '=', value, '\n'))))
                                skip = True
                                log('info', '{} was set to {} in {} section (previously {})', param, value, section, line[len(param) + 1:])
                            del changes[section][param]
                            break
                if not skip: ini.write(line + '\n')
        if backup is None: os.remove(orig)
        else:
            backup = os.path.sep.join((backup, os.path.basename(name)))
            if os.path.exists(backup): os.remove(backup)
            shutil.move(orig, backup)
    with open(name, 'a') as ini:
        for section, params in changes.iteritems():
            if len(params) == 0: continue
            ini.write('\n')
            ini.write(''.join((section, '\n')))
            for param, value in params.iteritems():
                ini.write(''.join((param, '=', value, '\n')))


    # if not found:
    #     log('warn', 'section {} not found in {}', section, ini)
