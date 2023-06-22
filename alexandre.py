import qrcode

def generate_qrcode(name, job_title, company, email, tel, linkedin, output_path):
    # Create a vCard string with contact information
    vcard = f"BEGIN:VCARD\n" \
            f"VERSION:3.0\n" \
            f"N:{name}\n" \
            f"TITLE:{job_title}\n" \
            f"ORG:{company}\n" \
            f"TEL;TYPE=CELL:{tel}\n" \
            f"EMAIL;TYPE=INTERNET:{email}\n" \
            f"URL;TYPE=LINKEDIN:{linkedin}\n" \
            f"END:VCARD"

    # Generate QR code for the vCard
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(vcard)
    qr.make(fit=True)

    # Create and save the QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)

# Example usage
name = "Alexandre Schinazi"
job_title = "Partner and Technical Director"
company = "Mitsidi"
email = "alexandre@mitsidi.com"
tel = "+55-11-940441864"
linkedin = "https://www.linkedin.com/in/alexandre-schinazi/"
output_path = "./files/qrcode.png"

generate_qrcode(name, job_title, company, email, tel, linkedin, output_path)
