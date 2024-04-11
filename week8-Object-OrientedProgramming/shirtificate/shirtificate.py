from fpdf import FPDF
from PIL import Image


user_name = input("Enter name: ")

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "", 36)
        self.cell(80)
        self.cell(30, 40, "CS50 Shirtificate", align="C")
        self.ln(20)

    def add_centered_image(self, image_path):
        self.image(image_path, x='C', y=60, w=190, h=0, keep_aspect_ratio=False)

    def set_user_name(self, user_name):

        self.set_font("helvetica", "", 24)

        self.set_text_color(255, 255, 255)

        self.cell(80)

        self.cell(30, 190, f"{user_name} took CS50", align="C")

pdf = PDF(orientation="P", unit="mm", format="A4")

pdf.add_page()

image_path = 'shirtificate.png'
# Add the centered image to the PDF
pdf.add_centered_image(image_path)

pdf.set_user_name(user_name)

pdf.output("shirtificate.pdf")

