import requests


url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

returnedData = requests.get(url)

bitCoinDict = returnedData.json()

#print(bitCoinDict)
#print(type(bitCoinDict))

#print(bitCoinDict.items())

#for keys, values in bitCoinDict.items():
   #print(values)

print(bitCoinDict['bpi'])

currency = bitCoinDict['bpi']
#print(currency)

#for values in currency.items():
#    newCur = currency{values}
#    print(newCur)
dollarRate = currency['USD']['rate_float']
euroRate = currency['EUR']['rate_float']
poundRate = currency['GBP']['rate_float']
print('1 bitcoin is ${:.2f} (US Dollars)'.format(dollarRate))
print('1 bitcoin is £{:.2f} (Euro)'.format(euroRate))
print('1 bitcoin is €{:.2f} (Pound Sterling)'.format(poundRate))