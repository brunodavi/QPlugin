#!/usr/bin/python3

from qplugin.tasks import Alert
from time import sleep

Alert().Notify('Teste', 'Notificação', priority=5)
sleep(1)
Alert().NotifyCancel()