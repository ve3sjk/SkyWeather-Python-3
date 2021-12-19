This is the initial commit of a port of SkyWeather to Python 3

I have made additional changes to the original files as follows

Currently Working Sensors and my development system

as3935
veml6070
bme680
sht30
ads1015
oled
tsl2591

System is currently sending data to 

internal mysql database - custom
so it may not out of the box 
support original database

It should not take much work to make it work
i think its a coulple of lines that are commented
out in SkyWeather.py and some setting in your 
conflocal.py and it should work. Of course you need
to import the data base into mysql as well.

Further Modifications to orig files include

- Added settings in config file

#MySQL Logging and Password Information
enable_MySQL_Logging = False
MySQL_Password = "password"
MySQL_Address = "x.x.x.x"
MySQL_User = "xxxx"
MySQL_Database = "xxxx"
MySQL_Database2 = "xxxx"

Any reference in other files and MySql 
calls now use the above settings.

- Added settings in config file

MySQL_debug = True
WU_debug = False

Additional debug flags
- shows MySQL query string
- shows WeatherUnderground URL String

Getting it to run as a background service

 change to pigpio-develop directory 
 run make
 run make install
 
 This will install the development verison
 of pigpio that is currently working on my
 develpment system which is raspberry Pi4b
 running Ubuntu Server 20.04 via direct USB
 boot from external SSD.
 
 create a cron job, i use webmin for this
 on the server that runs startserver.sh
 in the root directory at boot
 
 
 all the original version can be found below.
 
 
SkyWeather Libraries and Examples for Raspberry Pi Solar Powered Weather Station<BR>

Supports SwitchDoc Labs WeatherRack PiWeather Board <BR> 

All documentation is on:<BR>

https://shop.switchdoc.com/products/skyweather-raspberry-pi-based-weather-station-kit-for-the-cloud

December 15, 2019: Version 055 - MySQL SolarMAX Fixes



