from .import *


class Task:
	def get(self):
			if isDroid:
				while len(edfile(OUT)) == 0: pass
				out = edfile(OUT)
				return eval(out)

			else:
				while len(adb(f'cat {OUT}')) == 0: pass
				out = adb(f'cat {OUT}')
				return eval(out)

	def run(self):
			cat, act = type(self).__qualname__.split('.')
			pars = dict(**self.__dict__)

			data = autodict(cat, act, pars)

			if isDroid:
				rsh(f'echo -n "" > {OUT}')
				edfile(JSON, f'{data}')
				return self.get()

			elif len(devices) > 0:
				adb(f'echo -n "" > {OUT}')
				adb(f'echo -n "$(echo -n {data} | base64 -w 0)" | base64 -d > {JSON}')
				return self.get()

			else:
				print('Nenhum android encontrado')

	class Stream:
			def call(self):
				self.stream = 'call'
				return self.run()

			def system(self):
				self.stream = 'system'
				return self.run()

			def ringer(self):
				self.stream = 'ringer'
				return self.run()

			def media(self):
				self.stream = 'media'
				return self.run()

			def alarm(self):
				self.stream = 'alarm'
				return self.run()

			def notify(self):
				self.stream = 'notify'
				return self.run()


class Alert(Task):
	class Toast(Task):
		def __init__(self, text: str, long: bool=False):
			self.text = text
			self.long = long
			self.out = self.run()

		def finished(self):
			return self.out

	class Beep(Task, Task.Stream):
		def __init__(self, frequency: int=8000, duration: int=1000, amplitude: int=50):
			self.frequency = frequency
			self.duration = duration
			self.amplitude = amplitude