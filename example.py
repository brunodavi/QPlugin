from qplugin.tasks import App
from time import sleep

sleep(3)

app = App()
pkg = app.Info('Brave')['app_package'][0]

app.Launch(pkg, 'https://www.google.com/')
