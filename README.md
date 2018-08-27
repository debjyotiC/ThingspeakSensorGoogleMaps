# Plotting the sensor data from Thingspeak on Google Maps 

This repo downloads the sensor from Thingspeak and overlays it on Google Maps with maker containing the sensor `data` and time of `last update`.

## Getting Started

To get started cd to the `GoogleMapsPlotter` to install the gmplot lib, type `$sudo setup.py install` or `$ sudo pip install gmaplot`.

### Prerequisites

The support modules required to run the code are :
     
      1. urllib2 --> For opening URLs
      2. jason --> As JASON encoder/decoder 

### Installing
After installing the gmplot lib (`by setup.py or by pip`), navigate to the install folder `/usr/local/lib/python2.7/dist-packages/gmplot` if done via `pip` or `<install_dir>/gmplot/` if done via `setup.py` and replace the gmplot.py with the one form this repo.  

## Running the tests

To update the map with sensor data run the `thingspeak_goolgemaps.py` from the thingspeakCode folder as `$python thingspeak_goolgemaps.py` , the src variable in the `gmap.marker(hidden_gem_lat, hidden_gem_lon,src)` can be used to pass in any string that is to be pesented in the marker as shown in the figure.

The map view with sensor value and update time stamp, 
                                    <img src="https://github.com/debjyotiC/ThingspeakSensorGoogleMaps/blob/master/maps.png" width="580">

## Web access
If the code from the above runs successfully `my_map.html` will be generated in the `thingspeakCode folder` this file will be updated after every 10s depending on the Thingspeak server's refresh time. To access this file over the we install apache2 on with `sudo apt-get install apache2 -y` and change `gmap.draw("my_map.html")` to `gmap.draw("\var\www\html\my_map.html")` and run the code as `$sudo python thingspeak_goolgemaps.py`. This will generate the my_maps.html in apache's default HTML webpage folder, to access this file over the web use dataplicity's (https://www.dataplicity.com) wormhole feature. 

## Authors

* **Debjyoti Chowdhury** - *Initial work* - [MyGithub](https://github.com/debjyotiC)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* **Michael Woods** -*For gmplot* [Github](https://github.com/vgm64/gmplot)
