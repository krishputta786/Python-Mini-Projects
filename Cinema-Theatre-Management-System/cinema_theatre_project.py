class Movie:
    def __init__(self, movie_name, language, duration, ticket_price):
        self.movie_name = movie_name
        self.language = language
        self.duration = duration
        self.ticket_price = ticket_price

    def display_movie(self):
        print("\n----- Movie Details -----")
        print(f"Movie Name: {self.movie_name}")
        print(f"Language: {self.language}")
        print(f"Duration: {self.duration}")
        print(f"Ticket Price: {self.ticket_price}")


class Theatre:
    def __init__(self, theatre_name, movie, total_seats):
        self.theatre_name = theatre_name
        self.movie = movie
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.booked_tickets = 0

    def display_theatre(self):
        print("\n----- Theatre Details -----")
        print(f"Theatre Name   : {self.theatre_name}")
        print(f"Movie          : {self.movie.movie_name}")
        print(f"Total Seats    : {self.total_seats}")
        print(f"Available Seats: {self.available_seats}")

    def check_availability(self):
        print(f"Available seats: {self.available_seats}")

    def book_ticket(self, quantity):
        if quantity <= 0:
            print("Number of tickets must be greater than 0")
            return False

        if quantity > self.available_seats:
            print("Insufficient seats!",self.available_seats,"seats are available")
            return False

        self.available_seats -= quantity
        self.booked_tickets += quantity

        print("Tickets booked successfully!")
        return True

    def cancel_ticket(self, quantity):
        if quantity <= 0:
            print("Number of tickets must be greater than 0")
            return False

        if quantity > self.booked_tickets:
            print("Invalid cancellation! You cannot cancel more tickets than booked")
            return False

        self.available_seats += quantity
        self.booked_tickets -= quantity

        print("Tickets cancelled successfully!")
        return True


class Booking:
    def __init__(self, customer_name, movie, ticket_count):
        self.customer_name = customer_name
        self.movie = movie
        self.ticket_count = ticket_count

    def calculate_amount(self):
        return self.ticket_count * self.movie.ticket_price

    def display_booking(self):
        print("\n----- Booking Details -----")
        print(f"Customer     : {self.customer_name}")
        print(f"Movie        : {self.movie.movie_name}")
        print(f"Tickets      : {self.ticket_count}")
        print(f"Ticket Price : {self.movie.ticket_price}")
        print(f"Total Amount : {self.calculate_amount()}")


movie = Movie("Avatar 2", "English", "3 Hours", 250)
theatre = Theatre("PVR Cinemas", movie, 100)


while True:
    print("\n==============================")
    print(" CINEMA THEATRE MANAGEMENT")
    print("==============================")
    print("1--> Display Movie")
    print("2--> Display Theatre")
    print("3--> Check Available Seats")
    print("4--> Book Tickets")
    print("5--> Cancel Tickets")
    print("6--> Exit")
    print("==============================")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Invalid input! Please enter a number from 1 to 6.")
        continue

    if choice == 1:
        movie.display_movie()

    elif choice == 2:
        theatre.display_theatre()

    elif choice == 3:
        theatre.check_availability()

    elif choice == 4:
        customer_name = input("Enter your name: ")

        try:
            ticket_count = int(input("Enter number of tickets: "))

        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if theatre.book_ticket(ticket_count):
            booking = Booking(
                customer_name,
                movie,
                ticket_count
            )

            booking.display_booking()
            print("Available Seats:", theatre.available_seats)

    elif choice == 5:
        customer_name = input("Enter your name: ")

        try:
            ticket_count = int(
                input("Enter number of tickets to cancel: ")
            )

        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if theatre.cancel_ticket(ticket_count):
            print("Available Seats:", theatre.available_seats)

    elif choice == 6:
        print("Thank you for visiting Cinema Theatre Management System.."
              "Have a Nice Day!")
        break

    else:
        print("Invalid menu choice! Please select 1 to 6.")

