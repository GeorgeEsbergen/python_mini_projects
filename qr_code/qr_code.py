import qrcode


def generate_qr_code(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5
    )
    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black" , back_color="white")
    img.save("qrimg.png")


link=input("Enter Your Link ")

generate_qr_code(link)