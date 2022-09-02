from dataclasses import dataclass


@dataclass
class Credit():
    amount: float
    interest: float
    downpayment: float
    term: int
    total_interest: float = 0

    @staticmethod
    def show_payment_info(self):
        return InfoMessage(
            month_payment = self.get_payment_month(),
            total_interest = self.get_total_interest(),
            total_payment = self.get_total_amount()
        )

@dataclass
class AnnuityPayment(Credit):

    def get_payment_month(self):    #Total month payment
        return self.amount * (self.interest/100/12 + self.interest/100/12 /
            ((1 + self.interest/12/100)**self.term*12 - 1))

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
            #self.term * 12 - 1
        return self.total_interest

    def get_total_amount(self):
        return self.amount + self.get_total_interest()

@dataclass
class InfoMessage():
    """Class describe info object."""
    MESSAGE = ('Ежемесячный платеж по кредиту: {month_payment} руб.; '
               'Общая сумма процентов по кредиту: {total_interest} руб.; '
               'Общая сумма выплаты: {total_payment} руб.'
               )

    month_payment: float = None
    total_interest: float = None
    total_payment: float = None

    @staticmethod
    def printing(self):
        return self.MESSAGE.format(
            month_payment = '%.2f' % self.month_payment,
            total_interest = '%.2f' % self.total_interest,
            total_payment = '%.2f' % self.total_payment
            )

def create_credit():
    CALCULATOR = {'ANUIT':AnnuityPayment,
                  'DIFF':DifferentialPayment
    }
    
    amount = float(input('amount: '))
    interest = float(input('interest: '))
    downpayment = float(input('downpayment: '))
    term = int(input('term: '))
    calculator  = input('ANUIT - annuity payment, DIFF - differential payment: ')
    
    try:
        credit_object = CALCULATOR[calculator](amount, interest, downpayment, term)
    except KeyError:
        raise KeyError(f'Вы ввели не поддерживаемый кредитный калькулятор: {calculator}')
    return credit_object
    
def main(credit):
    """Function for creating user message with activity parameters. """
    info = Credit.show_payment_info(credit)
    print(InfoMessage.printing(info))

if __name__ == '__main__':
    credit = create_credit()
    main(credit)
    
    