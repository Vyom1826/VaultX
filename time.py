import threading
import time

# Global simulated time
hour = 0
minute = 0


def run_clock():
    global hour, minute

    while True:
        time.sleep(0.5)  # 0.5 real sec = 1 simulated minute

        minute += 1

        if minute == 60:
            minute = 0
            hour += 1

        if hour == 24:
            hour = 0


# Start clock in background
clock_thread = threading.Thread(target=run_clock, daemon=True)
clock_thread.start()


while True:
    print("\n1. Perform Task")
    print("2. Show Current Time")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task name: ")

        print(f"Task '{task}' completed.")
        print(f"Current Simulated Time: {hour:02d}:{minute:02d}")

    elif choice == "2":
        print(f"Current Simulated Time: {hour:02d}:{minute:02d}")

    elif choice == "3":
        break

    else:
        print("Invalid choice.")