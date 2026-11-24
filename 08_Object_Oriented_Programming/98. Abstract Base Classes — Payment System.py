# Objective: Design an abstract payment interface and implement multiple concrete payment methods using Python's abc module.
# Requirements
# 1. Create an abstract base class called Payment.
#    - It should define an abstract method called process_payment(amount).
#    - The method should raise no implementation itself; subclasses must provide their own implementation.
# 2. Create three concrete payment classes:
#    - CreditCardPayment
#    - PayPalPayment
#    - BankTransferPayment
# 3. Each concrete class must:
#    - Inherit from Payment.
#    - Implement process_payment(amount).
#    - Display a message indicating that the payment was processed and identify the payment method and amount.
# 4. Create instances of all three payment classes and process payments using them.

from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def process_payment(self):
        pass

class CreditCardPayment(Payment):
    def process_payment(self):
        print(f'Processing ${self.amount:.2f} through Credit Card...')
        print('Credit Card payment successful!')
        print()

class PayPalPayment(Payment):
    def process_payment(self):
        print(f'Processing ${self.amount:.2f} through PayPal...')
        print('PayPal payment successful!')
        print()

class BankTransferPayment(Payment):
    def process_payment(self):
        print(f'Processing ${self.amount:.2f} through Bank Transfer...')
        print('Bank Transfer payment successful!')
        print()

# p1 = CreditCardPayment(100)
# p2 = PayPalPayment(75)
# p3 = BankTransferPayment(200)
#
# p1.process_payment()
# p2.process_payment()
# p3.process_payment()

p_list = [CreditCardPayment(100), PayPalPayment(75), BankTransferPayment(200)]

for p in p_list:
    p.process_payment()