class Vehicle: 
    def __init__(self, make, model):
        self.make = make
        self.model = model 
    
    def move(self): 
        print("move along...")

    def get_make_model(self): 
        print(f"I'm {self.make} {self.model}")
        
my_car = Vehicle("Tesla", "Model 3")
my_car.move()
my_car.get_make_model()

your_car = Vehicle("Cadilac", "Escalade")
your_car.move()
your_car.get_make_model()

class Airplain(Vehicle): 
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id
    def move(self): 
        print("ply along ...")

class Truck(Vehicle): 
    def move(self): 
        print("rumble along ...")

class Golfcar(Vehicle): 
    pass

cessna = Airplain('Cessna', "skyhawk", "N-12345") 
mack = Truck("Mack", "Pinacle")
golfwagen = Golfcar("golfwagen", "GC1000")

golfwagen.move()
cessna.move()
mack.move()

for v in (my_car, your_car, cessna, mack, golfwagen): 
    v.get_make_model()
    v.move()