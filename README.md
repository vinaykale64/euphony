# Euphony

![py27](https://img.shields.io/badge/python-2.7-brightgreen)
![py36](https://img.shields.io/badge/python-3.6%2B-brightgreen)
![black](https://img.shields.io/badge/black--white)
![pypi](https://img.shields.io/badge/pypi-v0.0.5-blue)
![license](https://img.shields.io/badge/license-MIT-white)

Have you ever got bored of running long chunks of code? 

It can get repetitive to monitor the progress of the code continuously.

Euphony can help you. It is a Python package that plays classical 
music in background while your code runs whether it be on terminal 
or script or jupyter notebook. Once your code is complete
or if it errors out, it stops so you can go back to it. 

## How to use

Its pretty simple to use. Create a instance of the `player` class and let your code run enclosed 
in a `with` statement with the object. You can choose between `bach`, `beethoven`
or `mozart`. If not specified, it chooses at random. 

``` python

  from euphony import Player
  mozart = Player.player(artist = 'mozart') # options: ['bach', 'beethoven']

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
