class SpaceAge:
    earth_year_in_seconds = 31557600
    multipliers = {"mer":0.2408467,"ven": 0.61519726,"mar":1.8808158,"jup": 11.862615,"sat": 29.447498,"ura": 84.016846,"nep": 164.79132}

    def __init__(self, seconds:int):
        self.seconds = seconds
    def raw_earth_years(self):
        return self.seconds / SpaceAge.earth_year_in_seconds
    def on_earth(self):
        return round(self.raw_earth_years(), 2)
    def on_mercury(self):
        return round(self.raw_earth_years() / SpaceAge.multipliers["mer"], 2)
    def on_venus(self):
        return round(self.raw_earth_years() / SpaceAge.multipliers["ven"], 2)
    def on_mars(self):
        return round(self.raw_earth_years() / SpaceAge.multipliers["mar"], 2)
    def on_jupiter(self):
        return round(self.raw_earth_years() / SpaceAge.multipliers["jup"], 2)
    def on_saturn(self):
        return round(self.raw_earth_years() / SpaceAge.multipliers["sat"], 2)
    def on_uranus(self):
        return round(self.raw_earth_years() / SpaceAge.multipliers["ura"], 2)
    def on_neptune(self):
        return round(self.raw_earth_years() / SpaceAge.multipliers["nep"], 2)

