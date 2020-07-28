alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias l='ls -CF'
alias la='ls -A'
alias ll='ls -alFh'
alias less='less -R'
alias c='clear'
alias cd..='cd ..'
alias clr='clear'
alias ..='cd ..'
alias lsa='ls -a'
alias rm='rm -i'
alias v='vim'
alias python='python3'
alias pip='pip3'
alias top='top -o CPU -O MEM'
alias g++='g++ -std=c++11'
alias cat="highlight -O ansi --force"
alias catb="highlight -O ansi --syntax=bash"
alias activate='source ./ENV/bin/activate'

#git
alias add='git add -A'
alias commit='git commit -m'
alias push='git push'
alias pull='git pull'
alias checkout='git checkout'
alias status='git status'
alias logs='git log --oneline --graph --stat'
alias log='git log --oneline --graph --shortstat'
alias fetch='git fetch'

# man colors
export LESS_TERMCAP_mb=$'\e[1;32m'
export LESS_TERMCAP_md=$'\e[1;32m'
export LESS_TERMCAP_me=$'\e[0m'
export LESS_TERMCAP_se=$'\e[0m'
export LESS_TERMCAP_so=$'\e[01;33m'
export LESS_TERMCAP_ue=$'\e[0m'
export LESS_TERMCAP_us=$'\e[1;4;31m'

#Top
function topgrep() {
    if [[ $# -ne 1 ]]; then 
        echo "Usage: topgrep <expression>"
    else 
        top -pid `pgrep $1`
    fi
}
