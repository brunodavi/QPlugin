#!/usr/bin/python3

from qplugin.tasks import Alert

alert = Alert()

alert.Toast('1')
alert.Toast('2')
alert.Toast('3')
alert.Toast('4')
alert.Toast('5')

alert.Beep(9000, 100)
alert.Beep(8000, 100)
