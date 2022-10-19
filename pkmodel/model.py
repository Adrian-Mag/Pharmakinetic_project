#
# Model class
#

# from numpy import NaN


class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, V_c, CL, K_a=None, Q_p1=None, Q_p2=None, V_p1=None,
                 V_p2=None):
        self.V_c = V_c
        self.CL = CL
        self.K_a = K_a
        self.Q_p1 = Q_p1
        self.Q_p2 = Q_p2
        self.V_p1 = V_p1
        self.V_p2 = V_p2
        self.opt_params = [K_a, Q_p1, Q_p2, V_p1, V_p2]

    def construct_param_dict(self):
        # Construct a dictionary of the model parameters.
        param_dict = {
            'V_c': self.V_c,
            'CL': self.CL
        }
        # Add any optional parameters to the dictionary
        i = 0
        optional_param_name_list = ['K_a', 'Q_p1', 'Q_p2', 'V_p1', 'V_p2']
        for param in self.opt_params:
            if param is not None:
                param_dict[optional_param_name_list[i]] = param
                i += 1
    # def rhs(t, y, Q_p1, V_c, V_p1, CL, X):
    #     q_c, q_p1 = y
    #     transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    #     dqc_dt = dose(t, X) - q_c / V_c * CL - transition
    #     dqp1_dt = transition
    #     return [dqc_dt, dqp1_dt]
