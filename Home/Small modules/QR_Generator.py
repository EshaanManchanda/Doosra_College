import qrcode

img = qrcode.make("https://www.youtube.com/c/TechLovev_212subs")
img.save("Techlovev_qr.jpg")
