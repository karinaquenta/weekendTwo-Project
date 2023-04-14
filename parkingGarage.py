
class ParkingGarage():
    def __init__(self, max_tickets = 50, max_spaces = 50):
        self.max_tickets = max_tickets
        self.max_spaces = max_spaces
        self.open_tickets = max_tickets
        self.open_spaces = max_spaces
        self.current_ticket = {}
        self.tickets = []
        self.parking_spaces = []

    def driver(self):
        garage = True
        while garage:
            response = input("Welcome to the parking garage. Please press 1 to take a ticket, 2 for paying, and 3 to leave or 4 to quit: ")
            if response == "1":
                self.takeTicket()
            elif response == "2":
                self.payForParking()
            elif response == "3":
                self.leaveGarage()
            elif response == "4":
                print("Come again soon!")
                garage = False
            else: 
                print('Invalid Input, try again.')
                

    def payForParking(self):
        if self.current_ticket.get('paid'):
            print('Your ticket was already paid for.')
        else:
            pay = input('Ticket are 5 Dollars. Please type 5 to authorize this purchase (type 5): ')
            if pay:
                self.current_ticket['paid'] = True
                print('Thank you! Enjoy your time here.')
            else:
                print('We did not receive your payment, please try again.')

    def takeTicket(self):
        if self.open_tickets > 0 and self.open_spaces > 0:
            self.open_tickets -= 1
            self.open_spaces -= 1
            ticket_number = len(self.tickets) + 1
            self.current_ticket = {'ticket_number': ticket_number, 'paid': False}
            self.tickets.append(self.current_ticket)
            self.parking_spaces.append(ticket_number)
            print(f'You have successfully taken a ticket. Your ticket number is {ticket_number}')
        else:
            print(f'Sorry the garage is full! No more tickets at this time.')


    def leaveGarage(self):
        if self.current_ticket.get('paid'):
            print('Thanks, take care now!')
        else:
                # come back to this once running and adjust to display the ticket price upon paying.
            pay = input('Please pay for your ticket now: ')
            if pay == '5':
                self.current_ticket['paid'] = True
                print('Thank you, please come again soon!')
            else:
                print('We did not get your payment, try again please.')
        ticket_number = self.current_ticket.get('ticket_number')
        self.tickets.remove(self.current_ticket)
        self.parking_spaces.remove(ticket_number)
        self.open_tickets += 1
        self.open_spaces += 1

new_garage = ParkingGarage()
new_garage.driver()     
