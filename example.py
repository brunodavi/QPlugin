from qplugin.tasks import App
from time import sleep

app = App()

pkgs_info = app.List('App', 'ru.*')
print(pkgs_info)
