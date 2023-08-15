import qrcode

info = input ("enter your name and phone number: ")

img = qrcode.make (info)
img.save ("name & phone qrcode.png")