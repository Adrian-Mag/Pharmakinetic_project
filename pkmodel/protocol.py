#
# Protocol class
#
import numpy as np

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, end_time, points, intervals, spikes):
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
        return int(self.values[np.where(self.time == t)])
        
intervals = [{'start': 0, 'end': 0.1, 'dose': 1}, 
             {'start': 0.5, 'end': 0.6, 'dose': 1},
             {'start': 0.9, 'end': 1, 'dose': 2}]
spikes = [{'time': 0.2, 'dose': 1},
          {'time': 0.8, 'dose': 2}]
