try:
    from androidhelper import Android
    droid = Android()
except:
    from os import popen


def run(action='ACTION', parameters={'qpy': 'Test'}):
    """
    Broadcast do app QPlugin

    Args:
        action      (str): Ações do QPlugin
        parameters (dict): Define variáveis do QPlugin
    """
    
    try:
        droid.sendBroadcast(action, extras=parameters)

    except:
        par = ''
        for k, v in parameters.items():
            if type(v) == list:

                l = ''
                for s in v:
                    l += f'{s},'
                    v = l[:-1]

                par += f'--esal {k} {v} '
            else:
                par += f'--es {k} {str(v)} '

        parameters = par[:-1]
        popen(f"am broadcast --user 0 -a {action} {parameters}")


def beep(frequency='8000', duration='1000', amplitude='50', stream='media'):
    """
    Executa uma frequência sonora
    
    Args:
        frequency (str | int): Valor da frequência     [ 20 - 16000 ]
        duration  (str | int): Duração em milesegundos [  1 - 10000 ]
        amplitude (str | int): Amplificação do som     [  1 -   100 ]


        stream          (str): Saída do som            [   call     ]
                                                       [   system   ]
                                                       [   ringer   ]
                                                       [   media    ]
                                                       [   alarm    ]
                                                       [   notify   ]
    """

    run('BEEP', locals())


def toast(text, long=False):
    """
    Mostra uma mensagem na tela
    
    Args:
        text       (str): Texto da mensagem
        
        long (str | int): True  (1) A mensagem demora mais para desaparecer
                          False (0) A mensagem demora menos para desaparecer
        
    """
    
    run('TOAST', locals())

