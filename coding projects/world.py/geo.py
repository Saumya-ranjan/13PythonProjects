class Geolocation:
    def __init__(self,latitude,longitude):
        self.latitude = latitude
        self.longitude = longitude

    def closest_parallel(self):
        return round(self.latitude)

    



tokyo  = Geolocation(latitude = 12.34, longitude =12.34).closest_parallel()
print(tokyo)
