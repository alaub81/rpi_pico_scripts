# -*- coding: utf-8 -*-
# first you need to install uping (enable wifi first):
# import upip
# upip.install('uping')

# ping Target
target = "google.de"

import uping
uping.ping(target)