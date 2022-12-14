#
# Model class
#
class Model:
    """A Pharmokinetic (PK) model
    ---------------------------------------
    INPUTS: dictionary describing the model
    ----------------------------------------
    name: str
        This will be used for plotting the solutions
    CL: float
        [mL/h], the clearance/elimination rate from the
        central compartment
    Vc: float
        [mL], the volume of the central compartment
    ka: float, optional
        [1/h], the “absorption” rate for the s.c dosing.
        If a ka is not given in the dictionary, its default
        value will be 0
    Qpi: float, optional
        [mL/h], the transition rate between central compartment
        and peripheral compartments i, where i can be any positive
        integer
        By default there are no peripheral compartmentss
    Vpi: float, optional
        [mL], the volume of the peripheral compartments i,
        where i can be any positive integer. Qpi and Vpi
        must be present at the same time. If only one of them
        is offered, the code will throw an error
        By default there are no peripheral compartmentss

    The dictionary should have the following template:
    {
        'name': name your model <str>, (for visualization purposes)

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

    **The peripheral compartmentss must be added starting from
    1 and increasing in increments of 1 up to the maximum number
    peripheral compartmentss used**

    **At a minimum, the model must have a main compartiemnt with
    CL and Vc given, and a name**
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
