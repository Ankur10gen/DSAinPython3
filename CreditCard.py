class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance
        
        Initial Balance:ZERO
        """
        self._customer = customer
        self._bank =bank
        self._account = acnt
        self._limit = limit
        self._liability = 0

    def get_customer(self):
        """Return: Name of customer"""
        return self._account

    def get_bank(self):
        """Return: Bank name"""
        return self._bank

    def get_limit(self):
        """Return: Current credit limit"""
        return self._limit

    def get_account(self):
        """Return: card identifying number"""
        return self._account

    def get_liability(self):
        """Return: current balance"""
        return self._liability

    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient credit limit
        Return: True if processed; False otherwise
        """
        if price + self._liability > self._limit:
            return False
        else:
            self._liability += price
            return True

    def make_payment(self,amount):
        """Process customer payment : Reduce Balance"""
        self._liability -= amount