#!/usr/bin/env python3
######################################################################
#
# You need to install required libraries with the following commands:
#
# sudo pip3 install adafruit-extended-bus
# sudo pip3 install adafruit-circuitpython-ahtx0
# sudo pip3 install adafruit-circuitpython-bh1750
# sudo pip3 install adafruit-circuitpython-bme280
# sudo pip3 install adafruit-circuitpython-sht31d
# sudo pip3 install adafruit-circuitpython-sgp30
# sudo pip3 install adafruit-circuitpython-sgp40
# sudo pip3 install adafruit-circuitpython-scd30
# sudo pip3 install adafruit-circuitpython-tsl2561
# sudo pip3 install adafruit-circuitpython-ssd1305
# sudo pip3 install adafruit-circuitpython-ssd1305
# sudo pip3 install adafruit-circuitpython-ssd1306
# sudo pip3 install adafruit-circuitpython-ds1307
#
#####################################################################
from adafruit_extended_bus import ExtendedI2C as I2C
from adafruit_ahtx0 import AHTx0
from adafruit_bh1750 import BH1750
from adafruit_bme280 import Adafruit_BME280_I2C as BME280
from adafruit_sht31d import SHT31D
from adafruit_sgp30 import Adafruit_SGP30 as SGP30
from adafruit_sgp40 import SGP40
from adafruit_scd30 import SCD30
from adafruit_tsl2561 import TSL2561
from adafruit_ssd1305 import SSD1305_I2C
from adafruit_ssd1306 import SSD1306_I2C
from adafruit_ds1307 import DS1307

ahtx0_addresses = [0x38]
bmx_addresses = [0x76,0x77]
bh1750_addresses = [0x23,0x5C]
sht3x_addresses = [0x44,0x45]
sgp30_addresses = [0x58]
sgp40_addresses = [0x59]
scd30_addresses = [0x61]
tsl2561_addresses = [0x29,0x39,0x49]
ssd130x_addresses = [0x35,0x36]
ds1307_addresses = [0x68]

#######################################################################################
#
#  The Raspberry Pi I2C buses need to be enabled in /boot/config.txt like this:
#
#  for I2C-0:   with SDA = GPIO0 (pin 27) and SCL = GPIO1 (pin 28)        - fixed pin #
#  ====================================================================================
#  dtparam=i2c_arm=on
#
#  for I2C-1:   with SDA = GPIO2 (pin 3) and SCL = GPIO3 (pin 5)          - fixed pin #
#  ====================================================================================
#  dtparam=i2c_vc=on
#
#  for I2c-4    with SDA = GPIO6 (pin 31) and SCL = GPIO7 (pin 26) - configurable pin #
#  ====================================================================================
#  dtoverlay=i2c-gpio,bus=4,i2c_gpio_delayUs=1,i2c_gpio_sda=6,i2c_gpio_scl=7
#
#######################################################################################
i2c0 = I2C(0)
i2c1 = I2C(1)
i2c4 = I2C(4)

def bus_scan(i2c,devices):
    for device in devices:
        for address in ahtx0_addresses:
            if device == address:
                print("AHTx0 temperature, humidity sensor at: ",hex(device))
                try:
                    sensor = AHTx0(i2c)
                    print("sensor initialized")
                    print("Temperature = %.0f °C"%sensor.temperature)
                    print("Relative Humidity = %.0f %"%sensor.relative_humidity)
                except OSError:
                    print("sensor doesn't respond")
        for address in bmx_addresses:
            if device == address:
                print("BMx temperature, humidity sensor at: ",hex(device))
                try:
                    sensor = BME280(i2c)
                    print("sensor initialized")
                    print("Temperature = %.0f °C"%sensor.temperature)
                    print("Relative Humidity = %.0f %"%sensor.relative_humidity)
                    print("Pressure = %.0f mbar"%sensor.pressure)
                except OSError:
                    print("sensor doesn't respond")
        for address in bh1750_addresses:
            if device == address:
                print("BH1750 light intensity sensor at: ",hex(device))
                try:
                    sensor = BH1750(i2c)
                    print("sensor initialized")
                    print("Light intensity = %.0f Lux"%sensor.lux)
                except OSError:
                    print("sensor doesn't respond")
        for address in sht3x_addresses:
            if device == address:
                print("SHT3x temperature, humidity sensor at: ",hex(device))
                try:
                    sensor = SHT31D(i2c)
                    print("sensor initialized")
                    print("Temperature = %.0f °C"%sensor.temperature)
                    print("Relative Humidity = %.0f %"%sensor.relative_humidity)
                except OSError:
                    print("sensor doesn't respond")
        for address in sgp30_addresses:
            if device == address:
                print("SGP30 air quality sensor at: ",hex(device))
                try:
                    sensor = SGP30(i2c)
                    print("sensor initialized")
                    print("CO2 = %d ppm"%sensor.eCO2)
                    print("TVOC = %d ppb"%sensor.TVOC)
                except OSError:
                    print("sensor doesn't respond")
        for address in sgp40_addresses:
            if device == address:
                print("SGP40 air quality sensor at: ",hex(device))
                try:
                    sensor = SGP40(i2c)
                    print("sensor initialized")
                    print("Raw Gas = ", sensor.raw)
                except OSError:
                    print("sensor doesn't respond")
        for address in scd30_addresses:
            if device == address:
                print("SCD30 Temperature, Humidity & CO2 sensor at: ",hex(device))
                try:
                    sensor = SCD30(i2c)
                    print("sensor initialized")
                    print("Temperature = %.0f °C"%sensor.temperature)
                    print("Relative Humidity = %.0f %"%sensor.relative_humidity)
                    print("CO2 = %d ppm"%sensor.CO2)
                except OSError:
                    print("sensor doesn't respond")
        for address in tsl2561_addresses:
            if device == address:
                print("TSL2561 light intensity sensor at: ",hex(device))
                try:
                    sensor = TSL2561(i2c)
                    print("sensor initialized")
                    print("Light intensity = %.0f Lux"%sensor.lux)
                    print("Broadband = %.0f"%sensor.broadband)
                    print("Infrared = %.0f"%sensor.infrared)
                    print("Luminosity = %.0f"%sensor.luminosity) 
                except OSError:
                    print("sensor doesn't respond")
        for address in ssd130x_addresses:
            if device == address:
                print("SSD130x display at: ",hex(device))
                try:
                    display = SSD1305_I2C(i2c)
                    print("display initialized")
                except OSError:
                    print("display doesn't respond")
        for address in ds1307_addresses:
            if device == address:
                print("DS1307 RTC at: ",hex(device))
                try:
                    rtc = DS1307(i2c)
                    print("rtc initialized")
                    print("Date/Time = ",rtc.datetime)
                except OSError:
                    print("rtc doesn't respond")

def main():
    print('Scan i2c-0 bus...')
    devices = i2c0.scan()
    print('i2c devices found on bus 0:',len(devices))
    bus_scan(i2c0,devices)

    print('Scan i2c-1 bus...')
    devices = i2c1.scan()
    print('i2c devices found on bus 1:',len(devices))
    bus_scan(i2c1,devices)

    print('Scan i2c-4 bus...')
    devices = i2c4.scan()
    print('i2c devices found on bus 4:',len(devices))
    bus_scan(i2c4,devices)


if __name__ == "__main__":
     main()



