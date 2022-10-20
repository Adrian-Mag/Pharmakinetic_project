"""     Parameters
    ----------
    Required:
    Vc (float): Volume of the central compartment in mL
    CL (float): The clearance/elimination rate from the central compartment in
    mL/h
	@@ -27,26 +27,33 @@ class Model:
    Subcutaneous (int): the number of subcutaneous dosing compartments in the
    model
 """
def __init__(self, Vc, CL, K_a=None, Q_p1=None, V_p1=None, Q_p2=None,
                 V_p2=None):
        self.Vc = Vc
        self.CL = CL
        self.opt_params = [K_a, Q_p1, V_p1, Q_p2, V_p2]
        self.Qp = []
        self.Vp = []
        if Q_p2 is not None:
            self.peripherals = 2
            self.Qp.append(Q_p1, Q_p2)
            self.Vp.append(V_p1, V_p2)
        elif Q_p1 is not None:
            self.peripherals = 1
            self.Qp.append(Q_p1)
            self.Vp.append(V_p1)
        else:
            self.peripherals = 0
        if K_a is None:
            self.subcutaneous = 0
            self.K_a = K_a
        else:
            self.subcutaneous = 1

    def construct_param_dict(self):
        # Construct a dictionary of the model parameters.
        param_dict = {
            'V_c': self.Vc,
            'CL': self.CL
        }
        # Add any optional parameters to the dictionary