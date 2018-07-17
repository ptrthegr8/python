#!/bin/python3
""" 
A solution for the iss_location assignment.
This implementation uses python3 and urllib.request library.
Refactoring in python2 is left as an additional student exercise.
"""

import json
import urllib.request
import turtle
import time

iss_icon = './assessments/iss_location/iss.gif'
world_map = './assessments/iss_location/map.gif'

# For more info about open-notify see http://open-notify.org
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print('People in Space: ', result['number'])

people = result['people']
for p in people:
  print(p['name'], ' in ', p['craft'])


url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])
print('Latitude: ', lat)
print('Longitude: ', lon)

screen = turtle.Screen()
screen.setup(720, 360)
# image source: 
# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA
screen.bgpic(world_map)
screen.setworldcoordinates(-180, -90, 180, 90)

screen.register_shape(iss_icon)
iss = turtle.Turtle()
iss.shape(iss_icon)
iss.setheading(90)
iss.penup()
iss.goto(lon, lat)

# When Does ISS next pass over me?
# Indianapolis IN
lat = 39.768403
lon = -86.158068

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

#print result
over = result['response'][1]['risetime']
location.write(time.ctime(over))

# leave the screen open until user clicks on it
print('Click on screen to exit ...')
screen.exitonclick()

print('Completed.')