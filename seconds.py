import time

seconds = int(input("Enter the number of seconds: "))

for i in range(seconds, -1, -1):
    time.sleep(1)
    print(i, " seconds remaining")
print("Stopped")