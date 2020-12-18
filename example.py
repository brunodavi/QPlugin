from qplugin.tasks import App, Alert

app = App()
alert = Alert()

infos = app.Info('Chrome')

print(infos)

alert.Vibrate(100)