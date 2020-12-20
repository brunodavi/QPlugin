from qplugin.tasks import App, Alert

Alert().Beep(10000, duration=250)
app_info = App().Info('Youtube')

print(app_info)

