'''Write a Class 'Train' which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways.'''

class Train:
    def __init__(self, name, seat, fare):
        self.name = name
        self.seat = seat
        self.fare = fare
    
    def getStatus(self):
        print(f"Train :  {self.name} | Available Seats : {self.seat}")
    
    def getFareInfo(self):
        print(f"Train: {self.name} | Ticket Fare: ₹{self.fare}")
    
    def bookTicket(self):
        if(self.seat>0):
            print(f"Ticket book successfully on {self.name}. Seat Number: {self.seat}")
            self.seat -= 1
        else:
            print("❌ Sorry, no seats available.")

t1 = Train("Rajdhani Express", 3, 1500)

t1.getStatus()       # Available seats
t1.getFareInfo()     # Fare information
t1.bookTicket()      # Book a seat
t1.getStatus()       # Seats updated
t1.bookTicket()
t1.bookTicket()
t1.bookTicket()      # No seat available now