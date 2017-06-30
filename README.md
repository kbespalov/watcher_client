## Requirements.

Python 3+

## Installation

Locally:
```
pip install .
```

Remote:
```sh
pip install git+https://github.com/kbespalov/watcher_client.git
```

## Usage:

- Python Client

```python

from watcher.client import Client
from watcher.config import WatcherConfig

client = Client(host='https://abc.com/v1', api_key='12345')

client.status()
client.markets()

# start with defaults params

client.start()
client.stop()

# overwrite defaults

config = WatcherConfig(refresh_rate=5, observers=['Rabbitmq'])
client.start(config)
client.stop()

```

- CLI

```sh

 watcher markets --host https://abc.com/v1  api_key='12345'
 
- CampBXUSD
- CoinBaseUSD
- OKCoinCNY
- BtceUSD
- BTCCCNY
- BtceEUR
- BitstampUSD
- GeminiUSD
- BitfinexUSD
- KrakenUSD
- PaymiumEUR
- KrakenEUR

```

```sh

watcher start  --host https://abc.com/v1  api_key='12345' 
```
```sh
watcher start  --host https://abc.com/v1  api_key='12345' -c params.yaml   
```

```yaml
# params.yaml example
refresh_rate: 5
observers:
 - Logger
 - Rabbitmq
```


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_fee** | **float** | Bank fees accounting at conversion | [optional] [default to 0.007]
**default_market_update_rate** | **int** | Default market&#39;s depth update rate in seconds | [optional] [default to 20]
**fiat_update_delay** | **int** | Delay in seconds between an exchange rate updates | [optional] 
**market_expiration_time** | **int** | Markets order book expiration time | [optional] 
**markets** | **list[str]** | List of market names | [optional] 
**max_tx_volume** | **float** | The max money volume that can be involved into transfer | [optional] [default to 10.0]
**observers** | **list[str]** | List of opportunity observers names | [optional] 
**refresh_rate** | **int** | Update rate in seconds of the arbiter&#39;s main loop | [optional] [default to 20]
**report_queue** | **str** | The name of the response queue | [optional] [default to 'arbitrage_watcher']