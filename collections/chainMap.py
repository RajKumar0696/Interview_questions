"""ChainMap combines a lot of dictionaries together and returns a list of dictionaries.
 ChainMaps basically encapsulates a lot of dictionaries into one single unit with no
 restriction on the number of dictionaries.

The following program ChainMap to return two dictionaries."""

import collections

dictionary1 = {'a': 1, 'b': 2}
dictionary2 = {'c': 3, 'b': 4}
chain_Map = collections.ChainMap(dictionary1, dictionary2)
print(chain_Map.maps)
