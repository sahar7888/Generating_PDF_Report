from flat import Bill, Flatmate
from pdfreport import PDFReport

bill_amount = float(input("what is the bill amount?"))
period = input("what is the period of bill?")
name1= input("What is your name?")
days_in_1 = int(input(f"how many days {name1} stayed in the house?"))

name2= input("What is your flatmate's name?")
days_in_2 = int(input(f"how many days {name2} stayed in the house?"))


flatmate1= Flatmate(name1, days_in_1)
flatmate2= Flatmate(name2, days_in_2)
The_bill = Bill(bill_amount, period)
pdf_report = PDFReport(filename=f"{period}.pdf")

pdf_report.generate(flatmate1, flatmate2, bill= The_bill)




name1_rent = flatmate1.Pay(bill=The_bill, Flatmate2_days=flatmate2.days_in)
name2_rent = flatmate2.Pay(bill=The_bill, Flatmate2_days=flatmate1.days_in)

print(f"{name1} pays: {name1_rent}")
print(f"{name2} pays: {name2_rent}")



