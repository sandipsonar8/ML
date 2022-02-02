#prices are in per kg
prices={ 'suger' :60,
         'solt' :20,
         'oil' :120
       }
max_price=max(prices, key=prices.get)
print(max_prices)
