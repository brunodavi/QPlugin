# QPlugin <img width="50" src="/src/icon.png"/>

### Como usar:

* Instale o [QPlugin.apk](https://github.com/brunodavi/QPlugin/releases/download/1.7/QPlugin.apk) ou importe o projeto no [Tasker](https://taskernet.com/shares/?user=AS35m8nXHtAHUb3g429CktIgI9aKlA1%2FEglWKHxy0IyPwx0q7aeQMBH2ekF4AG%2F7FRqn58T5R5q3qrGmIPwa&id=Project%3AQPlugin)
* Abra a aplicação que ela mostrará uma notificação de serviço


### Como funciona?

* O python envia instruções pelo data.json para o QPlugin executar
* O qplugin é usado como biblioteca das ações disponíveis


### Exemplo com python3:

    from qplugin.tasks import Alert
  
    alert = Alert()
    alert.Toast('Exemplo', 1)
