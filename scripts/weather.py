#!/usr/bin/python 

import os, sys

debug = False

os.system('curl -s "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22concord%2Cnh%22)&format=xml&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys" -o ~/.cache/temp_weather.xml')

filePath = os.path.expanduser("~/.cache/")

if os.path.isfile(filePath+"temp_weather.xml"):
    tw = open(filePath+"temp_weather.xml",'r')
    lines = tw.readlines()
    tw.close()

    if len(lines) > 5:
        os.system("cp " + filePath + "temp_weather.xml " + filePath + "weather.xml")
        if debug: print "moved"
    else:
        if debug:print "short file"
else:
    if debug:print "no file"

