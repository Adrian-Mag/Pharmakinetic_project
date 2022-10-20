#
# Solution class
#
import scipy.integrate
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pylab as plt
from protocol import Protocol
from model import Model

class Solution:
    """A Pharmokinetic (PK) model

    Parameters
    model object
    pprotocol object

    value: numeric, optional
        an example paramter

    """
    def __init__(self, model, protocol):
        self.solution = self.__solve(model, protocol)
    
    def __matrix(self, model):
        print(model.Qp, model.Vp)
        no_of_unknowns = model.peripherals + model.subcutaneous + 1
        matrix = np.zeros((no_of_unknowns, no_of_unknowns))
        matrix[0, 0] = -1*(model.CL + np.sum(model.Qp))/model.Vc
        if model.subcutaneous == 0:
            for i in range(1, no_of_unknowns):
                matrix[i, i] = -model.Qp[i-1]/model.Vp[i-1]
                matrix[0, i] = model.Qp[i-1]/model.Vp[i-1]
                matrix[i, 0] = model.Qp[i-1]/model.Vc
        else:
            matrix[0, 1] = model.ka
            matrix[1, 1] = -model.ka
            for i in range(2, no_of_unknowns):
                matrix[i, i] = -model.Qp[i-2]/model.Vp[i-2]
                matrix[0, i] = model.Qp[i-2]/model.Vp[i-2]
                matrix[i, 0] = model.Qp[i-2]/model.Vc
        return matrix
    
    def __dose_vector(self, model, protocol, t):
        dose = np.zeros(model.peripherals + model.subcutaneous + 1)
        if model.subcutaneous == 0:
            dose[0] = protocol.dose()
        else:
            dose[1] = protocol.dose()
        return dose
    
    def __solve(self, model, protocol):
        
        def __rhs(model, protocol, matrix, t, y):
            dq = np.matmul(matrix, y) + self.__dose_vector(model, protocol, t)
            return dq
        
        # Create time domain
        time  = np.linspace(0, 1, 1000)
        # Find number of unknowns to be solved for 
        no_of_unknowns = model.peripherals + model.subcutaneous + 1
        # Build model matrix
        matrix = self.__matrix(model)
        print(matrix)
        # Build initial conditions
        y0 = np.zeros(no_of_unknowns)
        
        # Integrate IVP over all time and save solution
        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: __rhs(model, protocol, matrix, t, y),
            t_span=[time[0], time[-1]],
            y0=y0, t_eval=time
        )
        
        
        return sol
        
    def visualize(self, model):
        """ Plotter of drug presence in body over time

            Input parameters: solve_ivp object holding the solution
            Output: Graphs of drugs content over time 
        """
        plt.plot(self.solution.t, self.solution.y[0, :], label=model.name + 'qc')
        for i in range(model.peripherals + model.subcutaneous + 1):
            plt.plot(self.solution.t, self.solution.y[i, :], label=model.name)
        plt.legend()
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.show()
        
        
model1_args = {
            'name': 'model1',
            'CL': 1.0,
            'V_c': 1.0,
            'Q_p1': 1.0,
            'V_p1': 1.0,
            }

model2_args = {
            'name': 'model2',
            'CL': 1.0,
            'V_c': 1.0,
            }

model3_args = {
            'name': 'model3',
            'CL': 1.0,
            'Vc': 1.0,
            'ka': 1,
            'Qp1': 1.0,
            'Vp1': 1.0,
            'Qp2': 1.0,
            'Vp2': 2.0,
            'Qp3': 4.0,
            'Vp3': 1.0
            }


model = Model(model3_args)
my_protocol = Protocol(1)
my_solution = Solution(model, my_protocol)
my_solution.visualize(model)


