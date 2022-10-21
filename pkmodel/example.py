import pkmodel as pk

# Create Models----------------------------------------
model_subcutaneous = {'name': 'model_subcutaneous',
                      'CL': 1.0,
                      'Vc': 2.0,
                      'ka': 10.0,
                      'Qp1': 3.0,
                      'Vp1': 4.0}
model_intravenous = {'name': 'model_intravenous',
                     'CL': 1.0,
                     'Vc': 1.0,
                     'Qp1': 1.0,
                     'Vp1': 1.0}
# Create protocols-------------------------------------
end_time_1h = 1
end_time_5h = 5
points = 101
spike_1 = [{'time': 0.5, 'dose': 1.0}]
spike_2 = [{'time': 0.0, 'dose': 5.0},
           {'time': 0.6, 'dose': 10.0}]
interval_1 = [{'start': 0.0, 'end': 1.0, 'dose': 1.0}]
interval_2 = [{'start': 0.0, 'end': 1.0, 'dose': 1.0},
              {'start': 2.0, 'end': 3.5, 'dose': 2.0}]
# Build models-----------------------------------------
my_model_subcutaneous = pk.Model(model_subcutaneous)
my_model_intravenous = pk.Model(model_intravenous)
# Build protocols--------------------------------------
spike_1_interval_1 = pk.Protocol('Spike1',
                                 end_time_1h,
                                 points,
                                 interval_1,
                                 spike_1)
spike_2_interval_2 = pk.Protocol('Spike1',
                                 end_time_5h,
                                 points,
                                 interval_2,
                                 spike_2)
no_spike_interval_1 = pk.Protocol('Constant',
                                  end_time_1h,
                                  points,
                                  interval_1,
                                  None)
just_spike = pk.Protocol('Delta',
                         end_time_1h,
                         points,
                         None,
                         spike_1)
# Solve------------------------------------------------
Solution_subcutaneous_delta = pk.Solution(my_model_subcutaneous,
                                          just_spike)
Solution_intravenous_2_delta = pk.Solution(my_model_intravenous,
                                           spike_1_interval_1)
# Visualize and compare--------------------------------
just_spike.show_graph()
Solution_subcutaneous_delta.visualize()

spike_1_interval_1.show_graph()
Solution_intravenous_2_delta.visualize()

pk.solution.compare([Solution_subcutaneous_delta,
                    Solution_intravenous_2_delta])