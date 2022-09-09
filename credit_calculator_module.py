from Levenshtein import distance
from dataklasses import dataklass

@dataklass
class Credit():
    """Class for creating credit object."""
    amount: float
    interest: float
    downpayment: float = 0
    term: int = 0
    total_interest: float = 0
    CONSTANT_1 = 1200
    CONSTANT_2 = 1
    CONSTANT_3 = 12

    def get_debt(self):     
        return self.amount - self.downpayment
        
    @staticmethod
    def show_payment_info(self):
        return InfoMessage(
            month_payment = self.get_payment_month(),
            total_interest = self.get_total_interest(),
            total_payment = self.total_interest + self.get_debt()
            )

@dataklass
class AnnuityPayment(Credit):
    """Class with logic of calculations for annuity payment."""
    
    def get_payment_month(self):    
        payment_month = (self.get_debt() * 
               (self.interest/self.CONSTANT_1 + self.interest/self.CONSTANT_1/
               ((self.CONSTANT_2 + self.interest/self.CONSTANT_1)**
               (self.term*self.CONSTANT_3) - self.CONSTANT_2)))
        return float('{:.2f}'.format(payment_month))

    def get_total_interest(self):   
        debt_amount = self.get_debt()
        period = 0
        
        while period < self.term * self.CONSTANT_3:
            period += 1
            self.total_interest += (debt_amount*self.interest/self.CONSTANT_1)
            debt_amount = debt_amount - (self.get_payment_month() -
                          debt_amount*self.interest/self.CONSTANT_1)
        return self.total_interest

        
@dataklass
class DifferentialPayment(Credit):
    """Class with logic of calculations for annuity payment."""

    def get_total_interest(self):  
        debt_month = self.get_debt()/self.term/self.CONSTANT_3
        total_debt = self.get_debt()
        period = 0
        while period < self.term*self.CONSTANT_3:
            period += 1
            self.total_interest += total_debt*self.interest/self.CONSTANT_1
            total_debt -= debt_month
        return self.total_interest

    def get_payment_month(self): 
        payments = {}
        debt_month = self.get_debt()/self.term/self.CONSTANT_3
        total_debt = self.get_debt()
        period = 0
        
        while period < self.term * self.CONSTANT_3:
            period += 1
            month_payment = (total_debt*self.interest/
                            self.CONSTANT_1 + debt_month)
            payments[period] = '{:.2f}'.format(month_payment)
            total_debt -= debt_month
        return payments


@dataklass
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
        """Get the message with final calculations."""
        return self.MESSAGE.format(
            month_payment = self.month_payment,
            total_interest = '{:.2f}'.format(self.total_interest),
            total_payment = '{:.2f}'.format(self.total_payment)
            )

def read_data(message):
    """Getting data from user's message."""
    NAMES = ('amount', 'interest', 'downpayment', 'term', 'calculator')
    data_dict = {}
    message_dict = {}
    message_dict.update([part.split(' ') for part in message.split('\n')])
    
    for name in NAMES:
        for key in message_dict.keys():
            result = distance(name, key)
            if result < 5:
                data_dict[name] = message_dict[key]
    return data_dict

def create_credit(data_dict):
    CALCULATOR = {'annuity' : AnnuityPayment,
                  'differential' : DifferentialPayment
    }
    CALCULATOR_NAMES = ('annuity', 'differential')

    try:
        amount = float(data_dict['amount'])
    except ValueError:
        print('Cумма кредита должна быть положительным числом'
              'без кавычек.')
        exit()
    if amount < 0:
        raise Exception ('Сумма кредита не может быть отрицательной.')

    try:
        interest = float(data_dict['interest'])
    except ValueError:
        print('Процент по кредиту должен быть'
              'положительным числом от 0 до 100 без знака %.')
        exit()
    if 0 > interest or interest > 100:
        raise Exception ('Процент по кредиту не может быть отрицательным'
                         'и быть больше 100.')
    
    try:
        downpayment = float(data_dict['downpayment'])
    except ValueError:
        print ('Первоначальный взнос должен быть в виде числа.')
        exit()
    if downpayment < 0:
        raise Exception ('Первоначальный взнос не может быть меньше 0.')
    
    try:
        term = int(data_dict['term'])
    except ValueError:
        print('Срок кредитования должен быть целым числом.')
        exit()
    if term < 0:
        raise Exception ('Срок кредитования не может быть отрицательным.')
    
    for name in CALCULATOR_NAMES:  
        if distance(name, data_dict['calculator']) < 5:
            credit_object = CALCULATOR[name](amount, interest,
                                                       downpayment, term,
                                                       total_interest=0
                                                       )
            break
        else:
            raise Exception('Введите annuity или differential.')
    
    return credit_object
    

def main(credit):
    """Function for creating user message with activity parameters. """
    info = Credit.show_payment_info(credit)
    print(InfoMessage.printing(info))

if __name__ == '__main__':
    message = 'amnt: 1000000\nintresy: 5.5\ndownpament: 20000\ntewm: 7\ncalculator: annuityt.'
    data = read_data(message)
    credit = create_credit(data)
    main(credit)
    
    