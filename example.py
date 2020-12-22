from qplugin.tasks import App
from time import sleep

app = App()
pkg = app.Info('brave')['app_package'][0]

app.Launch(pkg, 'https://www.google.com/')
