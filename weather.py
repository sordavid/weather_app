import requests
# bb2c404683921cdea62ce543bac5e976 API key
api_key = 'bb2c404683921cdea62ce543bac5e976'
longitude = -84.386330
latitude = 33.753746

print("This is a weather app built in Python, please type in a city!")
user_input = input("Type in your city: ")
weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=imperial")

# print(weather_data.status_code) # Should return 200 status for active connection
# print(weather_data.json()) # returns the data in json format

weather = weather_data.json()['weather'][0]['main']
temp = round(weather_data.json()['main']['temp'])

print(f"The weather is {weather} in {user_input}")
print(f"The temperature is: {temp}°F")