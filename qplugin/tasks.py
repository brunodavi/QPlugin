from .import *

def run(action: str, pars: dict):
	
	dic = globals()
	key = action
	func = dic[key]
	
	funckeys = func.__code__.co_varnames
	parskeys = tuple(pars.keys())
	
	values = pars.values()
	
	if funckeys != parskeys:
		values = tuple(values)[::-1]
					
	send = f'{action}\n\n'
	
	for v in values:
		send += f'<>>\n{v}\n<<>\n\n'
		
	edfile(LOCAL_RESULT, '')
	edfile(LOCAL_OUT, send)
	
	while True:
		read = edfile(LOCAL_RESULT)
		quant = len(read)
		
		if quant != 0:
			break
	
	from result import RESULT
	return RESULT


def Beep(frequency=8000, duration=1000, amplitude=50, stream='media'):
    """
    
    Executa uma frequência sonora
    
    Args:
        frequency (int): Frequência sonora       [ 20 - 16000 ]
        duration  (int): Duração em milesegundos [  1 - 10000 ]
        amplitude (int): Amplificação do som     [  1 -   100 ]

        stream    (str): Saída do som            [   call     ]
                                                 [   system   ]
                                                 [   ringer   ]
                                                 [   media    ]
                                                 [   alarm    ]
                                                 [   notify   ]
    """

    return run('Beep', locals())


def Toast(text, long=0):
    """
    
    Mostra uma mensagem na tela
    
    Args:
        text (str): Texto da mensagem
        
        long (int): 1: A mensagem demora mais
                    0: A mensagem demora menos
        
    """
    
    return run('Toast', locals())
    

def Morse(text, frequency=4000, speed=80, amplitude=50, stream='media'):
    """
    
    Executa um coódigo morse
    
    Args:
        text       (str): Texto a ser pronunciado
        
        frequency  (int): Frequência sonora          [ 20 - 16000 ]
        speed      (int): Velocidade da reprodução   [  1 -   100 ]
        amplitude: (int): Amplificação do som        [  1 -   100 ]
        
        stream     (str): Saída do som               [   call     ]
                                                     [   system   ]
                                                     [   ringer   ]
                                                     [   media    ]
                                                     [   alarm    ]
                                                     [   notify   ]
    """
    return run('Morse', locals())
    
    
def Notify(title, text='', icon='', permanent=0, priority=3):
    """
    
    Mostra uma notificação
    
    Args:
        title     (str): Título da notificicação
                         Obs: Se existir uma
                         notificação com o mesmo
                         título, ela é atualizada
                     
        text      (str): Texto da notficação
        icon      (str): Local do ícone
        
        permanent (int): 1 = Notificação permanente
                         0 = Notificaçaão padrão
                         
        priority  (int): Nível de alerta da notificação [ 1 - 5 ]
    """
    
    return run('Notify', locals())
    
    
def NotifyCancel(title='*'):
    """
    
    Remove notificações
    
    Args:
        title (str): Cancela notificações pelo título
                     Obs: Se não definido o tiítulo,
                     remove todas as notificações
                     do QPlugin.
    """
    
    return run('NotifyCancel', locals())