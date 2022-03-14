# Ranodm Number
from random import random
upperlim = int(input("Enter Upper Limit : "))
lowerlim = int(input("Enter Lower Limit : "))
print(f'''Random Number : {
    lowerlim + random() * ( upperlim-lowerlim )
}''')