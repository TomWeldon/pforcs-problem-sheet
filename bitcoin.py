import requests


url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

returnedData = requests.get(url)

bitCoinDict = returnedData.json()

#print(bitCoinDict)
#print(type(bitCoinDict))

#print(bitCoinDict.items())

#for keys, values in bitCoinDict.items():
   #print(values)

#print(bitCoinDict['bpi'])

currency = bitCoinDict['bpi']
#print(currency)

#for values in currency.items():
#    newCur = currency{values}
#    print(newCur)
Usrate = currency['USD']['rate_float']
print(Usrate)