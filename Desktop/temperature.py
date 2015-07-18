import datetime
import sqlite3 as lite
import requests

api_key = "<api_key>"
url = 'https://api.forecast.io/forecast/' + api_key

cities = { "Atlanta": '33.762909,-84.422675',
            "Austin": '30.303936,-97.754355',
            "Boston": '42.331960,-71.020173',
            "Chicago": '41.837551,-87.681844',
            "Cleveland": '41.478462,-81.679435'
        }
        
url1 = 'https://api.forecast.io/forecast/APIKEY/LATITUDE,LONGITUDE,TIME'

datetime.datetime.now()

datetime.timedelta()

start_date = datetime.datetime.now() - datetime.timedelta(days=30)

datetime.timedelta(days=1)

end_date = datetime.datetime.now()

con = lite.connect('weather.db')
cur = con.cursor()

cities.keys()
with con:
    cur.execute('CREATE TABLE daily_temp ( day_of_reading INT, Atlanta REAL, Austin REAL, Boston REAL, Chicago REAL, Cleveland REAL);')
    
query_date = end_date - datetime.timedelta(days=30)

with con:
    while query_date < end_date:
        cur.execute("INSERT INTO daily_temp(day_of_reading) VALUES (?)", (int(query_date.strftime('%s')),))
        query_date += datetime.timedelta(days=1)

for k,v in cities.iteritems():
    query_date = end_date - datetime.timedelta(days=30)
    while query_date < end_date:
        r = requests.get(url + v + ',' +  query_date.strftime('%Y-%m-%dT12:00:00'))

        with con:
            cur.execute('UPDATE daily_temp SET ' + k + ' = ' + str(r.json()['daily']['data'][0]['temperatureMax']) + ' WHERE day_of_reading = ' + query_date.strftime('%s'))

	query_date += datetime.timedelta(days=1)


con.close()
