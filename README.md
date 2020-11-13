# QPlugin <img width=50 src="/src/icon.png"/>
### Executa ações do android pelo python3

### Como usar:

* Instale o [QPlugin.apk](https://github.com/brunodavi/QPlugin/blob/master/app/QPlugin.apk?raw=true) ou importe o projeto no [Tasker](https://taskernet.com/shares/?user=AS35m8nXHtAHUb3g429CktIgI9aKlA1%2FEglWKHxy0IyPwx0q7aeQMBH2ekF4AG%2F7FRqn58T5R5q3qrGmIPwa&id=Project%3AQPlugin)
* Abra a aplicação que ela mostrará uma notificação de serviço


### Como funciona?

* O python envia instruções pelo arquivo out.txt para o QPlugin.apk executar
* O qplugin é usado como biblioteca das ações disponíveis


### Tarefas

* Beep
* Toast
* [NEW] Morce
* [NEW] Notify
* [NEW] NotifyCancel


### Exemplo com python3:

    from qplugin.tasks import Toast, run
  
    # Executa uma mensagem com o texto: Exemplo 1
    Toast('Exemplo 1')
  
    # Executa uma mensagem com o texto: Exemplo 2
    pars = {'text': 'Exemplo 2', 'long': 1}
    run('Toast', pars)


