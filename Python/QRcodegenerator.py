# You can visit https://pypi.org/project/qrcode/#description
# For checking the documentation

import qrcode
kd=qrcode.make("You can visit https://pypi.org/project/qrcode/#description"
                "import qrcode"
                "For checking the documentation"
                "kd=qrcode.make('')"
                "type(kd)"
                "kd.save(Generated Qr_code.png)")
type(kd)
kd.save("Generated Qr_code.png")