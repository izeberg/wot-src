import unittest
from ctypes import *
import re, sys
if sys.byteorder == 'little':
    THIS_ENDIAN = '<'
    OTHER_ENDIAN = '>'
else:
    THIS_ENDIAN = '>'
    OTHER_ENDIAN = '<'

def normalize(format):
    if format is None:
        return ''
    else:
        format = format.replace(OTHER_ENDIAN, THIS_ENDIAN)
        return re.sub('\\s', '', format)


class Test(unittest.TestCase):

    def test_native_types(self):
        for tp, fmt, shape, itemtp in native_types:
            ob = tp()
            v = memoryview(ob)
            try:
                self.assertEqual(normalize(v.format), normalize(fmt))
                if shape is not None:
                    self.assertEqual(len(v), shape[0])
                else:
                    self.assertEqual(len(v) * sizeof(itemtp), sizeof(ob))
                self.assertEqual(v.itemsize, sizeof(itemtp))
                self.assertEqual(v.shape, shape)
                self.assertEqual(v.strides, None)
                self.assertFalse(v.readonly)
                if v.shape:
                    n = 1
                    for dim in v.shape:
                        n = n * dim

                    self.assertEqual(n * v.itemsize, len(v.tobytes()))
            except:
                print tp
                raise

        return

    def test_endian_types(self):
        for tp, fmt, shape, itemtp in endian_types:
            ob = tp()
            v = memoryview(ob)
            try:
                self.assertEqual(v.format, fmt)
                if shape is not None:
                    self.assertEqual(len(v), shape[0])
                else:
                    self.assertEqual(len(v) * sizeof(itemtp), sizeof(ob))
                self.assertEqual(v.itemsize, sizeof(itemtp))
                self.assertEqual(v.shape, shape)
                self.assertEqual(v.strides, None)
                self.assertFalse(v.readonly)
                if v.shape:
                    n = 1
                    for dim in v.shape:
                        n = n * dim

                    self.assertEqual(n, len(v))
            except:
                print tp
                raise

        return


class Point(Structure):
    _fields_ = [
     (
      'x', c_long), ('y', c_long)]


class PackedPoint(Structure):
    _pack_ = 2
    _fields_ = [('x', c_long), ('y', c_long)]


class Point2(Structure):
    pass


Point2._fields_ = [
 (
  'x', c_long), ('y', c_long)]

class EmptyStruct(Structure):
    _fields_ = []


class aUnion(Union):
    _fields_ = [
     (
      'a', c_int)]


class StructWithArrays(Structure):
    _fields_ = [
     (
      'x', c_long * 3 * 2), ('y', Point * 4)]


class Incomplete(Structure):
    pass


class Complete(Structure):
    pass


PComplete = POINTER(Complete)
Complete._fields_ = [('a', c_long)]
s_bool = {1: '?', 2: 'H', 4: 'L', 8: 'Q'}[sizeof(c_bool)]
s_short = {2: 'h', 4: 'l', 8: 'q'}[sizeof(c_short)]
s_ushort = {2: 'H', 4: 'L', 8: 'Q'}[sizeof(c_ushort)]
s_int = {2: 'h', 4: 'i', 8: 'q'}[sizeof(c_int)]
s_uint = {2: 'H', 4: 'I', 8: 'Q'}[sizeof(c_uint)]
s_long = {4: 'l', 8: 'q'}[sizeof(c_long)]
s_ulong = {4: 'L', 8: 'Q'}[sizeof(c_ulong)]
s_longlong = 'q'
s_ulonglong = 'Q'
s_float = 'f'
s_double = 'd'
s_longdouble = 'g'
if c_int is c_long:
    s_int = s_long
if c_uint is c_ulong:
    s_uint = s_ulong
if c_longlong is c_long:
    s_longlong = s_long
if c_ulonglong is c_ulong:
    s_ulonglong = s_ulong
if c_longdouble is c_double:
    s_longdouble = s_double
native_types = [
 (
  c_char, '<c', None, c_char),
 (
  c_byte, '<b', None, c_byte),
 (
  c_ubyte, '<B', None, c_ubyte),
 (
  c_short, '<' + s_short, None, c_short),
 (
  c_ushort, '<' + s_ushort, None, c_ushort),
 (
  c_int, '<' + s_int, None, c_int),
 (
  c_uint, '<' + s_uint, None, c_uint),
 (
  c_long, '<' + s_long, None, c_long),
 (
  c_ulong, '<' + s_ulong, None, c_ulong),
 (
  c_longlong, '<' + s_longlong, None, c_longlong),
 (
  c_ulonglong, '<' + s_ulonglong, None, c_ulonglong),
 (
  c_float, '<f', None, c_float),
 (
  c_double, '<d', None, c_double),
 (
  c_longdouble, '<' + s_longdouble, None, c_longdouble),
 (
  c_bool, '<' + s_bool, None, c_bool),
 (
  py_object, '<O', None, py_object),
 (
  POINTER(c_byte), '&<b', None, POINTER(c_byte)),
 (
  POINTER(POINTER(c_long)), '&&<' + s_long, None, POINTER(POINTER(c_long))),
 (
  c_double * 4, '<d', (4, ), c_double),
 (
  c_float * 4 * 3 * 2, '<f', (2, 3, 4), c_float),
 (
  POINTER(c_short) * 2, '&<' + s_short, (2, ), POINTER(c_short)),
 (
  POINTER(c_short) * 2 * 3, '&<' + s_short, (3, 2), POINTER(c_short)),
 (
  POINTER(c_short * 2), '&(2)<' + s_short, None, POINTER(c_short)),
 (
  Point, ('T{<l:x:<l:y:}').replace('l', s_long), None, Point),
 (
  PackedPoint, 'B', None, PackedPoint),
 (
  Point2, ('T{<l:x:<l:y:}').replace('l', s_long), None, Point2),
 (
  EmptyStruct, 'T{}', None, EmptyStruct),
 (
  aUnion, 'B', None, aUnion),
 (
  StructWithArrays, ('T{(2,3)<l:x:(4)T{<l:x:<l:y:}:y:}').replace('l', s_long), None, StructWithArrays),
 (
  StructWithArrays * 3, ('T{(2,3)<l:x:(4)T{<l:x:<l:y:}:y:}').replace('l', s_long), (3, ), StructWithArrays),
 (
  Incomplete, 'B', None, Incomplete),
 (
  POINTER(Incomplete), '&B', None, POINTER(Incomplete)),
 (
  Complete, ('T{<l:a:}').replace('l', s_long), None, Complete),
 (
  POINTER(Complete), '&B', None, POINTER(Complete)),
 (
  CFUNCTYPE(None), 'X{}', None, CFUNCTYPE(None))]

class BEPoint(BigEndianStructure):
    _fields_ = [
     (
      'x', c_long), ('y', c_long)]


class LEPoint(LittleEndianStructure):
    _fields_ = [
     (
      'x', c_long), ('y', c_long)]


endian_types = [
 (
  BEPoint, ('T{>l:x:>l:y:}').replace('l', s_long), None, BEPoint),
 (
  LEPoint, ('T{<l:x:<l:y:}').replace('l', s_long), None, LEPoint),
 (
  POINTER(BEPoint), ('&T{>l:x:>l:y:}').replace('l', s_long), None, POINTER(BEPoint)),
 (
  POINTER(LEPoint), ('&T{<l:x:<l:y:}').replace('l', s_long), None, POINTER(LEPoint))]
if __name__ == '__main__':
    unittest.main()