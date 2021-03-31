#!/usr/bin/python3

from qplugin.tasks import Alert, get

alert = Alert()
alert.Toast('oi')
out = get()

print(out)
print(type(out))
