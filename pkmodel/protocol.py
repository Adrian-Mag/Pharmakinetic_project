#
# Protocol class
#

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    amount: float, optional
        If interval == None: ng/h of drug steadily applied
        If interval != None: ng of drug added every <interval>
        time steps

        Default is 10.0 ng/h OR 10.0 ng every
        <interval> time steps

    interval: int, optional
        Time steps between dose applications,
        if using instantaneous dosing

        Default is None, meaning steady application
        of a dose of <amount> ng/h
        Specify if using instantaneous dosing,
        meaning an instantaneous application
        of <amount> ng every <interval> time steps
    """
    def __init__(self,
                 amount: float = 10.0,
                 interval: int = None
                 ):
        self.amount = amount
        self.interval = interval

    def dose(self):
        """The dose as a function of time

        Returns
        -------

        dose: float
            If using constant dosing (self.interval == None),
            returns the dose amount in ng/hr

            If using instantaneous dosing (self.interval != None),
            returns 0
            In the Solution() class, an instantaneous dose of
            self.amount will be added to the 1st compartent (either
            central or the dosing compartment) every self.interval
        """
        if self.interval is None:
            return self.amount
        else:
            return 0
