# Uncle Engineer (calculatesubmarine)



สวัสดีจร้าาาาทุกคน ไลบรารี่นี้เป็นโปรแกรมที่ลุงเขียนขึ้นมาเพื่อเผยแพร่เป็นวิทยาทาน
ให้ทุกคนได้ศึกษาภาษา Python แบบง่ายๆ อยากให้คนไทยเก่งเทีบยเท่าต่างชาติ ช่วย
กันพัฒนาประเทศเราให้ก้าวหน้า พึ่งตัวเองดีที่สุด ถ้ามัวแต่รอรัฐบาลสนับสนุนก็คงอีก 1000 ปี 555

เวอร์ชั่นนี้มีอะไรบ้าง

  - เช็คราคาหุ้นไทย 
  - อื่นๆ ลุงจะทยอยลงเรื่อยๆนะจ๊ะ

# เช็คราคาหุ้นไทย (thaistock())

  - เช็คราคาแบบเรียลไทม์
  - เช็คราคาเปลี่ยนกี่บาท
  - เช็คเปอร์เซ็นเปลี่ยนแปลง
  - เช็คว่าราคาอัพเดตตอนไหน





### วิธีติดตั้งแสนง่าย

ไปกดไลค์เพจ ก่อน [ลุงวิศวกร สอนคำนวณ](https://www.facebook.com/UncleEngineer)  ฮ่าาา ไม่บังคับ (กดไลค์หน่อยๆ 555)

เราจะติดตั้งผ่านเจ้า pip

```sh
pip install calculatesubmarine
```

ง่ายไหมล่ะ

วิธีใช้ก็ง่ายมาก
- เปิด Python แล้วพิพม์ตามนี้เลย

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
