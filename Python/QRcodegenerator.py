# # You can visit https://pypi.org/project/qrcode/#description
# # For checking the documentation

import qrcode
qr = qrcode.QRCode(
         version=1,
          error_correction=qrcode.constants.ERROR_CORRECT_L,
          box_size=10,
        border=4,
 )
ad=input("Enter what you wanted to get in QR code scan")
qr.add_data(ad)
qr.make(fit=True)
kd=qr.make_image(fill_color="black", back_color="white")
kd.save("Generated Qr_code.png")
