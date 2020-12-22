from qplugin.tasks import App
from time import sleep

sleep(3)

out = App().Kill('lt.andro.broadcastlogger', True)
print(out)
