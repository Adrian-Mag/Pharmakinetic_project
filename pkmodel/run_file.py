import pkmodel as pk
import numpy as np

# User imputs --------------------------------------------- 
# Models
model1 = {'name': 'model1',
          'CL': 1.0,
          'Vc': 2.0,
          'ka': 10.0,
          'Qp1': 3.0,
          'Vp1': 4.0}
model2 = {'name': 'model2',
          'CL': 1.0,
          'Vc': 1.0,
          'ka': 1.0,
          'Qp1': 1.0,
          'Vp1': 1.0}
# Protocols
end_time = 1
points = 101
intervals = [{'start': 0, 'end': 1, 'dose': 5}] 
"""              {'start': 0.5, 'end': 0.6, 'dose': 1},
             {'start': 0.9, 'end': 1, 'dose': 2}] """
spikes = [{'time': 0.2, 'dose': 1},
          {'time': 0.8, 'dose': 1}]

# Build 
my_model = pk.Model(model1)
my_model2 = pk.Model(model2)
my_protocol = pk.Protocol('protocol 1', end_time, points, intervals, spikes)
my_protocol.show_graph()
solution = pk.Solution(my_model, my_protocol)
solution2 = pk.Solution(my_model2, my_protocol)
compare([solution, solution2])