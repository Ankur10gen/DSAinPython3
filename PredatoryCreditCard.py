from CreditCard import CreditCard
class PredatoryCreditCard(CreditCard):
    """Extension to existing CreditCard class"""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Init method for PredatoryCreditCard class"""

        super().__init__(customer, bank, acnt, limit)
        """Init method for CreditCard class"""
        self._apr = apr # Initialise apr

    def charge(self,price): # Charge price on the given card

        success = super().charge(price) # Call charge() from super class (CreditCard class)

        if not success: # In case of failure, charge the customer for $5 liability
            self._liability += 5
            return success

    def process_month(self): # Process monthly interest

        if self._liability > 0:
            monthly_factor = pow(1+self._apr,1/12)
            self._liability *= monthly_factor
