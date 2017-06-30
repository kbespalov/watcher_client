import argparse
import sys

import yaml

from watcher.client import Client
from watcher.config import WatcherConfig


def status(opts, client):
    response = client.status()
    print(yaml.safe_dump(response.as_dict(), default_flow_style=False))


def start(opts, client):
    params = {}
    try:
        with open(opts.config_file) as f:
            params = yaml.safe_load(f)
    except Exception as e:
        pass
    config = WatcherConfig(**params)
    client.start(config)
    print('started: ok')


def markets(opts, client):
    print(yaml.safe_dump(client.markets(), default_flow_style=False))


def stop(opts, client):
    client.stop()
    print('stopped: ok')


def get_parser():
    """Build a parser of command line interface"""

    base = argparse.ArgumentParser()

    subparsers = base.add_subparsers(help='list of commands')

    cmd = 'status'
    status_parser = subparsers.add_parser(cmd, help='Returns a status of the '
                                                    'watcher')
    status_parser.set_defaults(cmd=status)

    cmd = 'stop'
    stop_parser = subparsers.add_parser(cmd, help='Stop the watcher process')
    stop_parser.set_defaults(cmd=stop)

    cmd = 'markets'
    markets_parser = subparsers.add_parser(cmd, help='Returns a list of '
                                                     'markets available '
                                                     'for watching')
    markets_parser.set_defaults(cmd=markets)

    cmd = 'start'
    start_parser = subparsers.add_parser(cmd, help='Starts the watcher '
                                                   'process, returns result')

    start_parser.set_defaults(cmd=start)
    start_parser.add_argument('-c', '--config', dest='config_file',
                              help='watcher params in the yaml format')

    for p in [status_parser, stop_parser, markets_parser, start_parser]:
        p.add_argument('-a', '--api-key', dest='key', default=None)
        p.add_argument('--host', dest='host',
                       default='http://localhost:5000/v1')

    return base


def main():
    parser = get_parser()
    namespace = parser.parse_args(sys.argv[1:])
    if 'cmd' in namespace and namespace.cmd:
        try:
            client = Client(namespace.host, namespace.key)
            namespace.cmd(namespace, client)
        except Exception as e:
            print('Failed: %s' % str(e))


if __name__ == '__main__':
    main()
