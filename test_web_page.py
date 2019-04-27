from flask import Flask, render_template
import urllib2
import json
import time


def read_value():
    READ_API_KEY = '72N0S025TNQQ3OSI'
    CHANNEL_ID = 740792
    connt_speak = urllib2.urlopen(
        "http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" % (CHANNEL_ID, READ_API_KEY))
    response = connt_speak.read()
    data = json.loads(response)
    temp = data['field1']
    updated_at = data['created_at']
    data_str = "The sensor val:" + temp + " Last updated at:" + updated_at
    print data_str
    f = open('templates/map.html', 'w')
    message = """<!DOCTYPE html>
<html>
  <head>
    <style>
       /* Set the size of the div element that contains the map */
      #map {
        height: 969px;  /* The height is 400 pixels */
        width: 100%;  /* The width is the width of the web page */
       }
    </style>
  </head>
  <body>
    <!--The div element for the map -->
    <div id="map"></div>
    <script>"""
    message_2 = """function initMap() {
  // The location of Uluru
  var uluru = {lat: 22.5146298, lng: 88.4160477};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 15, center: uluru});
  // The marker, positioned at Uluru
   var marker = new google.maps.Marker({title: 'The sensor val: %s', position: uluru, map: map});
}
    </script>
    <!--Load the API from the specified URL
    * The async attribute allows the browser to render the page while the API loads
    * The key parameter will contain your own API key (which is not needed for this tutorial)
    * The callback parameter executes the initMap() function
    -->
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyC8vMJFml8r1638L2p4Pyow9DdpsfrvaZ8&callback=initMap">
    </script>
  </body>
</html>""" % temp
    f.write(message + message_2)
    f.close()


app = Flask(__name__)


@app.route("/")
def hello():
    time.sleep(15)
    read_value()
    return render_template('map.html')


if __name__ == "__main__":
    app.run()



