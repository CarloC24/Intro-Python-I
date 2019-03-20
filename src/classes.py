# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE


class lat_lng:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def sayMyLatandLng(self):
        return print(f'My lat is {self.lat} and my lng is {self.lng}')


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(lat_lng):
    def __init__(self, lat, lng, name):
        super().__init__(lat, lng)
        self.name = name

    def __str__(self):
        return 'This is the Waypoint Class'


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class geocache(Waypoint):
    def __init__(self, lat, lng, name, difficulty, size):
        super().__init__(lat, lng, name)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return 'This is the Geocache class'

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521


# YOUR CODE HERE
waypoint = Waypoint(41.70505, -121.51521, "Catacombs")
print(waypoint.lat)
print(waypoint.lng)
print(waypoint.name)
print(waypoint.sayMyLatandLng())
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
print(geocache)
