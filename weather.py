import talks
import pyowm

def main():

    owm = pyowm.OWM('528f493a92ec155d0833ec740c511075')  # You MUST provide a valid API key

    # You have a pro subscription? Use:
    # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

    # Will it be sunny tomorrow at this time in Milan (Italy) ?
    forecast = owm.daily_forecast("Kanpur,in")
    tomorrow = pyowm.timeutils.tomorrow()
   

           # Always True in Italy, right? ;-)
    
    # Search for current weather in London (UK)
    observation = owm.weather_at_place('Kanpur,in')
    w = observation.get_weather()
    #print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

    # Weather details
    print "The wind speed is " +str((w.get_wind())['speed'])
    talks.main("The wind speed is " +str((w.get_wind())['speed']))                  # {'speed': 4.6, 'deg': 330}
    print "The relative humidity is "+str(w.get_humidity())       
    talks.main("The relative humidity is "+str(w.get_humidity()))       # 87
    temp= w.get_temperature('celsius')
    print "The current temperature is " + str(temp['temp'])
    talks.main("The current temperature is " + str(temp['temp']))


    if forecast.will_be_sunny_at(tomorrow) == True:
       print "Thankfully, It may be sunny tomorrow"
       talks.main("Thankfully, It may be sunny tomorrow")
    else:
       print "Buckle up! It may not be sunny tomorrow"
       talks.main("Buckle up! It may not be sunny tomorrow")
  

    # Search current weather observations in the surroundings of
    # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
    observation_list = owm.weather_around_coords(-22.57, -43.12)

