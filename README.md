# QPlugin <img width=50 src="/src/icon.png"/> 
* Usado para executar ações do android pelo Python3

### Como usar:

* Instale o QPlugin.apk ou importe o projeto do Tasker
* Abra a aplicação que ela mostrará uma notificação de serviço


### Como funciona?

* O terminal envia um broadcast para o QPlugin App
* O qplugin.py é usado como blibioteca das ações disponíveis


### Exemplo com python3:

    from qplugin import toast, run
  
    # Executa uma mensagem com o texto: Exemplo 1
    toast('Exemplo 1')
  
    # Executa uma mensagem com o texto: Exemplo 2
    pars = {'text': 'Exemplo 2', 'long': True}
    run('TOAST', pars)


### Exemplo com terminal android:

    # Executa uma mensagem com o texto: Exemplo 3
    am broadcast --user 0 -a TOAST --es text 'Exemplo 3' --es long False


### Exempo com adb:

    # Executa uma mensagem com o texto: Exemplo 4
    adb shell am broadcast --user 0 -a TOAST --es text 'Exemplo 4' --es long True


### Demonstrações:
<img width=250 src="/src/termux.gif"/> <img width=250 src="/src/qpython.gif"/>
![Example](/src/adb.gif)

