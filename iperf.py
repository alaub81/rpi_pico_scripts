# install homebrew mac os
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/andreas/.zprofile
# eval "$(/opt/homebrew/bin/brew shellenv)"

# install iperf
# brew install iperf3

import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('CNX_Software_Xiaomi', 'The Password')
import upip
upip.install("uiperf3")
import uiperf3
uiperf3.client('192.168.31.48')