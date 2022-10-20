#
# Protocol class
#

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    interval: int, optional
        Time steps between dose applications,
        if using instantaneous dosing

        Default is None, meaning steady application
        of a dose of <amount> ng/h
        Specify if using instantaneous dosing,
        meaning an instantaneous application
        of <amount> ng every <interval> time steps

    amount: float, optional
        If interval == None: ng/h of drug steadily applied
        If interval != None: ng of drug added every <interval>
        time steps

        Default is 10.0 ng/h OR 10.0 ng every
        <interval> time steps

    """
    def __init__(self,
                 interval: int = None,
                 amount: float = 10.0):
        self.interval = interval
        self.amount = amount
