# 🎬 Terminal Based Movie Seat Booking System

A multithreaded movie seat booking system developed in **Python** using **Object-Oriented Programming (OOP)** and the **threading** module. The application simulates a real-world cinema booking system where users can book and cancel seats while ensuring thread-safe operations.

---

## 🚀 Features

- 🎟️ View all available seats
- ✅ Book a seat
- ❌ Cancel a booked seat
- 🔒 Thread-safe seat booking using `Lock`
- ⚡ Simulates concurrent booking requests with Python threads
- 🖥️ Simple terminal-based user interface

---

## 🛠️ Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Multithreading
- Thread Synchronization (`Lock`)
- Time Module

---

## 📂 Project Structure

```
Movie-Seat-Booking/
│
├── movie_booking.py
└── README.md
```

---

## ⚙️ How It Works

### 1. Seat Initialization

- Creates 50 seats numbered from **1 to 50**
- Every seat is initially available (`True`)

### 2. Booking

- User selects a seat.
- A booking thread is created.
- The thread acquires a lock.
- If the seat is available:
  - Displays availability.
  - Simulates processing using `time.sleep(1)`.
  - Books the seat.
- Otherwise, informs the user that the seat has already been booked.

### 3. Cancellation

- User enters the seat number.
- A cancellation thread is created.
- The lock prevents race conditions.
- The booked seat becomes available again.

---

## 🔒 Thread Safety

This project uses Python's `threading.Lock()` to prevent multiple users from booking the same seat simultaneously.

Without synchronization:

- Two users could book the same seat.
- Data inconsistency may occur.

Using `Lock` ensures only one thread accesses the booking system at a time.

---

## 📸 Sample Output

```
Welcome to ABC Cinemas

1. Show Available Seats
2. Book Seat
3. Cancel Seat
4. Exit

Enter Choice: 2

Enter Seat Number: 15

Seat no 15 is available
Seat no 15 is successfully booked
```

---

## 💡 Future Improvements

- Multiple movie support
- Different seat categories (Gold, Silver, Platinum)
- Ticket price calculation
- User login and authentication
- File/Database storage
- GUI using Tkinter or PyQt
- Web version using Django or Flask

---

## 🎯 Learning Outcomes

Through this project, I gained hands-on experience with:

- Python Programming
- Object-Oriented Programming
- Multithreading
- Thread Synchronization
- Lock Mechanism
- Exception Handling
- Console Application Development

---

## 👨‍💻 Author

**Ganji Veera Viswanadha Swamy**

- GitHub: https://github.com/viswanadha123709
- LinkedIn: https://www.linkedin.com/in/veera-viswanadha-swamy-ganji-7a8177375

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
