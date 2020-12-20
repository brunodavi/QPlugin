from qplugin.tasks import App, Alert


app = App()
taskerInfo = app.Info('Tasker', details=True)
print(taskerInfo)
