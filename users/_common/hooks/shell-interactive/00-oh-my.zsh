ZSH="$WHIZBANG/modules/oh-my-zsh"
if [ ! -e "$ZSH" ]; then
    echo 'Would you like to download and install oh-my-zsh [ http://ohmyz.sh/ ]? (yes/no)'
    while true; do
        read answer
        case "$answer" in
            "no") break ;;
            "yes")
                git clone git://github.com/robbyrussell/oh-my-zsh.git "$ZSH"
                themes="$ZSH/custom/themes"
                mkdir "$themes"
                ln -s "$WHIZBANG/conf/oh-my.zsh-theme" "$themes"
                break
                ;;
            *) echo 'Please type only "yes" or "no"'
        esac
    done
fi

export ZSH
ZSH_THEME="oh-my"
plugins=(git git-prompt mvn zsh-syntax-highlighting)

. "$ZSH/oh-my-zsh.sh"
