from dataclasses import dataclass


@dataclass
class Credit():
    amount: float
    interest: float
    downpayment: float
    term: int


@dataclass
class AnnuityPayment(Credit):

    def get_payment_month(self):
        return self.amount * (self.interest/100/12 + self.interest/100/12 / ((1 + self.interest/12/100)**self.term*12 - 1))

    def get_interest_amount(self):
        for month in range(self.term * 12):
            interest_amount = self.amount * self.interest / 12 / 100
            self.amount = self.amount - (self.get_payment_month - interest_amount)
            print(f'В {month} месяц проценты по кредиту составят {interest_amount} рублей.') 

    def total_amount(self):
        return self.get_payment_month * self.term * 12

        

class DifferentialPayment(Credit):

    def get_payment_month(self):
        