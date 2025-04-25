import qrcode

# User se input lena
data = input("Enter the text or link to generate QR Code: ")

# QR code banana
qr_image = qrcode.make(data)

# Save karna
qr_image.save("my_qr_code.png")

print("QR Code saved as 'my_qr_code.png'")
