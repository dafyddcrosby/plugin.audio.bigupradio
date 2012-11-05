#!/bin/python/
# Copyright 2012 Dafydd Crosby <dafydd@dafyddcrosby.com>
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
# POSSIBILITY OF SUCH DAMAGE.

import xbmc
import xbmcgui
import xbmcplugin
import sys

STATIONS = {
    "Slamming Dancehall": 8000,
    "Roots Reggae": 8005,
    "Massive Dub": 8013,
    "Ska Radio": 8017,
    "Strictly for Lovers Rock": 8021,
    "Sweet Soca": 8025,
    "Toma Reggaeton": 8029,
}

def main():
    for station, port in STATIONS.iteritems():
        lst = xbmcgui.ListItem(station)
        url = "http://radio.bigupradio.com:%i" % port
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=lst)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

main()
