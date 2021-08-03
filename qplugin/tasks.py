from .import *


class Task:
	def _getnames(self):
		cat = type(self).__qualname__
		cats = cat.split('.')

		if len(cats) == 1:
			act = current_method()
			act = convert_name(act)
		else:
			cat, act = cats

		return cat, act

	def _get(self):
			if isDroid:
				while len(edfile(OUT)) == 0: pass
				out = edfile(OUT)
				return eval(out)

			else:
				while len(adb(f'cat {OUT}')) == 0: pass
				out = adb(f'cat {OUT}')
				return eval(out)

	def _run(self):
			cat, act = self._getnames()
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


class Alert(Task):
	class Beep(Stream):
		def __init__(self, frequency: int=8000, duration: int=1000, amplitude: int=50):
			self.__dict__ = autodict(frequency, duration, amplitude)


	class Morse(Stream):
		def __init__(self, text: str, frequency: int=4000, speed: int=80, amplitude: int=50):
			self.__dict__ = autodict(text, frequency, speed, amplitude)


	class Say(Stream):
		def __init__(self, text: str, voice: str='default:default', pitch: int=5, speed: int=5, wait: bool=True):
			self.__dict__ = autodict(text, voice, pitch, speed, wait)


	class SayToFile(Stream):
		def __init__(self, text: str, path: str, voice: str='default:default', pitch: int=5, speed: int=5, wait: bool=True):
			self.__dict__ = autodict(text, path, voice, pitch, speed, wait)


	def toast(self, text: str, long: bool=False):
		self.__dict__ = autodict(text, long)
		return self._run()


	def notify(self, title: str, text: str=' ', icon: str='', permanent: bool=False, priority: int=3):
		self.__dict__ = autodict(title, text, icon, permanent, priority)
		return self._run()


	def notify_cancel(self, title: str='*'):
		self.__dict__ = autodict(title)
		return self._run()


	def stop_say(self):
		return self._run()


	def flash(self, set: bool=False):
		self.__dict__ = autodict(set)
		return self._run()


	def vibrate(self, *pattern: int):
		if not pattern:
			print(f'"pattern" está vazio')
			return

		pattern = (0, *pattern)
		pattern = str(pattern)
		pattern = pattern[1:-1]

		self.__dict__ = autodict(pattern)
		return self._run()


class App(Task):
	class List(Task):
		def __init__(self, match: str=None):
			self.match = match

		def package(self):
			self.mode = 'package'
			return self._run()

		def app(self):
			self.mode = 'app'
			return self._run()

		def activity(self):
			self.mode = 'activity'
			return self._run()

		def receiver(self):
			self.mode = 'receiver'
			return self._run()

		def service(self):
			self.mode = 'service'
			return self._run()

		def provider(self):
			self.mode = 'provider'
			return self._run()


	class Test(Task):
		def __init__(self, data: str):
			self.__dict__ = autodict(data)

# App
		def name(self):
			self.mode = 'name'
			return self._run()

		def version(self):
			self.mode = 'version'
			return self._run()

		def this(self):
			self.mode = 'this'
			return self._run()

# Calendar
		def c_calendar(self):
			self.mode = 'c_calendar'
			return self._run()

		def c_title(self):
			self.mode = 'c_title'
			return self._run()

		def c_note(self):
			self.mode = 'c_note'
			return self._run()

		def c_local(self):
			self.mode = 'c_local'
			return self._run()

		def c_start(self):
			self.mode = 'c_start'
			return self._run()

		def c_end(self):
			self.mode = 'c_end'
			return self._run()

		def c_allday(self):
			self.mode = 'c_allday'
			return self._run()

		def c_exists(self):
			self.mode = 'c_exists'
			return self._run()


	def info(self, package: str, ignorem: str='', details: bool=False):
		self.__dict__ = autodict(package, ignorem, details)
		return self._run()
	
	def camera(self, status: bool=None):
		self.__dict__ = autodict(status)
		return self._run()

	def home(self, page: int, launcher: None):
		self.__dict__ = autodict(page, launcher)
		return self._run()

	def kill(self, package: str, root: bool=False):
		self.__dict__ = autodict(package, root)
		return self._run()

	def launch(self, package: str, data: str='', recent: bool=True, new_start: bool=False):
		self.__dict__ = autodict(package, data, recent, new_start)
		return self._run()

	def recents(self):
		return self._run()


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