import random
import time as t
from datetime import datetime

saludo = ["@danoi","@jendaila","@guztioi"]
vacaciones = True
fin_vacaciones = "04-09"

while vacaciones:
	hoy = datetime.today()
	hoy_str = hoy.strftime("%m-%d")
	if hoy_str < fin_vacaciones:
		print("Egunon "+saludo[random.randint(0,2)])
		t.sleep(86400)
	else:
		vacaciones = False
