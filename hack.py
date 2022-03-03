import os
import time
from colorama import Fore
import random

try:
	while True:
		var = random.randint(1, 6)
		pipca = {
			1: Fore.GREEN,
			2: Fore.BLUE,
			3: Fore.RED,
			4: Fore.YELLOW,
			5: Fore.RESET,
			6: Fore.MAGENTA
		}
		print(pipca[var] + """▇◤▔▔▔▔▔▔▔◥▇
▇▏◥▇◣┊◢▇◤▕▇
▇▏▃▆▅▎▅▆▃▕▇
▇▏╱▔▕▎▔▔╲▕▇
▇◣◣▃▅▎▅▃◢◢▇
▇▇◣◥▅▅▅◤◢▇▇
▇▇▇◣╲▇╱◢▇▇▇""")
		print()
		print(Fore.RESET + "Нажмите ctrl + c для выхода")
#		time.sleep(0.1)
		os.system("clear")
except:
	print(Fore.MAGENTA + "Goodbye!")
