from ctypes import *
import array, gc, unittest

class X(Structure):
    _fields_ = [
     (
      'c_int', c_int)]
    init_called = False

    def __init__(self):
        self._init_called = True


class Test(unittest.TestCase):

    def test_fom_buffer(self):
        a = array.array('i', range(16))
        x = (c_int * 16).from_buffer(a)
        y = X.from_buffer(a)
        self.assertEqual(y.c_int, a[0])
        self.assertFalse(y.init_called)
        self.assertEqual(x[:], a.tolist())
        a[0], a[-1] = (200, -200)
        self.assertEqual(x[:], a.tolist())
        self.assertIn(a, x._objects.values())
        self.assertRaises(ValueError, c_int.from_buffer, a, -1)
        expected = x[:]
        del a
        gc.collect()
        gc.collect()
        gc.collect()
        self.assertEqual(x[:], expected)
        self.assertRaises(TypeError, (c_char * 16).from_buffer, 'aaaaaaaaaaaaaaaa')

    def test_fom_buffer_with_offset(self):
        a = array.array('i', range(16))
        x = (c_int * 15).from_buffer(a, sizeof(c_int))
        self.assertEqual(x[:], a.tolist()[1:])
        self.assertRaises(ValueError, lambda : (c_int * 16).from_buffer(a, sizeof(c_int)))
        self.assertRaises(ValueError, lambda : (c_int * 1).from_buffer(a, 16 * sizeof(c_int)))

    def test_from_buffer_copy(self):
        a = array.array('i', range(16))
        x = (c_int * 16).from_buffer_copy(a)
        y = X.from_buffer_copy(a)
        self.assertEqual(y.c_int, a[0])
        self.assertFalse(y.init_called)
        self.assertEqual(x[:], range(16))
        a[0], a[-1] = (200, -200)
        self.assertEqual(x[:], range(16))
        self.assertEqual(x._objects, None)
        self.assertRaises(ValueError, c_int.from_buffer, a, -1)
        del a
        gc.collect()
        gc.collect()
        gc.collect()
        self.assertEqual(x[:], range(16))
        x = (c_char * 16).from_buffer_copy('aaaaaaaaaaaaaaaa')
        self.assertEqual(x[:], 'aaaaaaaaaaaaaaaa')
        return

    def test_fom_buffer_copy_with_offset(self):
        a = array.array('i', range(16))
        x = (c_int * 15).from_buffer_copy(a, sizeof(c_int))
        self.assertEqual(x[:], a.tolist()[1:])
        self.assertRaises(ValueError, (c_int * 16).from_buffer_copy, a, sizeof(c_int))
        self.assertRaises(ValueError, (c_int * 1).from_buffer_copy, a, 16 * sizeof(c_int))

    def test_abstract(self):
        from ctypes import _Pointer, _SimpleCData, _CFuncPtr
        self.assertRaises(TypeError, Array.from_buffer, bytearray(10))
        self.assertRaises(TypeError, Structure.from_buffer, bytearray(10))
        self.assertRaises(TypeError, Union.from_buffer, bytearray(10))
        self.assertRaises(TypeError, _CFuncPtr.from_buffer, bytearray(10))
        self.assertRaises(TypeError, _Pointer.from_buffer, bytearray(10))
        self.assertRaises(TypeError, _SimpleCData.from_buffer, bytearray(10))
        self.assertRaises(TypeError, Array.from_buffer_copy, '123')
        self.assertRaises(TypeError, Structure.from_buffer_copy, '123')
        self.assertRaises(TypeError, Union.from_buffer_copy, '123')
        self.assertRaises(TypeError, _CFuncPtr.from_buffer_copy, '123')
        self.assertRaises(TypeError, _Pointer.from_buffer_copy, '123')
        self.assertRaises(TypeError, _SimpleCData.from_buffer_copy, '123')


if __name__ == '__main__':
    unittest.main()