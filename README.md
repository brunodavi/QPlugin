# QPlugin
![](/src/icon.png =50x50)
* Usado para executar ações do android pelo Python3

<img width=250 src="/src/termux.gif"/> <img width=250 src="/src/qpython.gif"/>
![example](/src/adb.gif)


### Como usar:

* Instale o QPlugin.apk ou importe o projeto do Tasker
* Abra a aplicação que ela mostrará uma notificação de serviço


### Como funciona?

* O terminal envia um broadcast para o QPlugin App
* O qplugin.py é usado como biblioteca das ações disponíveis


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


### Editar a aplicação

[![Tasker](https://lh3.googleusercontent.com/Z32CI1HB_7uGRIyKhKGd6rt9jLBzRxFasowSEzUt0kGJJeFUYeKChxti4x8USm4xAg=s180-rw)](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm&hl=pt_BR)

* Use o Tasker se quiser editar a aplicação

![](https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png | width=100)
