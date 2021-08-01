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