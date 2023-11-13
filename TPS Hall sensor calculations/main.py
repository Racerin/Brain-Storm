import math

# from units import unit


def get_min_max(pair:list[tuple[2]])->tuple[2]:
    """ 
    Looks at a list of paired data 'key and value' and returns the keys and values of the lowest and highest values. 
    TODO
    """
    minimum, maximum = None, None



class Circuit:
    r3 = 100e3
    r1 = r3
    r2 = r3

    r1 = 1e4
    r2 = 2e4

    def get_v_from_angle(self, degrees:float, ang_func, scalar:int, const:int)->float:
        """ 
        A template function for getting voltage value of hall effect sensor based on angle to magnet. 
        """
        return scalar * ang_func(math.radians(degrees)) + const

    def get_v1(self, degrees:float)->float:
        """ Get the voltage based on angle of V1. 
        Circuit model inside of method.
        """
        return self.get_v_from_angle(degrees, math.cos, 1.5, 1)
    
    def get_v2(self, degrees:float)->float:
        """ Get the voltage based on angle of V2.
        Circuit model inside of method.
        """
        return self.get_v_from_angle(degrees, math.sin, 1.5, 2.5)

    def get_i1(self, degrees:float)->float:
        """ Get the current for path 1 based on circuit model. """
        return self.get_v1(degrees)/(self.r1 + self.r2)
    
    def get_i2(self, degrees:float)->float:
        """ Get the current for path 2 based on circuit model. """
        return self.get_v2(degrees)/(self.r2 + self.r3)
    
    def get_i3(self, degrees:float)->float:
        """ 
        Get current through path 3 based on circuit. 
        Summation of I1 and I2. 
        """
        return self.get_i1(degrees) + self.get_i2(degrees)
    
    def get_v3(self, degrees:float)->float:
        """ 
        Get the voltage over resistor 3.
        Circuit model is the product of current I3 and Resistor I3
          """
        return self.get_i3(degrees) * self.r3

    def all_v3_values(self, status=True):
        """ 
        Print-out all the values of V3 for each angle.
        Status: Gives status of voltages such as min/max.
        """
        inputs = list(range(0,90,1))
        voltage_3_s = [self.get_v3(ang) for ang in inputs]
        input_outputs = zip(inputs, voltage_3_s)
        for inp,volt in input_outputs:
            print("Angle: {}, Voltage: {}".format(inp, volt))
        if status:
            # Get min and max
            maximum, minimum = max(voltage_3_s), min(voltage_3_s)
            max_i, min_i = voltage_3_s.index(maximum), voltage_3_s.index(minimum)
            ang_at_max, ang_at_min = inputs[max_i], inputs[min_i]
            print("Maximum v3 '{}' @ angle '{}'".format(maximum, ang_at_max))
            print("Minimum v3 '{}' @ angle '{}'".format(minimum, ang_at_min))


c = Circuit()


if __name__ == "__main__":
    c.all_v3_values()