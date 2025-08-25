#!/bin/bash

TMUX_CONFIG="$HOME/.tmux.conf"

read -p "Set mouse on? (y/n)" mouse
if [[ "$mouse" == "y" || "$mouse" == "Y" ]]; then
  
fi

if [ -e "~/.tmux.conf" ]; then
  read -p "Do you want to overwrite actual config?(y/n) " if_overwrite
  if [[ "$if_overwrite" == "n" || "$if_overwrite" == "N" ]]; then
    echo "Ending script..."
    exit 0
  fi
  rm "TMUX_CONFIG"
fi

touch "TMUX_CONFIG"

read -p "Choose type of keyboard shortcuts(1-emacs, 2-vi, default:1)" shortcuts
shortcuts=${shortcuts:-1}

if [[ "$shortcuts" == "2" ]]; then
  echo "set -g mode-keys vi" >> TMUX_CONFIG
  echo "set -g status-keys vi" >> TMUX_CONFIG
  read -p "Do you want to set panes switching with prefix key + h,j,k,l? (y/n)" hjkl_switching
  if [[ "$hjkl_switching" == "y" || "$hjkl_switching" =="Y" ]]; then
    echo "bind h select-pane -L" >> TMUX_CONFIG
    echo "bind j select-pane -D" >> TMUX_CONFIG
    echo "bind k select-pane -U" >> TMUX_CONFIG
    echo "bind l select-pane -R" >> TMUX_CONFIG
  fi

  read -p "Do you want to use y in copy mode to copy to clipboard? (y/n)" y_copy
  if [[ "$y_copy" == "y" || "$y_copy" == "Y" ]]; then
    echo 'bind-key -T copy-mode-vi y send-keys -X copy-pipe-and-cancel "xclip -selection clipboard -in"' >> TMUX_CONFIG

fi

read -p "Install tpm? " tpm
if [[ "$tpm" == "y" || "$tpm" == "Y" ]]; then
  echo "set -g @plugin 'tmux-plugins/tpm"
fi

