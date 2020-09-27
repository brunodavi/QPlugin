# QPlugin <img width=50 src="/src/icon.png"/>
* Usado para executar ações do android pelo Python3

<img width=250 src="/src/termux.gif"/> <img width=250 src="/src/qpython.gif"/>

### Tarefas

* Beep
* Toast
* [NEW] Morce
* [NEW] Notify
* [NEW] NotifyCancel


### Como usar:

* Instale o QPlugin.apk ou importe o projeto do Tasker
* Abra a aplicação que ela mostrará uma notificação de serviço


### Como funciona?

* O python envia instruções pelo arquivo out.txt para o QPlugin.apk executar
* O qplugin é usado como biblioteca das ações disponíveis


### Exemplo com python3:

    from qplugin.tasks import Toast, run
  
    # Executa uma mensagem com o texto: Exemplo 1
    Toast('Exemplo 1')
  
    # Executa uma mensagem com o texto: Exemplo 2
    pars = {'text': 'Exemplo 2', 'long': 1}
    run('Toast', pars)


