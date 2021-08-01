from .import *


class Task:
	def _get(self):
			if isDroid:
				while len(edfile(OUT)) == 0: pass
				out = edfile(OUT)
				return out

			else:
				while len(adb(f'cat {OUT}')) == 0: pass
				out = adb(f'cat {OUT}')
				return out

	def _run(self):
			cat, act = type(self).__qualname__.split('.')
			pars = dict(**self.__dict__)

			data = autodict(cat, act, pars)
			print(data)

			if isDroid:
				rsh(f'echo -n "" > {OUT}')
				edfile(JSON, str(data))
				return self._get()

			elif len(devices) > 0:
				adb(f'echo -n "" > {OUT}')
				adb(f"echo -n '{b64(data)}' | base64 -d > {JSON}")
				return self._get()

			else:
				print('Nenhum android encontrado')


class Stream(Task):
		def call(self):
			self.stream = 'call'
			return self._run()

		def system(self):
			self.stream = 'system'
			return self._run()

		def ringer(self):
			self.stream = 'ringer'
			return self._run()

		def media(self):
			self.stream = 'media'
			return self._run()

		def alarm(self):
			self.stream = 'alarm'
			return self._run()

		def notify(self):
			self.stream = 'notify'
			return self._run()


class Alert:
	class Toast(Task):
		def __init__(self, text: str, long: bool=False):
			self.text = text
			self.long = long
			self.out = self._run()

	class Beep(Stream):
		def __init__(self, frequency: int=8000, duration: int=1000, amplitude: int=50):
			self.frequency = frequency
			self.duration = duration
			self.amplitude = amplitude

	class Morse(Stream):
		def __init__(self, text: str, frequency: int=4000, speed: int=80, amplitude: int=50):
			self.text = text
			self.frequency = frequency
			self.speed = speed
			self.amplitude = amplitude

	class Notify(Task):
		def __init__(self, title: str, text: str=' ', icon: str='', permanent: bool=False, priority: int=3):
			self.title = title
			self.text = text
			self.icon = icon
			self.permanent = permanent
			self.priority = priority
			self.out = self._run()

	class NotifyCancel(Task):
		def __init__(self, title: str='*'):
			self.title = title
			self.out = self._run()

# 	def Say(self, text, voice='default:default', stream='media', pitch=5, speed=5, wait=True):
# 	    """

# 	    Fala o que for digitado

# 	    Args:
# 	        text   (str): Texto do que é falado
# 	        voice  (str): Voz do programa

# 	        stream (str): Saída do som            [   call     ]
# 	                                              [   system   ]
# 	                                              [   ringer   ]
# 	                                              [   media    ]
# 	                                              [   alarm    ]
# 	                                              [   notify   ]

# 	        pitch  (int): Tonalidade da voz       [   1 - 10   ]
# 	        speed  (int): Velocidade da voz       [   1 - 10   ]  

# 	        wait   (bool): Esperar até terminar                       
# 	    """

# 	    return run('Say', locals())


# 	def SayToFile(self, text, local, voice='default:default', pitch=5, speed=5, wait=True):
# 	    """

# 	    Fala o que for digitado

# 	    Args:
# 	        text  (str): Texto do que é falado
# 	        local (str): Local do arquivo
# 	        voice (str): Voz do programa

# 	        pitch (int): Tonalidade da voz       [   1 - 10   ]
# 	        speed (int): Velocidade da voz       [   1 - 10   ]

# 	        wait  (bool): Esperar até terminar                       
# 	    """

# 	    return run('SayToFile', locals())


# 	def StopSay(self):
# 	    """

# 	    Para a função Say enquanto está em execução
# 	    """

# 	    return run('StopSay', locals())


# 	def Flash(self, set=None):
# 	    """

# 	    Liga/Desliga Lanterna

# 	    Args:
# 	        set    (str):  True: Liga a lanterna
# 	                      False: Desliga a lanterna
# 	                       None: Alterna entre ligado/desligado
# 	    """

# 	    return run('Flash', locals())


# 	def Vibrate(self, *pattern):
# 		"""

# 		Padrões de Vibres

# 		Args:
# 			pattern (tuple): tempo_de_espera,tempo_de_vibre
# 		"""

# 		if len(pattern) == 1:
# 			pattern = (0,pattern[0])


# 		pattern = str(pattern)

# 		pattern = pattern.replace(' ', '')
# 		pattern = pattern[1:-1]

