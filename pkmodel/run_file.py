from model2 import Model
from protocol import Protocol
from solution import Solution
import numpy as np

#User imputs 
model1 = {'name': 'model1',
          'CL': 1,
          'Vc': 2,
          'ka': 1,
          'Qp1': 3,
          'Vp1': 4}
end_time = 1
points = 101
intervals = [{'start': 0, 'end': 1, 'dose': 5}] 
"""              {'start': 0.5, 'end': 0.6, 'dose': 1},
             {'start': 0.9, 'end': 1, 'dose': 2}] """
spikes = [{'time': 0.2, 'dose': 1},
          {'time': 0.8, 'dose': 1}]

# build 
my_model = Model(model1)
my_protocol = Protocol('protocol 1', end_time, points, intervals, spikes)
my_protocol.show_graph()
solution = Solution(my_model, my_protocol)
solution.visualize(my_model)