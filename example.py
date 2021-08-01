#!/usr/bin/python3

from qplugin.test import Alert

toast = Alert().Toast('Teste')
out = toast.finished()
print(out is True)

# Alert().Beep().call()