# 		return run('Vibrate', locals())


# class App:


# 	def Info(self, package, ignore='', details=False):
# 		"""

# 		Obtém mais informações de apps

# 		Args:
# 			package   (str): Pacotes/Nome de Apps
# 			ignore    (str): Pacotes Ignorados

# 			details  (bool): Mostrar todos os detalhes

# 		Return: informações de apps (dict)
# 		"""

# 		return run('Info', locals())


# 	def Camera(self, status=None):
# 		"""

# 		Ativa/Desativa a Câmera

# 		Args:
# 			status (bool): [ True=ON | False=OFF | None=ON/OFF ]
# 		"""

# 		return run('Camera', locals())


# 	def Home(self, page=0, launcher=None):
# 		"""

# 		Inícia um launcher

# 		Args:
# 			page     (int): Página de início
# 			launcher (str): Launcher que será inicializado
# 		"""

# 		return run('Home', locals())


# 	def Kill(self, package, root=False):
# 		"""

# 		Fechar um app a força

# 		Args:
# 			package  (str): Pacote do aplicativo
# 			root    (bool): Usar root para fechar
# 		"""

# 		return run('Kill', locals())


# 	def Launch(self, package, data=None, recent=True, new_start=False):
# 		"""

# 		Iniciar uma aplicação

# 		Args:
# 			package          (str): Pacote/Classes de Apps
# 			data             (str): Dados de entrada

# 			recent          (bool): Adicionar aos recentes
# 			new_start       (bool): Nova inicialização
# 		"""

# 		return run('Launch', locals())


# 	def List(self, mode, match=None):
# 		"""

# 		Lista informações de aplicações

# 		Args:
# 			mode  (str): Tipo de informação listada
# 			[ Package  ]
# 			[ App      ]
# 			[ Activity ]
# 			[ Receiver ]
# 			[ Services ]
# 			[ Provider ]

# 			match (str): Lista usando glob (!/*)

# 		Return: Lista (list)
# 		"""

# 		return run('List', locals())

# 	def Recents(self):
# 		"""

# 		Mostra as aplicações recentes

# 		"""

# 		return run('Recents', locals())


# 	def Test(self, data, mode='name'):
# 		"""

# 		Obtém informações sobre Apps/Calendário

# 		Args:
# 			data (str): Pacote/Data

# 			mode (str): Calendário
# 									[ c_calendar ]
# 									[ c_title    ]
# 									[ c_note     ]
# 									[ c_local    ]
# 									[ c_start    ]
# 									[ c_end      ]
# 									[ c_allday   ]
# 									[ c_exists   ]

# 						Apps
# 									[ name       ]
# 									[ version    ]
# 									[ this       ]

# 		Return: Informações de Apps/Calendário (str)
# 		"""

# 		return run('Test', locals())


# class Audio:


# 	def Accessibility(self, level, display=False, sound=False):
# 		"""

# 		Define o volume da acessibilidade

# 		Args:
# 			level    (int): Nível do Volume
# 			display (bool): Mostra o volume definido
# 			sound   (bool): Tocar ao definir volume
# 		"""

# 		return run('Accessibility', locals())


# 	def Alarm(self, level, display=False, sound=False):
# 		"""

# 		Define o volume do alarme

# 		Args:
# 			level    (int): Nível do Volume
# 			display (bool): Mostra o volume definido
# 			sound   (bool): Tocar ao definir volume
# 		"""

# 		return run('Alarm', locals())


# 	def Bluetooth(self, level, display=False, sound=False):
# 		"""

# 		Define o volume do bluetooth

# 		Args:
# 			level    (int): Nível do Volume
# 			display (bool): Mostra o volume definido
# 			sound   (bool): Tocar ao definir volume
# 		"""

# 		return run('Bluetooth', locals())


# 	def Call(self, level, display=False, sound=False):
# 		"""

# 		Define o volume de chamada

# 		Args:
# 			level    (int): Nível do Volume
# 			display (bool): Mostra o volume definido
# 			sound   (bool): Tocar ao definir volume
# 		"""

# 		return run('Call', locals())


# 	def DTMF(self, level, display=False, sound=False):
# 		"""

# 		Define o volume do DTMF

# 		Args:
# 			level    (int): Nível do Volume
# 			display (bool): Mostra o volume definido
# 			sound   (bool): Tocar ao definir volume
# 		"""

