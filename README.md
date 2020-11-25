# Euphony

![image info](https://img.shields.io/badge/python-3.6%2B-brightgreen)

Python package to play music in background while your code runs.

## How to use

Its pretty simple to use. Create a instance of the `player` class and let your code run enclosed in a with statement with the instance.

``` python

  from euphony import player
  mozart = player.player()

  with mozart:
      for i in range(1000000000):
          pass
  # plays music while the code runs
```

That's all ~!

## Installation

Euphony is pip-installable. Just run following cmd in terminal:

``` bash
  pip install euphony
```
