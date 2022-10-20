#
# Protocol class
#

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    dosing: str, optional
        'const' or 'inst'

        Specifies the dosing protocol. 'const' specifies a
        steady application of <amount> ng/h. 'inst' specifies
        instantaneous doses of <amount> ng at intervals of
        <interval> time steps
    amount: float, optional
        If dosing='const': ng/h of drug steadily applied
        If dosing='inst': ng of drug added every <interval>
        time steps
    interval: int, optional
        Time steps between dose applications

        Ignored if dosing='const'

    """
    def __init__(self,
                 dosing: str = 'const',
                 amount: float = 10.0,
                 interval: int = None):
        self.dosing = dosing
        self.amount = amount
        self.interval = interval
