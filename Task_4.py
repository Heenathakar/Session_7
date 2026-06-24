points = int(input("Enter your IPL fantasy team points: "))

if points > 800:
    print("Top Performer")
elif 500 <= points <= 800:
    print("Keep Trying")
else:
    print("Needs Improvement")

