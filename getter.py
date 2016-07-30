#!/usr/bin python2

import json
import os
import traceback

from googlefinance import getQuotes

securities = ['AAPL', 'TSLA', 'GOOG', 'VGSNX', 'RTN']
prefix = 'data'

def get_security(security_symbol):
	quote = getQuotes(security_symbol)[0]
	quote_data = {}
	quote_data['price'] = quote['LastTradePrice']
	quote_data['time'] = quote['LastTradeTime']
	quote_data['symbol'] = quote['StockSymbol']

	return quote_data

for security in securities:
	data = get_security(security)

	try:
		with open(os.path.join(prefix, '{0}_{1}.json'.format(data['symbol'], data['time'])), 'w') as f:
			f.write(json.dumps(data, indent=4, sort_keys=True))
	except Exception as e:
		traceback.print_exc(e)
		continue