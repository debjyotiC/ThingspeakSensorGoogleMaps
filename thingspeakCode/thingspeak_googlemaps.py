from gmplot import gmplot
import urllib2
import json
import time


READ_API_KEY = ''
CHANNEL_ID = 

# get data from cloud
def get_data():
  connt_speak = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" % (CHANNEL_ID, READ_API_KEY))
  response = connt_speak.read()
  data = json.loads(response)
  temp = data['field1']
  updated_at = data['created_at']
  data_str = "The sensor val:"+temp+" Last updated at:"+updated_at
  update_maps(data_str)

def update_maps(src):
  lat = #desired latitude
  lon = #desired longtitude 
  gmap = gmplot.GoogleMapPlotter(lat,lon, 13)
  hidden_gem_lat, hidden_gem_lon = lat,lon
  gmap.marker(hidden_gem_lat, hidden_gem_lon,src)
  gmap.draw("my_map.html")

def main():
  while True:
    get_data()
    print 'Map updated'
    time.sleep(10)


if __name__ == '__main__':
  main()
