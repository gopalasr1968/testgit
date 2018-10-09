class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price


kenwood = Kettle("Kenwood", 12.99)
hamilton = Kettle("Hamilton", 14.55)
print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

