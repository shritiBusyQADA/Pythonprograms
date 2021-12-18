class bird:

    species = 'parrot'
    name = 'Dobby'
    age = 2

    def sing(self, song, name):   # self is current object of the class
        return "{} sings {}'and {}'".format(self.name, song, name)


t = bird()   # creating object by calling bird constructor
print(t.sing('Hotel California', 'Harry'))


# Constructors and Destructors
class bird1:

    species = None
    name = None
    age = None

    def __init__(self, species, name, age):  # Explicit Constructor
        self.species = species
        self.name = name
        self.age = age

    def describe(self):
        return "{} is a {} of age {}".format( self.name, self.species, self.age)

    def sing(self, song):
        return "{} sings '{}'".format(self.name, song)


# Create Instances of the bird class
b1 = bird1('Parrot', 'Dobby', 4)
b2 = bird1('Owl', 'Hedwig', 5)

print(b1.describe())
print(b1.sing('Hotel California'))

print(b2.sing('Happy'))
