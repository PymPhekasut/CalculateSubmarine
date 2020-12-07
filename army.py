#army.py

import submarine
from submarine import ElectricSubmarine
from submarine import *
from submarine import ElectricSubmarine as ESM #abb


kongtab2 = submarine.Submarine(10000,400000,100000) #price,budget,battery distance

ElectricArmy = ElectricSubmarine(20000,50000,100000)
ElectricArmy.Goto('North Korea',20000)
ElectricArmy.Battery()

Kongtanarmy = ESM()