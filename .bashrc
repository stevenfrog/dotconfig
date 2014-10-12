# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
[ -z "$PS1" ] && return

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=5000
HISTFILESIZE=5000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "$debian_chroot" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

export TERM=xterm-256color

PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\[\033[01;33m\]\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '


# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi


# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

#
# ~/.bashrc
#

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias ll='ls -l --time-style=long-iso'
alias lr='ls -R'                    # recursive ls
alias la='ll -A'
alias lx='ll -BX'                   # sort by extension
alias lz='ll -rS'                   # sort by size
alias lt='ll -rt'                   # sort by date
alias lm='la | more'
alias grep='grep --color=auto'

#export LESS=-R
#export LESS_TERMCAP_me=$(printf '\e[0m')
#export LESS_TERMCAP_se=$(printf '\e[0m')
#export LESS_TERMCAP_ue=$(printf '\e[0m')
#export LESS_TERMCAP_mb=$(printf '\e[1;32m')
#export LESS_TERMCAP_md=$(printf '\e[1;34m')
#export LESS_TERMCAP_us=$(printf '\e[1;32m')
#export LESS_TERMCAP_so=$(printf '\e[1;44;1m')

# safety features
alias cp='cp -iv'
alias mv='mv -i'
alias rm='rm -i'                    # 'rm -i' prompts for every file
alias ln='ln -i'
alias chown='chown --preserve-root'
alias chmod='chmod --preserve-root'
alias chgrp='chgrp --preserve-root'
alias sudo='sudo '                  # make sure we can use alias in sudo

# Editor
export EDITOR=vim
export SVN_EDITOR=vim


# Add path for local home's bin dir
# add local heroku bin
# export PATH=$PATH:/sbin/:$HOME/bin

# Add color for man
man() {
    env \
        LESS_TERMCAP_mb=$(printf "\e[1;31m") \
        LESS_TERMCAP_md=$(printf "\e[1;31m") \
        LESS_TERMCAP_me=$(printf "\e[0m") \
        LESS_TERMCAP_se=$(printf "\e[0m") \
        LESS_TERMCAP_so=$(printf "\e[1;44;33m") \
        LESS_TERMCAP_ue=$(printf "\e[0m") \
        LESS_TERMCAP_us=$(printf "\e[1;32m") \
            man "$@"
    }

# Add Env for Topcoder
export TC_VM_IP=54.82.108.209
export MAVEN_OPTS="-Xms256m -Xmx1024m -XX:PermSize=128m -XX:MaxPermSize=256m"

# Add colors for bash
LS_COLORS='rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=00;91:*.tgz=00;91:*.arj=00;91:*.taz=00;91:*.lzh=00;91:*.lzma=00;91:*.tlz=00;91:*.txz=00;91:*.zip=00;91:*.z=00;91:*.Z=00;91:*.dz=00;91:*.gz=00;91:*.lz=00;91:*.xz=00;91:*.bz2=00;91:*.bz=00;91:*.tbz=00;91:*.tbz2=00;91:*.tz=00;91:*.deb=00;91:*.rpm=00;91:*.jar=00;91:*.war=00;91:*.ear=00;91:*.sar=00;91:*.rar=00;91:*.ace=00;91:*.zoo=00;91:*.cpio=00;91:*.7z=00;91:*.rz=00;91:*.jpg=01;35:*.JPG=01;35:*.jpeg=01;35:*.JPEG=01;35:*.gif=01;35:*.bmp=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.mkv=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.aac=00;35:*.au=00;35:*.flac=00;35:*.mid=00;35:*.midi=00;35:*.mka=00;35:*.mp3=00;35:*.mpc=00;35:*.ogg=00;35:*.ra=00;35:*.wav=00;35:*.m4a=00;35:*.pdf=00;96:*.doc=00;96:*.xls=00;96:*.docx=00;96:*.xlsx=00;96:*.ppt=00;96:*.csv=00;96:*.odt=00;96:*.ods=00;96:*.chm=00;96:*.epub=00;96:*.mobi=00;96:*.azw3=00;96:*.txt=00;96:*.properties=00;96:'
export LS_COLORS


tmux_init()
{
    tmux new-session -s "frog" -d -n "other"    # 开启一个会话
    tmux new-window -n "main"           # 开启一个窗口
    tmux split-window -h                # 开启一个竖屏
    tmux split-window -v                # 开启一个横屏,并执行top命令
    tmux select-pane -L
    tmux resize-pane -R 10
    tmux -2 attach-session -d           # tmux -2强制启用256color，连接已开启的tmux
}

# 判断是否已有开启的tmux会话，没有则开启
if which tmux 2>&1 >/dev/null; then
    test -z "$TMUX" && (tmux attach || tmux_init)
fi

# reload nvidia config
nvidia-settings -l

