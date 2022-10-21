#
# Protocol class
#
#import numpy as np
import matplotlib
import matplotlib.pylab as plt
matplotlib.use('TkAgg')


class Protocol:
    """A Pharmokinetic (PK) protocol
    -------------------------------
    INPUTS:
    -------------------------------
    name: str
        Name of the protocol. Will be used for plotting
    end: float
        End time of the protocol (assumed that start time is 0)
    points: int
        Number of time discretization points
    intervals: list of dicts
        List of dictionaries of constant dosage

        The intervals must be dictionaries stored in a list as follows:
        intervals = [{'start': 0, 'end': 0.1, 'dose': 1},
                    {'start': 0.5, 'end': 0.6, 'dose': 1},
                    {'start': 0.9, 'end': 1, 'dose': 2},
                    ... etc]
        'start' and 'end' are start and end times of dosage in hrs.
        'dose' is the rate of dosage in ng/h
    spikes: list of dicts
        List of delta functions that represent dose injections

        The dosage injections must be stored as follows:
        spikes = [{'time': 0.2, 'dose': 1},
                {'time': 0.8, 'dose': 2},
                ... etc]
        'time' is the time at which the instantaneous dose is applied
    """

    def __init__(self, name: str, end_time: float, points: int,
                 intervals: dict = None, spikes: dict = None):
        """ Initializes the protocol object

        Parameters
        ----------

        values: np.ndarray
            Dosage rate at any time point

        time: np.ndarray
            Time domain of the protocol

        name: str
            Name of the protocol. Will be used for plotting
        """

        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('Name must be string')
        if end_time > 0 and points > 1:
            self.time = np.linspace(0, end_time, points)
            self.values = np.zeros(points)
        else:
            raise ValueError('end time must be positive and \
                             the number of points must be > 1')
        if intervals is not None:
            for interval in intervals:
                self.__add_interval(interval)
        if spikes is not None:
            for spike in spikes:
                self.__add_spike(spike)

    def __add_interval(self, interval: dict):
        """Adds a constant dosage interval to the self.values
        attribute of Protocol object
        """

        for index, t in enumerate(self.time):
            if t >= interval['start'] and t <= interval['end']:
                if interval['dose'] > 0:
                    self.values[index] += interval['dose']
                else:
                    raise ValueError('Doses must be non-negative')

    def __add_spike(self, spike: dict):
        """Adds a local dosage spike to the self.values
        attribute of Protocol object
        """

        dt = self.time[1] - self.time[0]
        correct_dose = spike['dose']/dt  # this is a normalization
        # find location of spike time
        index = np.searchsorted(self.time, spike['time'])
        self.values[index] += correct_dose

    def value(self, t):
        """ Returns dose rate value at given time

            INPUT:
            ----------
            time: float
                A time when we want to evaluate the dosage rate

            OUTPUT:
            --------
            self.values[index]: float
                Dosage rate at time point closest to input time
        """

        # find location of given time point in our time series
        if t >= 0 and t <= self.time[-1]:
            index = np.searchsorted(self.time, t)
            return self.values[index]
        else:
            raise ValueError('Input time is outside of the protocol time')

    def show_graph(self):
        """Plots a figure of the protocol
        """

        plt.figure('Protocol ' + self.name)
        plt.plot(self.time, self.values)
        plt.title('Protocol ' + self.name)
        plt.xlabel('Time [h]')
        plt.ylabel('Dosage rate [mL/h]')
        plt.show()
