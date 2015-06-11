class Vehicle:
    name=""
    kind="car"
    color=""
    def desc(self):
        desc = "%s %s" %(self.name,self.kind)
        return desc

print dir(Vehicle)
car1=Vehicle()
car1.name="Swift"
car1.color="grey"
print car1.desc()
