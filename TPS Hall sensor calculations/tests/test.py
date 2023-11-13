import unittest
import itertools

import main

class CircuitTest(unittest.TestCase):

    def test_get_v_from_angle_range(self):
        """ Test to confirm that voltage values are in range with Circuit method. """
        # Create inputs
        circuit = main.Circuit()
        deg_lmt, sclr_lmt, cnst_lmt = 360, 10, 10
        input_possibilities = itertools.product(
            [i for i in range(deg_lmt)],
            [sclr_lmt*i/100 for i in range(100)],
            [cnst_lmt*i/100 for i in range(100)],
            )
        for input_possibility in input_possibilities:
            deg,sclr,cnst = input_possibility[0], input_possibility[1], input_possibility[2]
            value_max = abs(sclr) + cnst
            value_min = cnst - abs(sclr)
            # Now, test math.sin
            val = circuit.get_v_from_angle(deg, main.math.sin, sclr, cnst)
            assert type(val) == type(value_max) and type(val) == type(value_min), type(val)
            assert val >= value_min, "Degree,Scalar,Constant | {}".format(input_possibility)
            assert val <= value_max, "Degree,Scalar,Constant | {}".format([input_possibility, val])
            # Now, test math.cos
            val = circuit.get_v_from_angle(deg, main.math.cos, sclr, cnst)
            assert type(val) == type(value_max) and type(val) == type(value_min), type(val)
            assert val >= value_min, "Degree,Scalar,Constant | {}".format(input_possibility)
            assert val <= value_max, "Degree,Scalar,Constant | {}".format([input_possibility, val])

