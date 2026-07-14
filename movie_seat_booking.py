from threading import *
import time

lock = Lock()

tickets = {}
for i in range(1, 51):
    tickets[i] = True


class generation(Thread):
    def __init__(self, seat):
        super().__init__()
        self.seat = seat

    def run(self):
        with lock:
            try:
                if tickets[self.seat]:
                    print(f"seat no {self.seat} is available")
                    time.sleep(1)
                    print(f"seat no {self.seat} is successfully booked")
                    tickets[self.seat] = False
                else:
                    print("seat is not longer available")
            except:
                print("enter valid seat number")


class cancelation(Thread):
    def __init__(self, seat):
        super().__init__()
        self.seat = seat

    def run(self):
        with lock:
            try:
                if tickets[self.seat] == False:
                    tickets[self.seat] = True
                    print(f"seat no {self.seat} is successfully canceled")
                else:
                    print("ticket is not booked")
            except:
                print("enter valid seat number")


print("welcome to abc cinemas, how can we help you")

while True:
    print("\n1.show available seats")
    print("2.book seat")
    print("3.cancel seat")
    print("4.exit")

    command = int(input())

    if command == 1:
        for i in tickets:
            if tickets[i]:
                print(i, end=" ")
        print()

    elif command == 2:
        seat = int(input("enter seat number: "))
        t = generation(seat)
        t.start()
        t.join()

    elif command == 3:
        seat = int(input("enter seat number: "))
        t = cancelation(seat)
        t.start()
        t.join()

    elif command == 4:
        break
