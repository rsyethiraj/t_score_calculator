This repository consists of a simple script to compute T scores (Trond scores, or weight adjusted erg scores) when provided with a list of names, weights, and either erg splits or watts. 

T scores are a performance metric used by lightweight rowers to adjust erg (rowing machine) performance based on rower weight. 

The script can take in rower weights in either pounds or kilograms, but not both. It can also read data as both erg splits (time/500m, for example a 1:59.3 split means it takes the rower 1 minute and 59.3 seconds to row 500 meters) or watts. The conversion formula used is watts = 2.8 / (t^3), where t = seconds/500m. 

Currently, only a python implementation exists. I plan on adding different implementations in other languages in the future.
