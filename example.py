#!/usr/bin/python3

from qplugin.tasks import Audio

audio = Audio()

for i in range(10):
    audio.Notify(i, True, True)

