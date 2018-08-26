from gmplot import gmplot
import urllib2
import json
import time


READ_API_KEY = 'VDGD8FE4VCJ841F8'
CHANNEL_ID = 556128

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
  gmap = gmplot.GoogleMapPlotter(22.6199901,88.4239493, 13)
  hidden_gem_lat, hidden_gem_lon = 22.6199901,88.4239493
  gmap.marker(hidden_gem_lat, hidden_gem_lon,str(src))
  gmap.draw("my_map.html")

def main():
  while True:
    get_data()
    print 'Map updated'
    time.sleep(10)


if __name__ == '__main__':
  main()
