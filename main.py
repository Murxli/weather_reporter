from email import message
import requests
from twilio.rest import Client
import os

lat = YOUR LATITUDE
lon = YOUR LONGITUDE


api_key = YOUR OPEN WEATHER API KEY
api_ep = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"


twilio_id = YOUR TWILIO ID
token = YOUR TWILIO TOKEN

parameters = {
    "cnt" : 4
}

def weather_report(codes) :
    if len([id for id in codes if id< 300]) >= 1 :
            return "There might be a storm today.Avid being outside"
    if len([id for id in codes if id< 400]) >= 1 :
            return "It will be drizzly today, Carry an umbrella"
    if len([id for id in codes if id< 600]) >= 1 :
            return "It will be rainy today, Carry an umbrella"
    if len([id for id in codes if id< 700]) >= 1 :
            return "It will be snowy today, Carry an umbrella"
    if len([id for id in codes if id< 900]) >= 1 :
            return "Weather will be pleasant today"

response = requests.get(url=api_ep, params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]
weather_codes = []
for hr_data in weather_data :
    report = hr_data["weather"][0]["description"]
    print(report)
    id = hr_data["weather"][0]["id"]
    weather_codes.append(id)

msg = weather_report(weather_codes)
print(msg)


client = Client(twilio_id, token)

message = client.messages.create(
    body= msg,
    from_= YOUR TWILIO NUMBER,
    to= MOBILE NUMBER TO REPORT
)
print(message.sid)
