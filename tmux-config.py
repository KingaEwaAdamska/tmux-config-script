
#!/usr/bin/env python3
import os

TMUX_CONFIG = os.path.expanduser("~/.tmux.conf")

plugins = "# List of plugins"
binding = "\n# Control settings"
theme = "\n# Catppuccin settings"
run = "\n# Run commands"

def configureCatppuccin(plugins, theme, run):
    print("\n🎨 Catppuccin theme configuration")
    catppuccin = input("› Install Catppuccin? (y/n): ").lower()
    if catppuccin == 'n':
        return plugins, theme, run

    plugins += "\nset -g @plugin 'catppuccin/tmux#v2.1.3'"
    run += "\nrun ~/.config/tmux/plugins/catppuccin/tmux/catppuccin.tmux"

    print("\nChoose Catppuccin flavor:")
    print(" 1 - 🌻 Latte")
    print(" 2 - 🪴 Frappe")
    print(" 3 - 🌺 Macchiato")
    print(" 4 - 🌿 Mocha (default)")
    flavor = input("› Your choice: ")
    theme += "\nset -g @catppuccin_flavor "
    match flavor:
        case "1":
            theme += "'latte'"
        case "2":
            theme += "'frappe'"
        case "3":
            theme += "'macchiato'"
        case _:
            theme += "'mocha'"

    print("\nWindow status style:")
    print(" 1 - basic (default)")
    print(" 2 - rounded")
    print(" 3 - slanted")
    print(" 4 - none")
    window_status_style = input("› Your choice: ")
    theme += "\nset -g @catppuccin_window_status_style "
    match window_status_style:
        case "2":
            theme += '"rounded"'
        case "3":
            theme += '"slanted"'
        case "4":
            theme += '"none"'
        case _:
            theme += '"basic"'

    theme += "\nset -g status-right-length 100"
    theme += "\nset -g status-left-length 100"
    theme += '\nset -g status-left ""'
    theme += '\nset -g status-right "#{E:@catppuccin_status_application}"'
    theme += '\nset -agF status-right "#{E:@catppuccin_status_cpu}"'
    theme += '\nset -ag status-right "#{E:@catppuccin_status_session}"'
    theme += '\nset -ag status-right "#{E:@catppuccin_status_uptime}"'
    theme += '\nset -g @catppuccin_window_text "#W"'
    theme += '\nset -g @catppuccin_window_default_text "#W"'
    theme += '\nset -g @catppuccin_window_current_text "#W"'
    return plugins, theme, run


print("🌀 tmux configuration setup\n")

if os.path.exists(TMUX_CONFIG):
    if_overwrite = input("⚠️  Config file already exists. Overwrite? (y/n): ").lower()
    if if_overwrite == 'n':
        print("\n❌ Ending script...")
        exit(0)
    os.remove(TMUX_CONFIG)
    print("🗑️  Old config removed.")

with open(TMUX_CONFIG, 'w') as f:
    pass

mouse = input("\n🖱️  Enable mouse support? (y/n): ").lower()
if mouse == 'y':
    binding += "\nset -g mouse on"

print("\n⌨️  Choose keyboard shortcuts style:")
print(" 1 - emacs (default)")
print(" 2 - vi")
shortcuts = input("› Your choice: ") or "1"
if shortcuts == "2":
    binding += "\nbind h select-pane -L"
    binding += "\nbind j select-pane -D"
    binding += "\nbind k select-pane -U"
    binding += "\nbind l select-pane -R"
    y_copy = input("› Use 'y' in copy mode to copy to clipboard? (y/n): ").lower()
    if y_copy == 'y':
        binding += '\nbind-key -T copy-mode-vi y send-keys -X copy-pipe-and-cancel "xclip -selection clipboard -in"'

print("\n📦 Plugins installation")
tpm = input("› Install tpm (plugin manager)? (y/n): ").lower()
if tpm == 'y':
    plugins += "\nset -g @plugin 'tmux-plugins/tpm'"
    run += "\nrun '~/.tmux/plugins/tpm/tpm'"

sensible = input("› Install sensible? (y/n): ").lower()
if sensible == 'y':
    plugins += "\nset -g @plugin 'tmux-plugins/tmux-sensible'"

continuum = input("› Install continuum? (y/n): ").lower()
if continuum == 'y':
    plugins += "\nset -g @plugin 'tmux-plugins/tmux-continuum'"

resurrect = input("› Install resurrect? (y/n): ").lower()
if resurrect == 'y':
    plugins += "\nset -g @plugin 'tmux-plugins/tmux-resurrect'"

plugins, theme, run = configureCatppuccin(plugins, theme, run)

file_content = plugins + binding + theme + run
with open(TMUX_CONFIG, 'a') as f:
    f.write(file_content)

print("\n✅ Configuration written to", TMUX_CONFIG)
print("💡 Start tmux and press prefix + I to install plugins.")

