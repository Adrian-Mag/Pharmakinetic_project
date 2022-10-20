#
# Model class
#
class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------
    Required:
    V_c: Volume of the central compartment in mL
    CL: The clearance/elimination rate from the central compartment in mL/h

    Optional:
    K_a: Absorption rate for the subcutaneous dosing per hour
    Q_p1: Transition rate between central compartment and peripheral
    compartment 1 in mL/h
    V_p1: Volume of peripheral compartment 1 in mL
    Q_p2: Transition rate between central compartment and peripheral
    compartment 2 in mL/h
    V_p2: Volume of peripheral compartment 2 in mL

    """
    def __init__(self, V_c, CL, K_a=None, Q_p1=None, V_p1=None, Q_p2=None,
                 V_p2=None):
        self.V_c = V_c
        self.CL = CL
        self.opt_params = [K_a, Q_p1, V_p1, Q_p2, V_p2]

    def construct_param_dict(self):
        # Construct a dictionary of the model parameters.
        param_dict = {
            'V_c': self.V_c,
            'CL': self.CL
        }
        # Add any optional parameters to the dictionary
        i = 2  # i starts at 2 so that it doesn't overwrite V_c and CL
        optional_param_name_list = ['K_a', 'Q_p1', 'V_p1', 'Q_p2', 'V_p2']
        for param in self.opt_params:
            if param is not None:
                param_dict[optional_param_name_list[i]] = param
                i += 1
        return param_dict
