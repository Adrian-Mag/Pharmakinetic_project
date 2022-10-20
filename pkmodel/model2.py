#
# Model class
#

class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, dict):
        self.name = dict["name"]
        self.CL = dict["CL"]
        self.Vc = dict["Vc"]
        self.Qp = []
        self.Vp = []
        self.ka = 0
        
        for key in dict:
            if key[0] == "Q" and key[1] == "p":
                self.Qp.append(dict[key])
            if key[0] == "V" and key[1] == "p":
                self.Vp.append(dict[key])
        
        self.subcutaneous = 0
        
        if "ka" in dict:
            self.subcutaneous = 1
            self.ka = dict['ka']
            
        self.peripherals = len(self.Qp)
            

""" dictionary = {'CL': 1, 'Vc': 2, 'Qp1': 3, 'Vp1': 4, 'Qp2': 5, 'Vp2': 6, 'Qp3': 7, 'Vp3': 8}
my_mod = Model(dictionary)
print(my_mod.Qp, my_mod.Vp) """
