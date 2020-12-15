# calculatesubmarine

This project is to explain how to upload Python project into Pypi Package.
This project include; 
- Calculate traveling distance of submarine
- Calculate fuel of submarine
- Calculate Battery of submarine

How to calcualte
- You have to insert price, budget, distance(km)



#How to install pip

```sh
pip install calculatesubmarine
```


Example 1

```sh

import calculatesubmarine
from calculatesubmarine import ElectricSubmarine
from calculatesubmarine import *
from calculatesubmarine import ElectricSubmarine as ESM #abb


kongtab2 = calculatesubmarine.Submarine(10000,400000,100000) #price,budget,battery distance

ElectricArmy = ElectricSubmarine(20000,50000,100000)
ElectricArmy.Goto('North Korea',20000)
ElectricArmy.Battery()

Kongtanarmy = ESM()
print(Kongtanarmy.budget)
```


Example 2

```sh
from calculatesubmarine import *

tesla = ElectricSubmarine(40000,2000000,100000) #price+budget
	print(tesla.cap_name)
	print(tesla.budget)
	tesla.Goto('Japan',10000)
	print(tesla.BudgetRemaining) #call function fuel in fucntion Budgetremaining
	tesla.Battery()


	print('-------------------------------------')

	Navykongtab = Submarine(40000,2000000,10000) #price+budget
	print(Navykongtab.cap_name)
	print(Navykongtab.budget)
	Navykongtab.Goto('Japan',10000)
	print(Navykongtab.BudgetRemaining)
```


#file setup.py
- You have to renew some detail about project (name,author, keyword, ..)

#file __init__

from calculatesubmarine.submarine import Submarine
from calculatesubmarine.submarine import ElectricSubmarine

# Go to command prompt
--pip install twine --

#Open cmd again
cd calculatesubmarine

--python setup.py sdist--
to generate package to server
(you will ahve dist folder in package folder)

--twine upload dist/*--
Enter user and password

Uploading to server then you can go to check at https://pypi.org/project/calculatesubmarine/

Thank you
