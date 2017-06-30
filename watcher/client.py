import requests
from watcher.config import WatcherConfig, WatcherStatus


class Unauthorized(Exception):
    code = 401


class ServiceException(Exception):
    code = 400


class Client(object):
    """Provides the set of endpoints to manage arbitrage watcher service."""

    def __init__(self, host='http://localhost/v1', api_key=None):
        self._params = {'api_key': api_key} if api_key else {}
        self._host = host

    def start(self, config: WatcherConfig = None):
        """Starts the watcher process, returns result"""
        data = config.as_dict() if config else {}

        endpoint = '%s/start' % self._host
        response = requests.post(endpoint,
                                 params=self._params,
                                 json=data)

        if response.status_code == 200:
            return True
        elif response.status_code == 401:
            raise Unauthorized("You have no access to the endpoint")
        elif response.status_code == 400:
            print(response.json())
            raise ServiceException(
                'Failed to start: %s ' % response.json()['reason'])
        else:
            raise Exception(response.content)

    def stop(self):
        """Stop the watcher process"""
        endpoint = '%s/stop' % self._host
        response = requests.post(endpoint, params=self._params)
        if response.status_code == 200:
            return True
        elif response.status_code == 401:
            raise Unauthorized("You have no access to the endpoint")
        elif response.status_code == 400:
            raise ServiceException(
                'Failed to stop: %s ' % response.json()['reason'])

    def status(self) -> WatcherStatus:
        """Returns a status of the watcher"""
        endpoint = '%s/status' % self._host
        response = requests.get(endpoint, params=self._params)
        if response.status_code == 200:
            return WatcherStatus().update_from_response(response.json())
        elif response.status_code == 401:
            raise Unauthorized("You have no access to the endpoint")
        else:
            raise Exception(response.content)

    def markets(self):
        """Returns a list of markets available for watching"""
        endpoint = '%s/markets' % self._host
        response = requests.get(endpoint, params=self._params)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            raise Unauthorized("You have no access to the endpoint")
        else:
            raise Exception(response.content)
