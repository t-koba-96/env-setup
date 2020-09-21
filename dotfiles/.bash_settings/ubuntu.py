
#----------aliases----------

alias ll='ls -lG'
alias la='ls -laG'

# cd shortcut
cd() { builtin cd "$@"; ll; }
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'

# vim shortcuts
alias bs='vim ~/.bash_settings'
alias br='vim ~/.bashrc'
alias bp='vim ~/.bash_profile'
alias tc='vim ~/.tmux.conf'
alias sbs='source ~/.bash_settings'
alias sbr='source ~/.bashrc'
alias sbp='source ~/.bash_profile'
alias stc='source ~/.tmux.conf'

# random shortcuts
alias python='python3'

# other
alias mvim='/Applications/MacVim.app/Contents/MacOS/Vim'
alias atgp='~/Documents/atcoder/autogit.sh'
alias exA='gcc A.cpp&&./a.out'
alias exB='gcc B.cpp&&./a.out'
alias exC='gcc C.cpp&&./a.out'
alias exD='gcc D.cpp&&./a.out'