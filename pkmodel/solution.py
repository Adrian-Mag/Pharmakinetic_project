#
# Solution class
#
import scipy.integrate
import numpy as np
import matplotlib
import matplotlib.pylab as plt
matplotlib.use('TkAgg')


class Solution:
    """A Pharmokinetic (PK) solution model
    ------------
    INPUTS
    model object
    protocol object

    This class creates solution objects that contain the time interval,
    and the drug quantities in the central compartiment, the peripheral
    compartiments and the subcutaneous compartiment (if present). The
    solution can be visualized by calling the "visualization" method.

    The general system of equations governing the Pk model can be written
    as:
            dq/dt = A*q + D
    where q is a vector that holds all the unknowns in the following format:
    q = [qc q0 qp1 qp2 qp3 ...]
    A is a matrix that encapsulates the coupling between unknowns, and D
    is a vector of the form:
    D = [dose(t) 0 0 0 ...]

    Output:
    Solution object

    """
    def __init__(self, model, protocol):
        """ The solution is  automatically computed
        upon creation of solution object"""

        self.solution = self.__solve(model, protocol)
        self.name = model.name
        # The next two attributes are needed for automatically
        # building plots
        self.subcutaneous = model.subcutaneous
        self.peripherals = model.peripherals

    def __matrix(self, model):
        """ Matrix generator
        INPUTS: model object
        OUTPUTS: ODE system matrix

        This function generates a matrix that describes the linear
        system of equations. It uses the attributes of the model to
        create matrices for models with or without subcutaneous
        compartiments and peripherals."""

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
        """ Dosage Vectorization
        This function creates a numpy array that holds the
        dosage term in the form:
        D = [dose(t) 0 0 0 ...]
        """
        print(t)
        dose = np.zeros(model.peripherals + model.subcutaneous + 1)
        if model.subcutaneous == 0:
            dose[0] = protocol.value(t)
        else:
            dose[1] = protocol.value(t)
        return dose

    def __solve(self, model, protocol):
        """ This method integrates the IVP ODE system and returns the
        solution."""

        def __rhs(model, protocol, matrix, t, y):
            dq = np.matmul(matrix, y) + self.__dose_vector(model, protocol, t)
            return dq

        # Find number of unknowns to be solved for
        no_of_unknowns = model.peripherals + model.subcutaneous + 1
        # Build model matrix
        matrix = self.__matrix(model)
        # Build initial conditions
        y0 = np.zeros(no_of_unknowns)
        # Integrate IVP over all time and save solution
        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: __rhs(model, protocol, matrix, t, y),
            t_span=[protocol.time[0], protocol.time[-1]],
            y0=y0, t_eval=protocol.time, method='DOP853',
            max_step=0.01, atol=1, rtol=1
        )
        return sol

    def visualize(self):
        """ Plotter of drug presence in body over time

            Input parameters: solve_ivp object holding the solution
            Output: Graphs of drugs content over time
        """
        plt.figure('Model ' + self.name)
        plt.plot(self.solution.t, self.solution.y[0, :],
                 label=self.name + ' qc')
        if self.subcutaneous == 1:
            plt.plot(self.solution.t, self.solution.y[1, :],
                     label=self.name + ' q0')
            for i in range(self.peripherals):
                plt.plot(self.solution.t, self.solution.y[i+2, :],
                         label=self.name + ' qp' + str(i+1))
        else:
            for i in range(self.peripherals):
                plt.plot(self.solution.t, self.solution.y[i+1, :],
                         label=self.name + ' qp' + str(i+1))

        plt.legend()
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.show()


def compare(solutions):
    """ Compares multiple solutions in one graph

    Input parameters: list of solution objects
    Output: One graph of drug evolution for all solutions
    """
    title = 'Comparison:'
    for solution in solutions:
        title = title + ' vs ' + solution.name

    plt.figure(title)
    for solution in solutions:
        plt.plot(solution.solution.t, solution.solution.y[0, :],
                 label=solution.name + ' qc')
        if solution.subcutaneous == 1:
            plt.plot(solution.solution.t, solution.solution.y[1, :],
                     label=solution.name + ' q0')
            for i in range(solution.peripherals):
                plt.plot(solution.solution.t, solution.solution.y[i+2, :],
                         label=solution.name + ' qp' + str(i+1))
        else:
            for i in range(solution.peripherals):
                plt.plot(solution.solution.t, solution.solution.y[i+1, :],
                         label=solution.name + ' qp' + str(i+1))

    plt.title(title)
    plt.legend()
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [h]')
    plt.show()
