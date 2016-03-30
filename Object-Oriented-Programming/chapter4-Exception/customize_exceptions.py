# -*- coding: utf-8 -*-

# The exception hierarchy
#                     --- SystemExit
#                     -
# BaseException---------- KeyboardInterrupt
#                     -
#                     --- Exception
#                             -
#                             -
#             Most Other Exception(TypeError, ValueError..)


class EvenOnly(list):

    def append(self, integer):
        """
        overides the append method of list.
        """
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        # super().append(integer) python3
        super(EvenOnly, self).append(integer)


class InvalidWithdrawal(Exception):

    def __init__(self, balance, amount):
        super(InvalidWithdrawal, self).__init__(
            "account doesn't have ${}".format(amount))
        self.amount = amount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance

if __name__ == '__main__':
    # e = EvenOnly()
    # e.append(3)
    # print e
    # handle the InvalidWithdrawal Exception
    try:
        raise InvalidWithdrawal(25, 50)
    except InvalidWithdrawal as e:
        print("I'm sorry, but your withdrawl is more than your"
            "balance by ${}".format(e.overage()))
