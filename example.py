from qplugin.tasks import *
from time import sleep as wait

	
Toast('Olá, Mundo!!!')
wait(0.500)


Toast("'oi' em coódigo morse")
Morse('oi')


Notify('Esse é o QPlugin',
	            permanent=1, 
	            priority=5)

Beep(6000, 100)
Beep(7000, 1000)
Beep(8000, 10000)


NotifyCancel()


