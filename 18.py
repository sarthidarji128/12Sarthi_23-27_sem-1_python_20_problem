from datetime import datetime, timedelta

class Room:
    def __init__(self, room_id, capacity):
        self.room_id = room_id
        self.capacity = capacity
        self.reservations = []

    def check_availability(self, start_time, end_time):
        for reservation in self.reservations:
            if reservation.is_overlapping(start_time, end_time):
                return False
        return True

    def book_room(self, user, start_time, end_time):
        if self.check_availability(start_time, end_time):
            reservation = Reservation(user, self, start_time, end_time)
            self.reservations.append(reservation)
            user.add_reservation(reservation)
            return True
        else:
            return False

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.reservations = []

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

class Reservation:
    def __init__(self, user, room, start_time, end_time):
        self.user = user
        self.room = room
        self.start_time = start_time
        self.end_time = end_time

    def is_overlapping(self, other_start_time, other_end_time):
        return (self.start_time < other_end_time and self.end_time > other_start_time)

    def send_notification(self):
        print(f"Notification: Reservation for {self.room.room_id} on {self.start_time} to {self.end_time} confirmed. Email sent to {self.user.email}.")


room1 = Room(room_id=1, capacity=10)
room2 = Room(room_id=2, capacity=8)

user1 = User(user_id=101, name="u1", email="u1@gmail.com")
user2 = User(user_id=102, name="u2", email="u2@gmail.com")

booking_result1 = room1.book_room(user1, datetime(2023, 1, 1, 9, 0), datetime(2023, 1, 1, 11, 0))
booking_result2 = room2.book_room(user2, datetime(2023, 1, 1, 10, 0), datetime(2023, 1, 1, 12, 0))
booking_result3 = room1.book_room(user1, datetime(2023, 1, 1, 13, 0), datetime(2023, 1, 1, 14, 0))

print(f"Booking Result 1: {booking_result1}")
print(f"Booking Result 2: {booking_result2}")
print(f"Booking Result 3: {booking_result3}")

for reservation in user1.reservations:
    reservation.send_notification()

for reservation in user2.reservations:
    reservation.send_notification()
