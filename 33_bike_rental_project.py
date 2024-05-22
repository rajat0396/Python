# display available stocks of bike give quantity of max 100
# user ask bike for rent
# exit from code
# if user boooked the bike show much left in the stock
# is user booked 1 bike its for 100 rs , if he booked 50 bikes, 5000rs , show much price for the bike

class BikeShop:
    def __init__(self,stock):    # using constructor to display stock
        self.stock=stock

    def displaybike(self):
        print("Total available Bikes are ", self.stock)    # will display total avaialble bike i.e self.stock

    def bikeforrent(self,noq):            # noq - number of quantity which user want to rent and then logic

        if noq<=0:                        # if quantity is leass than 0 , have to give more quantity 
            print("Please give quantity more than 0")
        elif noq>100:                                 # quantity should be leas sthan 100
            print("you can order maximum 100 bikes")
        
        else:
            print(" user rent Bike price", noq*100)           ## give user chooses 3 bike print the price noq*100
            print("after renting available bike", self.stock-noq)    # remaining bike in stock

while True:
    obj=BikeShop(100)       # object instantiation of class  , total 100 bike
    uc = int(input('''                     
                   1 Display Stocks
                   2 Rent a Bike
                   3 Exit '''))                 # i.e user choice what he wants to see
    
    if uc == 1:
        obj.displaybike()
    elif uc == 2:
        n=int(input("Enter the Quantity ----"))
        obj.bikeforrent(n)

    else:
        break




    