# 		return run('DTMF', locals())


# 	def Effects(self, set=None):
# 		"""

# 		Ativa/Desativa Sons dos toques

# 		Args:
# 			set (bool): Define [ True=ON | False=OFF | None=ON/OFF ]
# 		"""

# 		return run('Effects', locals())


# 	def Feedback(self, set=None):
# 		"""

# 		Ativa/Desativa alguns eventos de vibrações

# 		Args:
# 			set (bool): Define [ True=ON | False=OFF | None=ON/OFF ]
# 		"""

# 		return run('Feedback', locals())


# 	def Media(self, level, display=False, sound=False):
# 		"""

# 		Define o volume de mídia

# 		Args:
# 			level    (int): Nível do Volume
# 			display (bool): Mostra o volume definido
# 			sound   (bool): Tocar ao definir volume
# 		"""

# 		return run('Media', locals())


# 	def Mic(self, set=None):
# 		"""

# 		Ativa/Desativa Microfone

# 		Args:
# 			set (bool): Define [ True=ON | False=OFF | None=ON/OFF ]
# 		"""

# 		if set is True:
# 			set = False

# 		elif set is False:
# 			set = True

# 		return run('Mic', locals())


# 	def Mode(self, set=None):
# 		"""

# 		Altera o padrão sonoro do dispositivo

# 		Args:
# 			set (bool): Define [ True=SOUND | False=MUTE | None=VIBRATE ]
# 		"""

# 		return run('Mode', locals())


# 	def Notify(self, level, display=False, sound=False):
# 		"""

# 		Define o volume de notificações

# 		Args:
# 			level    (int): Nível do Volume
# 			display (bool): Mostra o volume definido
# 			sound   (bool): Tocar ao definir volume
# 		"""

# 		return run('Notify', locals())


# 	def Ringer(self, level, display=False, sound=False):
# 		"""

# 		Define o volume de toque

# 		Args:
# 			level    (int): Nível do Volume
# 			display (bool): Mostra o volume definido
# 			sound   (bool): Tocar ao definir volume
# 		"""

# 		return run('Ringer', locals())


# 	def Ringtone(self, sound, set=None):
# 		"""

# 		Define os toques padrões de chamadas, notificações e alarme

# 		Args:
# 			sound (str): Nome/Local do toque
# 			set: (bool): Define [ True=ALARM | False=NOTIFY | None=RINGER ]

# 		"""

# 	def Speaker(self, set=None):
# 		"""

# 		Ativa/Desativa Viva Voz

# 		Args:
# 			set (bool): Define [ True=ON | False=OFF | None=ON/OFF ]
# 		"""

# 		return run('Speaker', locals())



# 	def System(self, level, display=False, sound=False):
# 		"""

# 		Define o volume do sistema

# 		Args:
# 			level    (int): Nível do Volume
# 			display (bool): Mostra o volume definido
# 			sound   (bool): Tocar ao definir volume
# 		"""

# 		return run('System', locals())


# class Code:


# 	def ADB(self, command, ip, port, timeout=1):
# 		"""

# 		Executa comandos do adb shell

# 		Args:
# 			command (str): Commando (ex: ls /sdcard/)
# 			     ip (str): IP do alvo (ex: 0.0.0.0)

# 			    port(int): Porta conectada (ex: 5555)
# 			timeout (int): Tempo de espera

# 		Return: Saída do ADB (str)
# 		"""

# 		return run('ADB', locals())


# 	def JavaScript(self, code, lib='', timeout=45):
# 		"""

# 		Executa JavaScript do Tasker

# 		Args:
# 			code    (str): Código JavaScript
# 			lib     (str): Bibliotecas
# 			timeout (int): Tempo de Espera

# 		Return: Variável %return
# 		"""

# 		return run('JavaScript', locals())


# 	def Shell(self, command, timeout=0, root=False):
# 		"""

# 		Executa shell script no Android

# 		Args:
# 			command (str): Comandos do Shell
# 			timeout (int): Tempo de Espera
# 			root   (bool): Usar Root


# 		Return: Erro & Saída (dict)
# 		"""

# 		return run('Shell', locals())


# class Display:

# 	def Auto(self, set=None):
# 		"""

# 		Mudar o Brilho Automático

# 		Args:
# 			set (bool): Define [ True=ON | False=OFF | None=ON/OFF ]

# 		"""

# 		return run('Auto', locals())