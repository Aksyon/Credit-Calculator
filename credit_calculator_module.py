from dataclasses import dataclass


@dataclass
class Credit():
    amount: float
    interest: float
    downpayment: float
    term: int
    total_interest: float = 0


@dataclass
class AnnuityPayment(Credit):

    def get_payment_month(self):    #Total month payment
        return self.amount * (self.interest/100/12 + self.interest/100/12 / ((1 + self.interest/12/100)**self.term*12 - 1))

    def get_total_interest(self):
        for month in range(self.term * 12):
            self.total_interest += self.amount * self.interest / 12 / 100
            self.amount = self.amount - (self.get_payment_month - self.amount * self.interest / 12 / 100)
        return self.total_interest

    def total_amount(self):
        return self.get_payment_month * self.term * 12

        
@dataclass
class DifferentialPayment(Credit):

    def get_payment_month(self):   # Total month payment
        return self.amount / self.term / 12 + self.amount * self.interest / 100 / 12

    def get_total_interest(self):
        debt_month = self.amount / self.term / 12
        total_debt = self.amount
        for month in range (self.term * 12):
            self.total_interest += total_debt * self.interest / 100 / 12
            total_debt -= debt_month
        return self.total_interest

    def get_total_amount(self):
        return self.amount + self.get_total_interest()


if __name__ == '__main__':

    
    