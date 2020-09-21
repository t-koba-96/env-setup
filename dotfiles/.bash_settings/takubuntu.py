
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
alias server='open http://25.33.181.66:3000/'
alias chrome='open -a google\ chrome'
alias vscode='open -n -b "com.microsoft.VSCode"'

# server lab 
alias hinton='open http://25.33.181.66:58812/lab'
alias lecun='open http://25.44.197.105:58812/lab'
alias dl='open http://25.71.247.26:58812/lab'
alias efros='open http://25.90.78.253:58812/lab'
alias dl2='open http://25.33.19.114:58812/lab'
alias feifei='open http://25.20.14.207:58812/lab'
alias taku='open http://25.17.129.130:8888/lab'

# myubuntu
alias demo_view='open http://127.0.0.1:8050/'
alias tboard_view='open http://127.0.0.1:6006/'

# other
alias mvim='/Applications/MacVim.app/Contents/MacOS/Vim'
alias atgp='~/Documents/atcoder/autogit.sh'
alias exA='gcc A.cpp&&./a.out'
alias exB='gcc B.cpp&&./a.out'
alias exC='gcc C.cpp&&./a.out'
alias exD='gcc D.cpp&&./a.out'

