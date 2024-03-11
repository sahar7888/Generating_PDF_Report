
""" Genarting the bill report in pdf"""

import webbrowser
import os
from fpdf import FPDF


class PDFReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format="A4")
        pdf.add_page()
        pdf.image("files/house.png", w=50, h=50) # customizing the report by adding an image to the report

        #insert title
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align="C", ln=1)

        # insert period
        pdf.cell(w=100, h=40, txt='Period:', border=0, align="C")
        pdf.cell(w=200, h=40, txt=bill.period, border=0, align="C", ln=1)

        #insert names
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0, align="C")
        pdf.cell(w=200, h=40, txt=str(round(flatmate1.Pay(bill=bill,Flatmate2_days= flatmate2.days_in),2)), border=0, align="C", ln=1)
#

        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0, align="C")
        pdf.cell(w=200, h=40, txt=str(round(flatmate2.Pay(bill=bill, Flatmate2_days=flatmate1.days_in),2)), border=0, align="C", ln=1)

        os.chdir("files") # Saving the report in this directory
        pdf.output(self.filename)
        webbrowser.open(self.filename)
