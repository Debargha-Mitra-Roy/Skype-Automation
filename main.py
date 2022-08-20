from skpy import Skype
import os.path
import random
import string


# User-ID & Password
email_id = input("Enter your Email ID : ")
password = input("Enter your Password : ")


# Login
slogin = Skype(email_id, password)


# Information about all contacts
contact = slogin.contacts
for i in contact:
    print(i + "\n")


# Message to a sender
sender = input("Enter the sender's Email-ID : ")
message = input("Enter the message that you wanted to send :\n")
message_to_sender = slogin.contacts[sender]
contact.chat.sendMsg(message)


# Group create
members = input("Enter the member(s) username(s) that you wanted to invite in your group :\n")
members_list = members.split()
# print("Members List : ", members_list)
group = slogin.chats.create(members_list)


# Send an image
user_image = input("Enter the user name : ")
image_path = input("Enter the image path : ")
ch = slogin.contacts[user_image]
# Give the image a random name
# initializing size of string
N = 7
# using random.choices() generating random strings
res = ''.join(random.choices(string.ascii_letters, k=N))
# Convert the string to a .png extention
res = res + ".png"
with open(image_path, "rb") as f:
    contact.chat.sendFile(f, res, image=True)
