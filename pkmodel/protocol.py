#
# Protocol class
#

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self,
                 amount: float = 10.0,
                 interval: int = None
                 ):
        self.amount = amount
        self.interval = interval
        
    def dose(self):
        if self.interval is None:
            return self.amount
        else:
            return 0

