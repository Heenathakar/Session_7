#Write a Python script that takes your current Spotify listening time in minutes and checks if it is above 120 minutes; if yes, print 'You are a true music #fan!', otherwise print 'Keep listening!'.


n=int(input("enter your current Spotify listening time:"))

if n>=120:
    print("You are a true music fan!")
else:
    print("Keep listening!")