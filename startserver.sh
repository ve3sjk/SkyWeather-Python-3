#!/bin/bash
# This is a script to automatically run SkyWeather

cd /home/active/SDL_Pi_SkyWeather
rm weatherold.out
mv weather.out weatherold.out
sudo pigpiod
sudo python SkyWeather.py &>weather.out &
