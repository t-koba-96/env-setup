
# 環境構築　備忘録  

環境構築が毎回ぐちゃぐちゃになってしまうので、ここに全部まとめる。  


# pyenv + virtualenv  

とりあえずはpyenvとvirtualenvを組み合わせて環境構築してる [(参考)](https://qiita.com/Kodaira_/items/feadfef9add468e3a85b)

virtualenvで環境切るたびにpipが古いバージョンのままなので注意!  
(はじめは pip install --upgrade pip して大丈夫)  



# dotfiles  

トップディレクトリに置くドットファイルを設定する

## ssh  
.ssh~  
- [config](dotfiles/.ssh/config) : ssh接続するためのconfig  


## bash系
- [.bash_profile](dotfiles/.bash_profile) : ログイン、ssh接続した初回のみ読み込む  
  (環境変数の部分は各環境に合わせて追記する必要あり)

- [.bashrc](dotfiles/.bashrc) : その後bashを起動するたびに読み込む

- [.bash_settings](dotfiles/.bash_settings) : 環境毎に違う部分記述、主にaliases  
  (ファイル名を.bash_settingsに変えて使う)

## tmux系  
- [.tmux.conf](dotfiles/.tmux.conf) : ssh接続するためのconfig
