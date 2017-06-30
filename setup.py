from setuptools import setup

setup(name='arbitrage watcher client',
      version='0.1.0',
      packages=['watcher'],
      install_requires=['requests', 'PyYAML'],
      entry_points={
            'console_scripts': [
                  'arbitrage-watcher = watcher.cli:main'
            ]
      })
