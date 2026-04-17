#brew install pipx
#cd /Applications/XAMPP/xamppfiles/htdocs/HJTNUMBERTHEORY/Module1
#/opt/homebrew/bin/python3 -m venv venv
#source venv/bin/activate
#python -m pip install "qrcode[pil]"
import qrcode

# Inputs
first = input("Enter First Name: ")
mi = input("Enter Middle Initial: ")
last = input("Enter Last Name: ")
student_id = int(input("Enter numeric student ID: "))
section = input("Enter section: ")
phone = input("Enter phone number: ")
email = input("Enter email: ")
address = input("Enter address: ")

# Fermat-style encoding
p = 13
encoded = pow(student_id, p-1, p)

# VCARD format (complete)
data = f"""BEGIN:VCARD
VERSION:3.0
N:{last};{first};{mi};;
FN:{first} {mi}. {last}
ORG:{section}
TEL;TYPE=CELL:{phone}
EMAIL;TYPE=INTERNET:{email}
ADR:;;{address};;;;
NOTE:Encoded ID {encoded}
END:VCARD"""

# Generate QR
qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("student_qr.png")

print("\nQR code generated!")
print("Scan it to view full contact details.")
print(data)