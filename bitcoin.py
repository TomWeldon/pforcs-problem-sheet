#Show current bitcoin rate in USD, GBP and Euro
#Author: Tom Weldon G00398828


# import the requests library
import requests

# url for get request
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

# url of json file for get request assigned to returnedData
returnedData = requests.get(url)

#assigning returnData json file to  bitCoinDict dictionary
bitCoinDict = returnedData.json()


# accessing nested dictionaries 'USD', 'EUR', 'GBP' within the nested dictionary 'bpi'
# and assigning the value of key 'rate_float' within 'USD', 'EUR', and 'GBP' to 
# dollarRate, euroRate and poundRate
dollarRate = bitCoinDict['bpi']['USD']['rate_float']
euroRate = bitCoinDict['bpi']['EUR']['rate_float']
poundRate = bitCoinDict['bpi']['GBP']['rate_float']

# printing  current USD, Euro and GBP  rate for 1 bitcoin corrected to two decimal places

print('')
print('1 Bitcoin = ${:.2f} (US Dollars)'.format(dollarRate))
print('\t    €{:.2f} (Euro)'.format(euroRate))
print('\t    £{:.2f} (Pound Sterling)'.format(poundRate))
