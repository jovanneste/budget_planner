import random
import sys

NUM_OF_MONTHS = int(input("Months to simulate: "))
recklessness =  float(input("Level of recklessness (0-1): "))


happiness = 0
bank_balance = 0
bills = 1000
unpaid=0
subscriptions = [5, 10, 25, 40, 50, 75, 100]
priority = ['getting my life in order', 'going out and kissing lots of men']
joy = {'handbag':100, 'makeup':30, 'dress':150, 'hair and nails':50, "spa":125}



for i in range(NUM_OF_MONTHS):
	print("Month " +str(i)+", savings: " + str(bank_balance) +", happiness: " +str(happiness))
	bank_balance+=2000
	p = random.choice(priority)
	if random.uniform(0,1)>recklessness:
		bank_balance-=bills 
		bank_balance-=random.choice(subscriptions)
		happiness-=5
	else:
		bank_balance -= random.choice(list(joy.values()))
		unpaid += bills

	if p == 'going out and kissing lots of men':
		bank_balance-=1000
		happiness+=3
	else:
		happiness+=1

	if i%12==0 and unpaid>3000:
		print("Police arrive to collect unpaid bills")
		if bank_balance-(unpaid*1.1)>0:
			print("You can afford to pay your bills")
			bank_balance -= unpaid*1.1
		else:
			print("You cannot afford yours bills and are sentenced to 2 years in prison")
			happiness-=1000
			sys.exit()

	

