class WatcherConfig(object):
    """Represents the set of configuration options for te watcher"""

    def __init__(self, bank_fee: float = None,
                 default_market_update_rate: int = None,
                 fiat_update_delay: int = None,
                 market_expiration_time: int = None,
                 markets: list = None,
                 max_tx_volume: float = None,
                 observers: list = None,
                 refresh_rate: int = None,
                 report_queue: str = None):
        """"""
        self.bank_fee = bank_fee
        self.default_market_update_rate = default_market_update_rate
        self.fiat_update_delay = fiat_update_delay
        self.market_expiration_time = market_expiration_time
        self.markets = markets
        self.max_tx_volume = max_tx_volume
        self.observers = observers
        self.refresh_rate = refresh_rate
        self.report_queue = report_queue

        self.attributes = {
            'bank_fee'
            'default_market_update_rate',
            'fiat_update_delay',
            'market_expiration_time',
            'markets',
            'max_tx_volume',
            'observers',
            'refresh_rate',
            'report_queue'
        }

    def as_dict(self):
        return {a: getattr(self, a) for a in self.attributes if
                getattr(self, a, None)}


class WatcherStatus(WatcherConfig):
    """Represents the json from /v1/status"""

    def __init__(self):
        super().__init__()
        self.is_started = None
        self.last_start_time = None
        self.amqp_url = None
        self.attributes.add('amqp_url')

    def update_from_response(self, response):
        print(response)
        self.is_started = response['is_started']
        self.last_start_time = response['last_start_time']
        for a in self.attributes:
            setattr(self, a, response['current_parameters'].get(a, None))
        return self
