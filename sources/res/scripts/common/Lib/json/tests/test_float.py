import math
from json.tests import PyTest, CTest

class TestFloat(object):

    def test_floats(self):
        for num in [1617161771.765, math.pi, math.pi ** 100,
         math.pi ** (-100), 3.1]:
            self.assertEqual(float(self.dumps(num)), num)
            self.assertEqual(self.loads(self.dumps(num)), num)
            self.assertEqual(self.loads(unicode(self.dumps(num))), num)

    def test_ints(self):
        for num in [1, 1, 4294967296, 18446744073709551616]:
            self.assertEqual(self.dumps(num), str(num))
            self.assertEqual(int(self.dumps(num)), num)
            self.assertEqual(self.loads(self.dumps(num)), num)
            self.assertEqual(self.loads(unicode(self.dumps(num))), num)

    def test_out_of_range(self):
        self.assertEqual(self.loads('[23456789012E666]'), [float('inf')])
        self.assertEqual(self.loads('[-23456789012E666]'), [float('-inf')])

    def test_allow_nan(self):
        for val in (float('inf'), float('-inf'), float('nan')):
            out = self.dumps([val])
            if val == val:
                self.assertEqual(self.loads(out), [val])
            else:
                res = self.loads(out)
                self.assertEqual(len(res), 1)
                self.assertNotEqual(res[0], res[0])
            self.assertRaises(ValueError, self.dumps, [val], allow_nan=False)

    def test_float_subclasses_use_float_repr(self):

        class PeculiarFloat(float):

            def __repr__(self):
                return "I'm not valid JSON"

            def __str__(self):
                return 'Neither am I'

        val = PeculiarFloat(3.2)
        self.assertEqual(self.loads(self.dumps(val)), val)


class TestPyFloat(TestFloat, PyTest):
    pass


class TestCFloat(TestFloat, CTest):
    pass