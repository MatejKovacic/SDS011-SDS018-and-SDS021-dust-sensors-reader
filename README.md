# SDS011, SDS018 and SDS021 dust sensors reader
Python application for reading data from SDS011, SDS018 and SDS021 dust sensors.

### What is particulate matter (PM)?

Atmospheric particulate matter, also known as particulate matter (PM) or particulates, are microscopic solid or liquid matter suspended in Earth's atmosphere. Sources of particulate matter can be natural or anthropogenic. They have strong impact on human health.

Particulates with a diameter between 2.5 and 10 micrometers (μm), also called PM10 are inhalable. So called fine PM, (often referred to as PM2.5), tend to penetrate into the gas exchange regions of the lung (alveolus), and very small particles (< 100 nanometers) may pass through the lungs to affect other organs.

### Health effects of particulate matter
Particulates are one of the deadliest form of air pollution due to their ability to penetrate deep into the lungs and blood streams unfiltered, causing permanent DNA mutations, heart attacks, and premature death. The IARC and WHO designate airborne particulates a Group 1 carcinogen.

A study from 2013has shown that for every increase of 10 μg/m3 in PM10, the lung cancer rate rose 22%. The smaller PM2.5 were particularly deadly, with a 36% increase in lung cancer per 10 μg/m3 as it can penetrate deeper into the lungs.

### Dust sensors
A Chinese company Inovafitness is producing cheap laser based dust sensors called SDS011, SDS018 and SDS021. They can be connected to computer via USB port. We are publishing Python application for reading SDS011, SDS018 and SDS021 dust sensor data.

Usage:
```sh
$ python dust-sensor-read.py
```
or:
```sh
python dust-sensor-read.py /dev/ttyUSB1
```

### About
This code is a fork from https://github.com/aqicn/sds-sensor-reader. It was developed by Matjaž Rihtar and Matej Kovačič as a part of a BlueSensor project. BlueSensor project is developing hardware and software for collecting data from cheap sensors and visualise them via web interface. More about the BlueSensor project: https://telefoncek.si/tag/BlueSensor/.
