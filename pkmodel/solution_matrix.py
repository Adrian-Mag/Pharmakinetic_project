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
        self.solution = self.__solve(model, protocol)
        
    def __matrix(self, model):
        no_of_unknowns = model.peripherals + model.subcutaneous + 1
        matrix = np.zeros((no_of_unknowns, no_of_unknowns))
        matrix[0, 0] = -1*(model.CL + np.sum(model.Qp))/model.Vc
        if model.peripherals == 0:
            for i in range(1, no_of_unknowns):
                matrix[i, i] = -model.Qp[i]/model.Vp[i]
                matrix[1, i] = model.Qp[i]/model.Vp[i]
                matrix[i, 1] = model.Qp[i]/model.Vc
        else:
            matrix[0, 1] = model.ka
            matrix[1, 1] = -model.ka
            for i in range(2, no_of_unknowns):
                matrix[i, i] = -model.Qp[i]/model.Vp[i]
                matrix[1, i] = model.Qp[i]/model.Vp[i]
                matrix[i, 1] = model.Qp[i]/model.Vc
        return matrix
    
    def __dose_vector(self, model, protocol, t):
        dose = np.zeros((model.peripherals + model.sub_cutaneous + 1, 1))
        if model.sub_cutaneous == 1:
            dose[0] = protocol.dose()
        else:
            dose[1] = protocol.dose(t)
        return dose
    
    def __solve(self, model, protocol):
        propagator_matrix = self.__matrix(model)
        q = np.zeros((model.peripherals + model.sub_cutaneous + 1, len(model.time)))
        dt = model.time[1] - model.time[0]
        for index, _ in enumerate(model.time):
            D = self.__dose_vector(model, protocol, index)
            q[:, index+1] = q[:, index] + dt*(propagator_matrix*q[:, index] + D)
        return q