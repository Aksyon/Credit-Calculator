from dataclasses import dataclass


@dataclass
class Credit():
    """Class for creating credit object."""
    amount: float
    interest: float
    downpayment: float = 0
    term: int = 0
    total_interest: float = 0
    
    def get_debt(self):     #Total debt for refunding
        return self.amount - self.downpayment
        
    @staticmethod
    def show_payment_info(self):
        return InfoMessage(
            month_payment = self.get_payment_month(),
            total_interest = self.get_total_interest(),
            total_payment = self.total_interest + self.get_debt()
        )

@dataclass
class AnnuityPayment(Credit):
    """Class with logic of calculations for annuity payment."""

    def get_payment_month(self):    #Total month payment for credit
        return self.get_debt() * (self.interest/100/12 + self.interest/100/12/
            ((1 + self.interest/12/100)**(self.term*12) - 1))

    def get_total_interest(self):   # Total credit overpayment.
        debt_amount = self.get_debt()
        period = 0
        
        while period < self.term * 12:
            period += 1
            self.total_interest += (debt_amount * self.interest / 12 / 100)
            debt_amount = debt_amount - (self.get_payment_month() -
                          debt_amount * self.interest / 12 / 100)
        return self.total_interest

        
@dataclass
class DifferentialPayment(Credit):
    """Class with logic of calculations for annuity payment."""

    def get_total_interest(self):   # Total credit overpayment.
        debt_month = self.get_debt() / self.term / 12
        total_debt = self.get_debt()
        period = 0
        while period < self.term * 12:
            period += 1
            self.total_interest += total_debt * self.interest / 100 / 12
            total_debt -= debt_month
        return self.total_interest

    def get_payment_month(self):  # Total month payment for credit. Return
                                  # dictionary with payments for whole period.
        payments = {}
        debt_month = self.get_debt() / self.term / 12
        total_debt = self.get_debt()
        period = 0
        
        while period < self.term * 12:
            period += 1
            month_payment = total_debt * self.interest / 100 / 12 + debt_month
            payments[period] = '%.2f' % month_payment
            total_debt -= debt_month
        return payments


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
    def printing(self):   #Get the message with final calculations
        return self.MESSAGE.format(
            month_payment = self.month_payment,
            total_interest = '%.2f' % self.total_interest,
            total_payment = '%.2f' % self.total_payment
            )

def create_credit():
    CALCULATOR = {'ANUIT':AnnuityPayment,
                  'DIFF':DifferentialPayment
    }
    
    try:
        amount = float(input('amount: '))
    except ValueError:
        print('Необходимо ввести сумму кредита в виде положительного числа.')
        exit()
    if amount < 0:
        raise Exception ('Сумма кредита не может быть отрицательной.')

    try:
        interest = float(input('interest: '))
    except ValueError:
        print('Необходимо ввести процент по кредиту в виде положительного числа от 0 до 100.')
        exit()
    if 0 > interest or interest > 100:
        raise Exception ('Процент по кредиту не может быть отрицательным и быть больше 100.')

    try:
        downpayment = float(input('downpayment: '))
    except ValueError:
        print ('Первоначальный взнос должен быть в виде числа.')
        exit()
    if downpayment < 0:
        raise Exception ('Первоначальный взнос не может быть меньше 0.')
    
    try:
        term = int(input('term: '))
    except ValueError:
        print('Срок кредитования должен быть введен в виде целого числа.')
        exit()
    if term < 0:
        raise Exception ('Срок кредитования не может быть отрицательным.')
        
    calculator  = input('ANUIT - annuity payment,'
                        'DIFF - differential payment: ')
    
    try:
        credit_object = CALCULATOR[calculator](amount, interest,
                                               downpayment, term
                                               )
    except KeyError:
        raise KeyError(f'Вы ввели не поддерживаемый кредитный калькулятор: '
                       f'{calculator}')
    return credit_object
    
def main(credit):
    """Function for creating user message with activity parameters. """
    info = Credit.show_payment_info(credit)
    print(InfoMessage.printing(info))

if __name__ == '__main__':
    credit = create_credit()
    main(credit)
    
    