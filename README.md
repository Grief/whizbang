whizbang
========

Linux environment, mostly console, KDE is preferred, latest Kubuntu is even better.

###Requirements
* Bash or Zsh shell. Support of others is planned.
* Python 2.*


###Installation

<sup>*I prefer installation into the topmost directory of the filesystem named by one letter. That makes the console access to contents of whizbang the fastest possible. As I am Grief, I use `/g/` directory. You are free to choose any other location you like but all instructions would assume that you want to install whizbang into that directory.*</sup>

In the most of linux distributions you are working under unprivileged user which cannot touch files outside his or her home directory:

    sudo mkdir /g
    sudo chown $USER:`id -gn $USER` /g

The installation itself

    cd /g
    git clone git@github.com:grief/whizbang.git .
    ./install

