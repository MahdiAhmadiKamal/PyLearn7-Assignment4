import instaloader
import getpass

# reading previous followers list
f = open ("followers.txt", "r")
old_followers = []
for line in f:
    old_followers.append(line)
f.close

# connecting to the Instagram
L = instaloader.Instaloader ()

username = input("enter username: ")
password = getpass.getpass ("enter password: ")

L.login (username, password)
print ("hooora!!! successfully logged in")

# going to somebody's profile
profile = instaloader.Profile.from_username (L.context, "sajjad_aemmi")

# somebody's new followers
new_followers = []
for follower in profile.get_followers():
    new_followers.append (follower)

# looking for those who have recently followed that person
for new_follower in new_followers:
    if new_follower not in old_followers:
        print (new_follower)

# updating the followers list
f = open ("followers.txt", "w")
for follower in new_followers:
    f.write (follower + "\n")

f.close()