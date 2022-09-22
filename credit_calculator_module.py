from Levenshtein import distance
from dataklasses import dataklass
import logging

logging.basicConfig(filename='credit_logs.log', filemode='w',
                    format='%(asctime)s %(levelname)s %(message)s')


@dataklass
class Credit():
    """Class for creating credit object."""
    amount: float
    interest: float
    downpayment: float = 0
    term: int = 0
    total_interest: float
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
    LEVENSHTEIN_DISTANCE = 5
    data_dict = {}
    message_dict = {}
    message_dict.update([part.split(' ') for part in message.split('\n')])
    
    for name in NAMES:
        for key in message_dict.keys():
            result = distance(name, key)
            if result < LEVENSHTEIN_DISTANCE:
                data_dict[name] = message_dict[key]
    
    if len(data_dict)<5:
        logging.error('One or more parapeters not recognized. '
                      f'check:\n{message}')
        raise Exception

    return data_dict

def create_credit(data_dict):
    CALCULATOR = {'annuity' : AnnuityPayment,
                  'differential' : DifferentialPayment
    }
    CALCULATOR_NAMES = ('annuity', 'differential')
    LEVENSHTEIN_DISTANCE = 5

    try:
        amount = float(data_dict['amount'])
    except ValueError:
        logging.error('Amount must be a positive number'
              'without quotes.', exc_info=True)
        exit()
    if amount < 0:
        logging.error ('Amount can not be a negative number.')
        raise Exception

    try:
        interest = float(data_dict['interest'])
    except ValueError:
        logging.error('Interest must be in the range from 0 to 100 without %.',
                      exc_info=True)
        exit()
    if 0 > interest or interest > 100:
        logging.error('Interest can not be out of range 0-100.')
        raise Exception
    
    try:
        downpayment = float(data_dict['downpayment'])
    except ValueError:
        logging.error('Downpayment must be a number.', exc_info=True)
        exit()
    if downpayment < 0:
        logging.error('Downpayment can not be less then 0.')
        raise Exception
    
    try:
        term = int(data_dict['term'])
    except ValueError:
        logging.error('Term must be an integer.')
        exit()
    if term < 0:
        logging.error('Term can not be a negative number.')
        raise Exception
    
    for name in CALCULATOR_NAMES:  
        if distance(name, data_dict['calculator']) < LEVENSHTEIN_DISTANCE:
            credit_object = CALCULATOR[name](amount, interest,
                                                       downpayment, term,
                                                       total_interest=0
                                                       )
            break
        else:
            logging.error('Input <annuity> or <differential>.')
            raise Exception
    return credit_object
    

def main(credit):
    """Function for creating user message with activity parameters. """
    info = Credit.show_payment_info(credit)
    print(InfoMessage.printing(info))

if __name__ == '__main__':
    message = 'amnt: 1000000\ninterest: 5.5\ndownpament: -20000\nterm: 7\ncalculator: annuityt.'
    data = read_data(message)
    credit = create_credit(data)
    main(credit)