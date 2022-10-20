#
# Protocol class
#
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pylab as plt

class Protocol:
    """A Pharmokinetic (PK) protocol
    -----------
    INPUTS: name of the protocol, 
    end time of the protocol (assumed that start time is 0),
    number of time diccretization points,
    intervals of constant dosage,
    local dose injections
    
    The intervals must be dictionaries stored in a list as 
    follows:
    intervals = [{'start': 0, 'end': 0.1, 'dose': 1}, 
                {'start': 0.5, 'end': 0.6, 'dose': 1},
                {'start': 0.9, 'end': 1, 'dose': 2},
                ... etc]
                
    The dosage injections must be stored as follows:
    spikes = [{'time': 0.2, 'dose': 1},
            {'time': 0.8, 'dose': 2},
            ... etc]
    
    ----------
    OUTPUTS: Object that can output the dosage rate at any time 
            and can plot the dosage protocol"""
            
    def __init__(self, name: str, end_time: float, points: int, 
                 intervals: dict, spikes: dict):
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
        
        for interval in intervals:
            self.__add_interval(interval)
        for spike in spikes:
            self.__add_spike(spike)
        
    def __add_interval(self, interval: dict):
        """ This function adds a constant dosage interval 
        to the value attribute of the protocol"""
        
        for index, t  in enumerate(self.time):
            if t >= interval['start'] and t <= interval['end']:
                if interval['dose'] > 0:
                    self.values[index] += interval['dose']
                else:
                    raise ValueError('Doses must be non-negative')
    
    def __add_spike(self, spike: dict):
        """ This function adds a local dosage spike 
        to the value attribute of the protocol"""
        
        dt = self.time[1] - self.time[0]
        correct_dose = spike['dose']/dt  # this is a normalization
        # find location of spike time
        index = np.searchsorted(self.time, spike['time'])
        self.values[index] += correct_dose
        
    def value(self, t):
        """ INPUT: a time [h] 
            OUTPUT: closest dosage value to the given time """
        
        # find location of given time point in our time series
        if t > 0 and t < self.time[-1]:
            index = np.searchsorted(self.time, t)
            return self.values[index]
        else:
            raise ValueError('Input time is outside of the protocol time')
    
    def show_graph(self):
        """ This function plots a figure of the protocol """
        
        plt.figure('Protocol ' +  self.name)
        plt.plot(self.time, self.values)
        plt.title('Protocol ' + self.name)
        plt.xlabel('Time [h]')
        plt.ylabel('Dosage rate [mL/h]')
        plt.show()

