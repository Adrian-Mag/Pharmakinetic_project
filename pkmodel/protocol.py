#
# Protocol class
#
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pylab as plt

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, name, end_time, points, intervals, spikes):
        self.name = name
        self.time = np.linspace(0, end_time, points)
        self.values = np.zeros(points)
        
        for interval in intervals:
            self.__add_interval(interval)
        for spike in spikes:
            self.__add_spike(spike)
        
    def __add_interval(self, interval: dict):
        for index, t  in enumerate(self.time):
            if t >= interval['start'] and t <= interval['end']:
                self.values[index] += interval['dose']
    
    def __add_spike(self, spike: dict):
        dt = self.time[1] - self.time[0]
        correct_dose = spike['dose']/dt
        # find location of spike time
        index = np.searchsorted(self.time, spike['time'])
        self.values[index] += correct_dose
        
    def value(self, t):
        # find location of given time point in our time series
        index = np.searchsorted(self.time, t)
        return self.values[index]
    
    def show_graph(self):
        plt.figure('Protocol ' +  self.name)
        plt.plot(self.time, self.values)

