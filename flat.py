class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    def __init__(self, name, days_in):
        self.name = name
        self.days_in = days_in

    def Pay(self, bill, Flatmate2_days):
        weight = self.days_in / (self.days_in + Flatmate2_days)
        return bill.amount * weight
