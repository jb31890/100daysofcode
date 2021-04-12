#!/usr/bin/env python

#sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
#result = { word:len(word) for word in sentence.split() }
#
#
#print(result)
#


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = { day:(weather_c[day] * 9/5) + 32 for day in weather_c }

print(weather_f)



