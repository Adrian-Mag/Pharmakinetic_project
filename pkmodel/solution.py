#
# Solution class
#
import scipy.integrate
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pylab as plt
from protocol import Protocol

class Solution:
    """A Pharmokinetic (PK) model

    Parameters
    model object
    pprotocol object

    value: numeric, optional
        an example paramter

    """
    def __init__(self, model, protocol):
        t_eval = np.linspace(0, 1, 1000) #model.time
        y0 = np.array([0.0, 0.0]) #model.y0
        args = []
        for key in model: 
            if key != 'name':
                args.append(model[key])
        self.solution = self.__solve(protocol, t_eval, y0, args)
        
    def __solve(self, protocol, t_eval, y0, args):
        def dose(t, X):
            return X
        def __rhs(protocol, t, y, Q_p1, V_c, V_p1, CL, X):
            q_c, q_p1 = y
            transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
            dqc_dt = protocol.dose(X) - q_c / V_c * CL - transition
            dqp1_dt = transition
            return [dqc_dt, dqp1_dt]
    
        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: __rhs(protocol, t, y, *args),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval
        )
        
        return sol
        
    def visualize(self, model):
        """ Plotter of drug presence in body over time

            Input parameters: solve_ivp object holding the solution
            Output: Graphs of drugs content over time 
        """
        plt.plot(self.solution.t, self.solution.y[0, :], label=model['name'] + '- q_c')
        plt.plot(self.solution.t, self.solution.y[1, :], label=model['name'] + '- q_p1')
        plt.legend()
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.show()
        
        
model1_args = {
            'name': 'model1',
            'Q_p1': 1.0,
            'V_c': 1.0,
            'V_p1': 1.0,
            'CL': 1.0,
            'X': 1.0,
            }
model2_args = {
    'name': 'model2',
    'Q_p1': 2.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'X': 1.0,
}
model = model2_args
my_protocol = Protocol()
my_solution = Solution(model, my_protocol)
my_solution.visualize(model)


