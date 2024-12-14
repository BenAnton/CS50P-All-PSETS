from fpdf import FPDF


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")

image_width = 156.63333333
page_width = 210

x_pos = (page_width - image_width) / 2

pdf.image("shirtificate.png", x=x_pos, y=50, w=image_width)


name = input("Please enter name: ")
output = f"{name} took CS50"
pdf.set_font("helvetica", "B", 24)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 160, output, 0, 1, "C")


output_path = "shirtificate.pdf"
pdf.output(output_path)
