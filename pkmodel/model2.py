#
# Model class
#

class Model:
    """A Pharmokinetic (PK) model
    -------
    INPUTS: dictionary describing the model
    The dictionary should have the following template:
    {
        'name': name <str>,
        'CL': CL <float> [mL/h],
        'Vc': Vc <float>, [mL]
        'ka': ka <float>, [1/h] (if subcutaneous)
        'Qp1': Qp1 <float>, [mL/h] (if one peripheral used)
        'Vp1': Vp1 <float>, [mL] (if one peripheral used)
        'Qp2': Qp1 <float>, [mL/h] (if two peripheral used)
        'Vp2': Vp1 <float>, [mL] (if two peripheral used)
        'Qp3': Qp1 <float>, [mL/h] (if three peripheral used)
        'Vp3': Vp1 <float>, [mL] (if three peripheral used)
        ... etc
    }
    
    !! The peripheral compartiments must be added starting from
    1 and increasing in increments of 1 up to the maximum number 
    peripheral compartiments used !!
    
    !! At a minimum the model must have a main compartiemnt with
    CL and Vc given and a name !!
    ----------
    OUTPUTS: model object that holds all the properties as attributes
    ----------

    """
    def __init__(self, dict: dict):
        
        if ("CL" not in dict):
            raise ValueError('Please provide CL!') 
        elif ("Vc" not in dict):
            raise ValueError('Please provide Vc!') 
        elif ("name" not in dict):
            raise ValueError('Please provide name!') 
        
        if isinstance(dict['name'], str):
            self.name = dict["name"]
        else: 
            raise ValueError('name must be string')
        if isinstance(dict['CL'], float) and \
           isinstance(dict['Vc'], float):
            self.CL = dict["CL"]
            self.Vc = dict["Vc"]
        else:
            raise ValueError('CL and Vc must be floats')
           
        self.Qp = []
        self.Vp = []
        self.ka = 0

        # Cycle through the input dictionary and separate 
        # the attributes
        for key in dict:
            if key[0] == "Q" and key[1] == "p":
                if isinstance(dict[key], float):
                    self.Qp.append(dict[key])
                else:
                    raise ValueError('All Qps must be floats')
            if key[0] == "V" and key[1] == "p":
                if isinstance(dict[key], float):
                    self.Vp.append(dict[key])
                else:
                    raise ValueError('All Vps must be floats')
                
        self.subcutaneous = 0
        
        if "ka" in dict:
            if dict['ka'] == 0:
                raise ValueError('ka must be positive!') 
            self.subcutaneous = 1
            self.ka = dict['ka']
        
        self.peripherals = len(self.Qp)
            
