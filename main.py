import alpaca_trade_api as alpaca
import os
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv('APCA_API_BASE_URL')
print(f'Alpaca API base URL: {base_url}')

api = alpaca.REST()
account = api.get_account()
print(account)

if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))
print(f'Current equity: ${account.equity}')

balance_change = float(account.equity) - float(account.last_equity)
print(f'Today\'s portfolio balance change: ${balance_change}')
