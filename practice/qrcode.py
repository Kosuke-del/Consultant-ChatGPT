"""This is a test program."""
import qrcode

# QRコードにエンコードする文字列を指定する
DATA = "KosukeANDO"

# QRコードを生成する
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(DATA)
qr.make(fit=True)
IMG = qr.make_image(fill_color="black", back_color="white")

# QRコードをPNGファイルとして保存する
IMG.save("qrcode.png")
