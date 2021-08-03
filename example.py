#!/usr/bin/python3

from qplugin.tasks import Alert, App

Alert().toast('Testando')

app_list = App().List('*termux').package()
App().launch(app_list[0])