from .import *


def run(action, pars):
	vals = getValues(pars)

	if isDroid:
		return SQL(DATABASE, action, vals)

	elif len(devices):
		db = 'database.db'

		SQL(db, action, vals, '012')

		rsh(f'adb push {db} {DATABASE}')
		size = getSize(DATABASE)

		rsh(f'adb shell am broadcast -a QPlugin')
		
		while size == getSize(DATABASE):
			continue

		rsh(f'adb pull {DATABASE} {db}')
		return SQL(db, action, vals, '3')

	else:
		exit('Nenhum dispositivo encontrado')


class Alert:
	

	def Beep(self, frequency=8000, duration=1000, amplitude=50, stream='media'):
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
	
	
	def Toast(self, text, long=0):
	    """
	    
	    Mostra uma mensagem na tela
	    
	    Args:
	        text (str): Texto da mensagem
	        
	        long (int): 1: A mensagem demora mais
	                    0: A mensagem demora menos
	    """
	    
	    return run('Toast', locals())
	    
	
	def Morse(self, text, frequency=4000, speed=80, amplitude=50, stream='media'):
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
	    
	    
	def Notify(self, title, text='', icon='', permanent=0, priority=3):
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
	    
	    
	def NotifyCancel(self, title='*'):
	    """
	    
	    Remove notificações
	    
	    Args:
	        title (str): Cancela notificações pelo título
	                     Obs: Se não definido o tiítulo,
	                     remove todas as notificações
	                     do QPlugin.
	    """
	    
	    return run('NotifyCancel', locals())
	    
	    
	def Say(self, text, voice='default:default', stream='media', pitch=5, speed=5, wait=True):
	    """
	    
	    Fala o que for digitado
	    
	    Args:
	        text   (str): Texto do que é falado
	        voice  (str): Voz do programa
	        
	        stream (str): Saída do som            [   call     ]
	                                              [   system   ]
	                                              [   ringer   ]
	                                              [   media    ]
	                                              [   alarm    ]
	                                              [   notify   ]
	                                                 
	        pitch  (int): Tonalidade da voz       [   1 - 10   ]
	        speed  (int): Velocidade da voz       [   1 - 10   ]  
	        
	        wait   (bool): Esperar até terminar                       
	    """
	
	    return run('Say', locals())
	
	
	def SayToFile(self, text, local, voice='default:default', pitch=5, speed=5, wait=True):
	    """
	    
	    Fala o que for digitado
	    
	    Args:
	        text  (str): Texto do que é falado
	        local (str): Local do arquivo
	        voice (str): Voz do programa
	        
	        pitch (int): Tonalidade da voz       [   1 - 10   ]
	        speed (int): Velocidade da voz       [   1 - 10   ]
	         
	        wait  (bool): Esperar até terminar                       
	    """
	
	    return run('SayToFile', locals())
	
	
	def StopSay(self):
	    """
	
	    Para a função Say enquanto está em execução
	    """
	
	    return run('StopSay', locals())
	
	
	def Flash(self, action=None):
	    """
	    
	    Liga/Desliga Lanterna
	    
	    Args:
	        action (str):  True: Liga a lanterna
	                      False: Desliga a lanterna
	                       None: Alterna entre ligado/desligado
	    """
	
	    return run('Flash', locals())

	
	def Vibrate(self, *pattern):
		"""

		Padrões de Vibres

		Args:
			pattern (tuple): tempo_de_espera,tempo_de_vibre
		"""

		if len(pattern) == 1:
			pattern = (0,pattern[0])


		pattern = str(pattern)

		pattern = pattern.replace(' ', '')
		pattern = pattern[1:-1]

		return run('Vibrate', locals())


class App:


	def Info(self, package, ignore='', unlanced=False, details=False):
		"""

		Obtém mais informações de apps

		Args:
			package   (str): Pacotes/Nome de Apps
			ignore    (str): Pacotes Ignorados

			unlanced (bool): Iniciar pacotes não inicializáveis
			details  (bool): Mostrar todos os detalhes
		"""

		return run('Info', locals())

	
	def Camera(self, status=None):
		"""

		Ativa/Desativa a Câmera

		Args:
			status (bool): [ True=Ativa | False=Desativa | None=Alterna ]
		"""

		return run('Camera', locals())

	
	def Home(self, page=0, launcher=None):
		"""

		Inícia um launcher

		Args:
			page     (int): Página de início
			launcher (str): Launcher que será inicializado
		"""
		
		return run('Home', locals())


	def Kill(self, package, root=False):
		"""

		Fechar um app a força

		Args:
			package  (str): Pacote do aplicativo
			root    (bool): Usar root para fechar
		"""

		return run('Kill', locals())


	def Launch(self, package, data=None, exclude_recents=False, new_start=False):
		"""

		Iniciar uma aplicação

		Args:
			package          (str): Pacote/Classes de Apps
			data             (str): Dados de entrada
			
			exclude_recents (bool): Excluir dos recentes
			new_start       (bool): Nova inicialização
		"""

		return run('Launch', locals())

	
	def List(self, mode, match=''):
		"""

		Lista informações de aplicações

		Args:
			mode  (str): Tipo de informação listada	[ Package  ]
													[ App      ]
													[ Activity ]
													[ Receiver ]
													[ Services ]
													[ Provider ]
			
			match (str): Lista usando glob (!/*)
		"""

		return run('List', locals())
		