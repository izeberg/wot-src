import difflib, pprint, pickle, re, sys
from copy import deepcopy
from test import test_support
import unittest
from unittest.test.support import TestEquality, TestHashing, LoggingResult, ResultWithNoStartTestRunStopTestRun

class Test(object):

    class Foo(unittest.TestCase):

        def runTest(self):
            pass

        def test1(self):
            pass

    class Bar(Foo):

        def test2(self):
            pass

    class LoggingTestCase(unittest.TestCase):

        def __init__(self, events):
            super(Test.LoggingTestCase, self).__init__('test')
            self.events = events

        def setUp(self):
            self.events.append('setUp')

        def test(self):
            self.events.append('test')

        def tearDown(self):
            self.events.append('tearDown')


class Test_TestCase(unittest.TestCase, TestEquality, TestHashing):
    eq_pairs = [
     (
      Test.Foo('test1'), Test.Foo('test1'))]
    ne_pairs = [
     (
      Test.Foo('test1'), Test.Foo('runTest')),
     (
      Test.Foo('test1'), Test.Bar('test1')),
     (
      Test.Foo('test1'), Test.Bar('test2'))]

    def test_init__no_test_name(self):

        class Test(unittest.TestCase):

            def runTest(self):
                raise TypeError()

            def test(self):
                pass

        self.assertEqual(Test().id()[-13:], '.Test.runTest')

    def test_init__test_name__valid(self):

        class Test(unittest.TestCase):

            def runTest(self):
                raise TypeError()

            def test(self):
                pass

        self.assertEqual(Test('test').id()[-10:], '.Test.test')

    def test_init__test_name__invalid(self):

        class Test(unittest.TestCase):

            def runTest(self):
                raise TypeError()

            def test(self):
                pass

        try:
            Test('testfoo')
        except ValueError:
            pass
        else:
            self.fail('Failed to raise ValueError')

    def test_countTestCases(self):

        class Foo(unittest.TestCase):

            def test(self):
                pass

        self.assertEqual(Foo('test').countTestCases(), 1)

    def test_defaultTestResult(self):

        class Foo(unittest.TestCase):

            def runTest(self):
                pass

        result = Foo().defaultTestResult()
        self.assertEqual(type(result), unittest.TestResult)

    def test_run_call_order__error_in_setUp(self):
        events = []
        result = LoggingResult(events)

        class Foo(Test.LoggingTestCase):

            def setUp(self):
                super(Foo, self).setUp()
                raise RuntimeError('raised by Foo.setUp')

        Foo(events).run(result)
        expected = ['startTest', 'setUp', 'addError', 'stopTest']
        self.assertEqual(events, expected)

    def test_run_call_order__error_in_setUp_default_result(self):
        events = []

        class Foo(Test.LoggingTestCase):

            def defaultTestResult(self):
                return LoggingResult(self.events)

            def setUp(self):
                super(Foo, self).setUp()
                raise RuntimeError('raised by Foo.setUp')

        Foo(events).run()
        expected = ['startTestRun', 'startTest', 'setUp', 'addError',
         'stopTest', 'stopTestRun']
        self.assertEqual(events, expected)

    def test_run_call_order__error_in_test(self):
        events = []
        result = LoggingResult(events)

        class Foo(Test.LoggingTestCase):

            def test(self):
                super(Foo, self).test()
                raise RuntimeError('raised by Foo.test')

        expected = [
         'startTest', 'setUp', 'test', 'addError', 'tearDown',
         'stopTest']
        Foo(events).run(result)
        self.assertEqual(events, expected)

    def test_run_call_order__error_in_test_default_result(self):
        events = []

        class Foo(Test.LoggingTestCase):

            def defaultTestResult(self):
                return LoggingResult(self.events)

            def test(self):
                super(Foo, self).test()
                raise RuntimeError('raised by Foo.test')

        expected = [
         'startTestRun', 'startTest', 'setUp', 'test', 'addError',
         'tearDown', 'stopTest', 'stopTestRun']
        Foo(events).run()
        self.assertEqual(events, expected)

    def test_run_call_order__failure_in_test(self):
        events = []
        result = LoggingResult(events)

        class Foo(Test.LoggingTestCase):

            def test(self):
                super(Foo, self).test()
                self.fail('raised by Foo.test')

        expected = [
         'startTest', 'setUp', 'test', 'addFailure', 'tearDown',
         'stopTest']
        Foo(events).run(result)
        self.assertEqual(events, expected)

    def test_run_call_order__failure_in_test_default_result(self):

        class Foo(Test.LoggingTestCase):

            def defaultTestResult(self):
                return LoggingResult(self.events)

            def test(self):
                super(Foo, self).test()
                self.fail('raised by Foo.test')

        expected = [
         'startTestRun', 'startTest', 'setUp', 'test', 'addFailure',
         'tearDown', 'stopTest', 'stopTestRun']
        events = []
        Foo(events).run()
        self.assertEqual(events, expected)

    def test_run_call_order__error_in_tearDown(self):
        events = []
        result = LoggingResult(events)

        class Foo(Test.LoggingTestCase):

            def tearDown(self):
                super(Foo, self).tearDown()
                raise RuntimeError('raised by Foo.tearDown')

        Foo(events).run(result)
        expected = ['startTest', 'setUp', 'test', 'tearDown', 'addError',
         'stopTest']
        self.assertEqual(events, expected)

    def test_run_call_order__error_in_tearDown_default_result(self):

        class Foo(Test.LoggingTestCase):

            def defaultTestResult(self):
                return LoggingResult(self.events)

            def tearDown(self):
                super(Foo, self).tearDown()
                raise RuntimeError('raised by Foo.tearDown')

        events = []
        Foo(events).run()
        expected = ['startTestRun', 'startTest', 'setUp', 'test', 'tearDown',
         'addError', 'stopTest', 'stopTestRun']
        self.assertEqual(events, expected)

    def test_run_call_order_default_result(self):

        class Foo(unittest.TestCase):

            def defaultTestResult(self):
                return ResultWithNoStartTestRunStopTestRun()

            def test(self):
                pass

        Foo('test').run()

    def test_failureException__default(self):

        class Foo(unittest.TestCase):

            def test(self):
                pass

        self.assertIs(Foo('test').failureException, AssertionError)

    def test_failureException__subclassing__explicit_raise(self):
        events = []
        result = LoggingResult(events)

        class Foo(unittest.TestCase):

            def test(self):
                raise RuntimeError()

            failureException = RuntimeError

        self.assertIs(Foo('test').failureException, RuntimeError)
        Foo('test').run(result)
        expected = ['startTest', 'addFailure', 'stopTest']
        self.assertEqual(events, expected)

    def test_failureException__subclassing__implicit_raise(self):
        events = []
        result = LoggingResult(events)

        class Foo(unittest.TestCase):

            def test(self):
                self.fail('foo')

            failureException = RuntimeError

        self.assertIs(Foo('test').failureException, RuntimeError)
        Foo('test').run(result)
        expected = ['startTest', 'addFailure', 'stopTest']
        self.assertEqual(events, expected)

    def test_setUp(self):

        class Foo(unittest.TestCase):

            def runTest(self):
                pass

        Foo().setUp()

    def test_tearDown(self):

        class Foo(unittest.TestCase):

            def runTest(self):
                pass

        Foo().tearDown()

    def test_id(self):

        class Foo(unittest.TestCase):

            def runTest(self):
                pass

        self.assertIsInstance(Foo().id(), basestring)

    def test_run__uses_defaultTestResult(self):
        events = []

        class Foo(unittest.TestCase):

            def test(self):
                events.append('test')

            def defaultTestResult(self):
                return LoggingResult(events)

        Foo('test').run()
        expected = [
         'startTestRun', 'startTest', 'test', 'addSuccess',
         'stopTest', 'stopTestRun']
        self.assertEqual(events, expected)

    def testShortDescriptionWithoutDocstring(self):
        self.assertIsNone(self.shortDescription())

    @unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
    def testShortDescriptionWithOneLineDocstring(self):
        self.assertEqual(self.shortDescription(), 'Tests shortDescription() for a method with a docstring.')

    @unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
    def testShortDescriptionWithMultiLineDocstring(self):
        self.assertEqual(self.shortDescription(), 'Tests shortDescription() for a method with a longer docstring.')

    def testAddTypeEqualityFunc(self):

        class SadSnake(object):
            pass

        s1, s2 = SadSnake(), SadSnake()
        self.assertNotEqual(s1, s2)

        def AllSnakesCreatedEqual(a, b, msg=None):
            return type(a) is type(b) is SadSnake

        self.addTypeEqualityFunc(SadSnake, AllSnakesCreatedEqual)
        self.assertEqual(s1, s2)
        return

    def testAssertIs(self):
        thing = object()
        self.assertIs(thing, thing)
        self.assertRaises(self.failureException, self.assertIs, thing, object())

    def testAssertIsNot(self):
        thing = object()
        self.assertIsNot(thing, object())
        self.assertRaises(self.failureException, self.assertIsNot, thing, thing)

    def testAssertIsInstance(self):
        thing = []
        self.assertIsInstance(thing, list)
        self.assertRaises(self.failureException, self.assertIsInstance, thing, dict)

    def testAssertNotIsInstance(self):
        thing = []
        self.assertNotIsInstance(thing, dict)
        self.assertRaises(self.failureException, self.assertNotIsInstance, thing, list)

    def testAssertIn(self):
        animals = {'monkey': 'banana', 'cow': 'grass', 'seal': 'fish'}
        self.assertIn('a', 'abc')
        self.assertIn(2, [1, 2, 3])
        self.assertIn('monkey', animals)
        self.assertNotIn('d', 'abc')
        self.assertNotIn(0, [1, 2, 3])
        self.assertNotIn('otter', animals)
        self.assertRaises(self.failureException, self.assertIn, 'x', 'abc')
        self.assertRaises(self.failureException, self.assertIn, 4, [1, 2, 3])
        self.assertRaises(self.failureException, self.assertIn, 'elephant', animals)
        self.assertRaises(self.failureException, self.assertNotIn, 'c', 'abc')
        self.assertRaises(self.failureException, self.assertNotIn, 1, [1, 2, 3])
        self.assertRaises(self.failureException, self.assertNotIn, 'cow', animals)

    def testAssertDictContainsSubset(self):
        self.assertDictContainsSubset({}, {})
        self.assertDictContainsSubset({}, {'a': 1})
        self.assertDictContainsSubset({'a': 1}, {'a': 1})
        self.assertDictContainsSubset({'a': 1}, {'a': 1, 'b': 2})
        self.assertDictContainsSubset({'a': 1, 'b': 2}, {'a': 1, 'b': 2})
        with self.assertRaises(self.failureException):
            self.assertDictContainsSubset({1: 'one'}, {})
        with self.assertRaises(self.failureException):
            self.assertDictContainsSubset({'a': 2}, {'a': 1})
        with self.assertRaises(self.failureException):
            self.assertDictContainsSubset({'c': 1}, {'a': 1})
        with self.assertRaises(self.failureException):
            self.assertDictContainsSubset({'a': 1, 'c': 1}, {'a': 1})
        with self.assertRaises(self.failureException):
            self.assertDictContainsSubset({'a': 1, 'c': 1}, {'a': 1})
        with test_support.check_warnings(('', UnicodeWarning)):
            one = ('').join(chr(i) for i in range(255))
            with self.assertRaises(self.failureException):
                self.assertDictContainsSubset({'foo': one}, {'foo': '�'})

    def testAssertEqual(self):
        equal_pairs = [((), ()), ({}, {}), ([], []),
         (
          set(), set()),
         (
          frozenset(), frozenset())]
        for a, b in equal_pairs:
            try:
                self.assertEqual(a, b)
            except self.failureException:
                self.fail('assertEqual(%r, %r) failed' % (a, b))

            try:
                self.assertEqual(a, b, msg='foo')
            except self.failureException:
                self.fail('assertEqual(%r, %r) with msg= failed' % (a, b))

            try:
                self.assertEqual(a, b, 'foo')
            except self.failureException:
                self.fail('assertEqual(%r, %r) with third parameter failed' % (
                 a, b))

        unequal_pairs = [((), []), ({}, set()),
         (
          set([4, 1]), frozenset([4, 2])),
         (
          frozenset([4, 5]), set([2, 3])),
         (
          set([3, 4]), set([5, 4]))]
        for a, b in unequal_pairs:
            self.assertRaises(self.failureException, self.assertEqual, a, b)
            self.assertRaises(self.failureException, self.assertEqual, a, b, 'foo')
            self.assertRaises(self.failureException, self.assertEqual, a, b, msg='foo')

    def testEquality(self):
        self.assertListEqual([], [])
        self.assertTupleEqual((), ())
        self.assertSequenceEqual([], ())
        a = [
         0, 'a', []]
        b = []
        self.assertRaises(unittest.TestCase.failureException, self.assertListEqual, a, b)
        self.assertRaises(unittest.TestCase.failureException, self.assertListEqual, tuple(a), tuple(b))
        self.assertRaises(unittest.TestCase.failureException, self.assertSequenceEqual, a, tuple(b))
        b.extend(a)
        self.assertListEqual(a, b)
        self.assertTupleEqual(tuple(a), tuple(b))
        self.assertSequenceEqual(a, tuple(b))
        self.assertSequenceEqual(tuple(a), b)
        self.assertRaises(self.failureException, self.assertListEqual, a, tuple(b))
        self.assertRaises(self.failureException, self.assertTupleEqual, tuple(a), b)
        self.assertRaises(self.failureException, self.assertListEqual, None, b)
        self.assertRaises(self.failureException, self.assertTupleEqual, None, tuple(b))
        self.assertRaises(self.failureException, self.assertSequenceEqual, None, tuple(b))
        self.assertRaises(self.failureException, self.assertListEqual, 1, 1)
        self.assertRaises(self.failureException, self.assertTupleEqual, 1, 1)
        self.assertRaises(self.failureException, self.assertSequenceEqual, 1, 1)
        self.assertDictEqual({}, {})
        c = {'x': 1}
        d = {}
        self.assertRaises(unittest.TestCase.failureException, self.assertDictEqual, c, d)
        d.update(c)
        self.assertDictEqual(c, d)
        d['x'] = 0
        self.assertRaises(unittest.TestCase.failureException, self.assertDictEqual, c, d, 'These are unequal')
        self.assertRaises(self.failureException, self.assertDictEqual, None, d)
        self.assertRaises(self.failureException, self.assertDictEqual, [], d)
        self.assertRaises(self.failureException, self.assertDictEqual, 1, 1)
        return

    def testAssertSequenceEqualMaxDiff(self):
        self.assertEqual(self.maxDiff, 640)
        seq1 = 'a' + 'x' * 6400
        seq2 = 'b' + 'x' * 6400
        diff = ('\n').join(difflib.ndiff(pprint.pformat(seq1).splitlines(), pprint.pformat(seq2).splitlines()))
        omitted = unittest.case.DIFF_OMITTED % (len(diff) + 1,)
        self.maxDiff = len(diff) // 2
        try:
            self.assertSequenceEqual(seq1, seq2)
        except self.failureException as e:
            msg = e.args[0]
        else:
            self.fail('assertSequenceEqual did not fail.')

        self.assertLess(len(msg), len(diff))
        self.assertIn(omitted, msg)
        self.maxDiff = len(diff) * 2
        try:
            self.assertSequenceEqual(seq1, seq2)
        except self.failureException as e:
            msg = e.args[0]
        else:
            self.fail('assertSequenceEqual did not fail.')

        self.assertGreater(len(msg), len(diff))
        self.assertNotIn(omitted, msg)
        self.maxDiff = None
        try:
            self.assertSequenceEqual(seq1, seq2)
        except self.failureException as e:
            msg = e.args[0]
        else:
            self.fail('assertSequenceEqual did not fail.')

        self.assertGreater(len(msg), len(diff))
        self.assertNotIn(omitted, msg)
        return

    def testTruncateMessage(self):
        self.maxDiff = 1
        message = self._truncateMessage('foo', 'bar')
        omitted = unittest.case.DIFF_OMITTED % len('bar')
        self.assertEqual(message, 'foo' + omitted)
        self.maxDiff = None
        message = self._truncateMessage('foo', 'bar')
        self.assertEqual(message, 'foobar')
        self.maxDiff = 4
        message = self._truncateMessage('foo', 'bar')
        self.assertEqual(message, 'foobar')
        return

    def testAssertDictEqualTruncates(self):
        test = unittest.TestCase('assertEqual')

        def truncate(msg, diff):
            return 'foo'

        test._truncateMessage = truncate
        try:
            test.assertDictEqual({}, {1: 0})
        except self.failureException as e:
            self.assertEqual(str(e), 'foo')
        else:
            self.fail('assertDictEqual did not fail')

    def testAssertMultiLineEqualTruncates(self):
        test = unittest.TestCase('assertEqual')

        def truncate(msg, diff):
            return 'foo'

        test._truncateMessage = truncate
        try:
            test.assertMultiLineEqual('foo', 'bar')
        except self.failureException as e:
            self.assertEqual(str(e), 'foo')
        else:
            self.fail('assertMultiLineEqual did not fail')

    def testAssertEqual_diffThreshold(self):
        self.assertEqual(self._diffThreshold, 65536)
        self.maxDiff = None
        old_threshold = self._diffThreshold
        self._diffThreshold = 256
        self.addCleanup(lambda : setattr(self, '_diffThreshold', old_threshold))
        s = 'x' * 128
        with self.assertRaises(self.failureException) as (cm):
            self.assertEqual(s + 'a', s + 'b')
        self.assertIn('^', str(cm.exception))
        self.assertEqual(s + 'a', s + 'a')
        s = 'x' * 512

        def explodingTruncation(message, diff):
            raise SystemError('this should not be raised')

        old_truncate = self._truncateMessage
        self._truncateMessage = explodingTruncation
        self.addCleanup(lambda : setattr(self, '_truncateMessage', old_truncate))
        s1, s2 = s + 'a', s + 'b'
        with self.assertRaises(self.failureException) as (cm):
            self.assertEqual(s1, s2)
        self.assertNotIn('^', str(cm.exception))
        self.assertEqual(str(cm.exception), '%r != %r' % (s1, s2))
        self.assertEqual(s + 'a', s + 'a')
        return

    def testAssertItemsEqual(self):
        a = object()
        self.assertItemsEqual([1, 2, 3], [3, 2, 1])
        self.assertItemsEqual(['foo', 'bar', 'baz'], ['bar', 'baz', 'foo'])
        self.assertItemsEqual([a, a, 2, 2, 3], (a, 2, 3, a, 2))
        self.assertItemsEqual([1, '2', 'a', 'a'], ['a', '2', True, 'a'])
        self.assertRaises(self.failureException, self.assertItemsEqual, [
         1, 2] + [3] * 100, [1] * 100 + [2, 3])
        self.assertRaises(self.failureException, self.assertItemsEqual, [
         1, '2', 'a', 'a'], ['a', '2', True, 1])
        self.assertRaises(self.failureException, self.assertItemsEqual, [
         10], [10, 11])
        self.assertRaises(self.failureException, self.assertItemsEqual, [
         10, 11], [10])
        self.assertRaises(self.failureException, self.assertItemsEqual, [
         10, 11, 10], [10, 11])
        self.assertItemsEqual([[1, 2], [3, 4], 0], [False, [3, 4], [1, 2]])
        self.assertItemsEqual(iter([1, 2, [], 3, 4]), iter([1, 2, [], 3, 4]))
        self.assertRaises(self.failureException, self.assertItemsEqual, [], [divmod, 'x', 1, complex(0.0, 5.0), complex(0.0, 2.0), frozenset()])
        self.assertItemsEqual([{'a': 1}, {'b': 2}], [{'b': 2}, {'a': 1}])
        self.assertItemsEqual([1, 'x', divmod, []], [divmod, [], 'x', 1])
        self.assertRaises(self.failureException, self.assertItemsEqual, [], [divmod, [], 'x', 1, complex(0.0, 5.0), complex(0.0, 2.0), set()])
        self.assertRaises(self.failureException, self.assertItemsEqual, [
         [
          1]], [[2]])
        self.assertRaises(self.failureException, self.assertItemsEqual, [
         1, 1, 2], [2, 1])
        self.assertRaises(self.failureException, self.assertItemsEqual, [
         1, 1, '2', 'a', 'a'], ['2', '2', True, 'a'])
        self.assertRaises(self.failureException, self.assertItemsEqual, [
         1, {'b': 2}, None, True], [{'b': 2}, True, None])
        a = [
         {
          2, 4}, {1, 2}]
        b = a[::-1]
        self.assertItemsEqual(a, b)
        diffs = set(unittest.util._count_diff_all_purpose('aaabccd', 'abbbcce'))
        expected = {(3, 1, 'a'), (1, 3, 'b'), (1, 0, 'd'), (0, 1, 'e')}
        self.assertEqual(diffs, expected)
        diffs = unittest.util._count_diff_all_purpose([[]], [])
        self.assertEqual(diffs, [(1, 0, [])])
        diffs = set(unittest.util._count_diff_hashable('aaabccd', 'abbbcce'))
        expected = {(3, 1, 'a'), (1, 3, 'b'), (1, 0, 'd'), (0, 1, 'e')}
        self.assertEqual(diffs, expected)
        return

    def testAssertSetEqual(self):
        set1 = set()
        set2 = set()
        self.assertSetEqual(set1, set2)
        self.assertRaises(self.failureException, self.assertSetEqual, None, set2)
        self.assertRaises(self.failureException, self.assertSetEqual, [], set2)
        self.assertRaises(self.failureException, self.assertSetEqual, set1, None)
        self.assertRaises(self.failureException, self.assertSetEqual, set1, [])
        set1 = set(['a'])
        set2 = set()
        self.assertRaises(self.failureException, self.assertSetEqual, set1, set2)
        set1 = set(['a'])
        set2 = set(['a'])
        self.assertSetEqual(set1, set2)
        set1 = set(['a'])
        set2 = set(['a', 'b'])
        self.assertRaises(self.failureException, self.assertSetEqual, set1, set2)
        set1 = set(['a'])
        set2 = frozenset(['a', 'b'])
        self.assertRaises(self.failureException, self.assertSetEqual, set1, set2)
        set1 = set(['a', 'b'])
        set2 = frozenset(['a', 'b'])
        self.assertSetEqual(set1, set2)
        set1 = set()
        set2 = 'foo'
        self.assertRaises(self.failureException, self.assertSetEqual, set1, set2)
        self.assertRaises(self.failureException, self.assertSetEqual, set2, set1)
        set1 = set([(0, 1), (2, 3)])
        set2 = set([(4, 5)])
        self.assertRaises(self.failureException, self.assertSetEqual, set1, set2)
        return

    def testInequality(self):
        self.assertGreater(2, 1)
        self.assertGreaterEqual(2, 1)
        self.assertGreaterEqual(1, 1)
        self.assertLess(1, 2)
        self.assertLessEqual(1, 2)
        self.assertLessEqual(1, 1)
        self.assertRaises(self.failureException, self.assertGreater, 1, 2)
        self.assertRaises(self.failureException, self.assertGreater, 1, 1)
        self.assertRaises(self.failureException, self.assertGreaterEqual, 1, 2)
        self.assertRaises(self.failureException, self.assertLess, 2, 1)
        self.assertRaises(self.failureException, self.assertLess, 1, 1)
        self.assertRaises(self.failureException, self.assertLessEqual, 2, 1)
        self.assertGreater(1.1, 1.0)
        self.assertGreaterEqual(1.1, 1.0)
        self.assertGreaterEqual(1.0, 1.0)
        self.assertLess(1.0, 1.1)
        self.assertLessEqual(1.0, 1.1)
        self.assertLessEqual(1.0, 1.0)
        self.assertRaises(self.failureException, self.assertGreater, 1.0, 1.1)
        self.assertRaises(self.failureException, self.assertGreater, 1.0, 1.0)
        self.assertRaises(self.failureException, self.assertGreaterEqual, 1.0, 1.1)
        self.assertRaises(self.failureException, self.assertLess, 1.1, 1.0)
        self.assertRaises(self.failureException, self.assertLess, 1.0, 1.0)
        self.assertRaises(self.failureException, self.assertLessEqual, 1.1, 1.0)
        self.assertGreater('bug', 'ant')
        self.assertGreaterEqual('bug', 'ant')
        self.assertGreaterEqual('ant', 'ant')
        self.assertLess('ant', 'bug')
        self.assertLessEqual('ant', 'bug')
        self.assertLessEqual('ant', 'ant')
        self.assertRaises(self.failureException, self.assertGreater, 'ant', 'bug')
        self.assertRaises(self.failureException, self.assertGreater, 'ant', 'ant')
        self.assertRaises(self.failureException, self.assertGreaterEqual, 'ant', 'bug')
        self.assertRaises(self.failureException, self.assertLess, 'bug', 'ant')
        self.assertRaises(self.failureException, self.assertLess, 'ant', 'ant')
        self.assertRaises(self.failureException, self.assertLessEqual, 'bug', 'ant')
        self.assertGreater('bug', 'ant')
        self.assertGreaterEqual('bug', 'ant')
        self.assertGreaterEqual('ant', 'ant')
        self.assertLess('ant', 'bug')
        self.assertLessEqual('ant', 'bug')
        self.assertLessEqual('ant', 'ant')
        self.assertRaises(self.failureException, self.assertGreater, 'ant', 'bug')
        self.assertRaises(self.failureException, self.assertGreater, 'ant', 'ant')
        self.assertRaises(self.failureException, self.assertGreaterEqual, 'ant', 'bug')
        self.assertRaises(self.failureException, self.assertLess, 'bug', 'ant')
        self.assertRaises(self.failureException, self.assertLess, 'ant', 'ant')
        self.assertRaises(self.failureException, self.assertLessEqual, 'bug', 'ant')
        self.assertGreater('bug', 'ant')
        self.assertGreater('bug', 'ant')
        self.assertGreaterEqual('bug', 'ant')
        self.assertGreaterEqual('bug', 'ant')
        self.assertGreaterEqual('ant', 'ant')
        self.assertGreaterEqual('ant', 'ant')
        self.assertLess('ant', 'bug')
        self.assertLess('ant', 'bug')
        self.assertLessEqual('ant', 'bug')
        self.assertLessEqual('ant', 'bug')
        self.assertLessEqual('ant', 'ant')
        self.assertLessEqual('ant', 'ant')
        self.assertRaises(self.failureException, self.assertGreater, 'ant', 'bug')
        self.assertRaises(self.failureException, self.assertGreater, 'ant', 'bug')
        self.assertRaises(self.failureException, self.assertGreater, 'ant', 'ant')
        self.assertRaises(self.failureException, self.assertGreater, 'ant', 'ant')
        self.assertRaises(self.failureException, self.assertGreaterEqual, 'ant', 'bug')
        self.assertRaises(self.failureException, self.assertGreaterEqual, 'ant', 'bug')
        self.assertRaises(self.failureException, self.assertLess, 'bug', 'ant')
        self.assertRaises(self.failureException, self.assertLess, 'bug', 'ant')
        self.assertRaises(self.failureException, self.assertLess, 'ant', 'ant')
        self.assertRaises(self.failureException, self.assertLess, 'ant', 'ant')
        self.assertRaises(self.failureException, self.assertLessEqual, 'bug', 'ant')
        self.assertRaises(self.failureException, self.assertLessEqual, 'bug', 'ant')

    def testAssertMultiLineEqual(self):
        sample_text = 'http://www.python.org/doc/2.3/lib/module-unittest.html\ntest case\n    A test case is the smallest unit of testing. [...]\n'
        revised_sample_text = 'http://www.python.org/doc/2.4.1/lib/module-unittest.html\ntest case\n    A test case is the smallest unit of testing. [...] You may provide your\n    own implementation that does not subclass from TestCase, of course.\n'
        sample_text_error = '- http://www.python.org/doc/2.3/lib/module-unittest.html\n?                             ^\n+ http://www.python.org/doc/2.4.1/lib/module-unittest.html\n?                             ^^^\n  test case\n-     A test case is the smallest unit of testing. [...]\n+     A test case is the smallest unit of testing. [...] You may provide your\n?                                                       +++++++++++++++++++++\n+     own implementation that does not subclass from TestCase, of course.\n'
        self.maxDiff = None
        for type_changer in (lambda x: x, lambda x: x.decode('utf8')):
            try:
                self.assertMultiLineEqual(type_changer(sample_text), type_changer(revised_sample_text))
            except self.failureException as e:
                error = str(e).encode('utf8').split('\n', 1)[1]
                self.assertTrue(sample_text_error == error)

        return

    def testAsertEqualSingleLine(self):
        sample_text = 'laden swallows fly slowly'
        revised_sample_text = 'unladen swallows fly quickly'
        sample_text_error = '- laden swallows fly slowly\n?                    ^^^^\n+ unladen swallows fly quickly\n? ++                   ^^^^^\n'
        try:
            self.assertEqual(sample_text, revised_sample_text)
        except self.failureException as e:
            error = str(e).split('\n', 1)[1]
            self.assertTrue(sample_text_error == error)

    def testAssertIsNone(self):
        self.assertIsNone(None)
        self.assertRaises(self.failureException, self.assertIsNone, False)
        self.assertIsNotNone('DjZoPloGears on Rails')
        self.assertRaises(self.failureException, self.assertIsNotNone, None)
        return

    def testAssertRegexpMatches(self):
        self.assertRegexpMatches('asdfabasdf', 'ab+')
        self.assertRaises(self.failureException, self.assertRegexpMatches, 'saaas', 'aaaa')

    def testAssertRaisesCallable(self):

        class ExceptionMock(Exception):
            pass

        def Stub():
            raise ExceptionMock('We expect')

        self.assertRaises(ExceptionMock, Stub)
        self.assertRaises((ValueError, ExceptionMock), Stub)
        self.assertRaises(ValueError, int, '19', base=8)
        with self.assertRaises(self.failureException):
            self.assertRaises(ExceptionMock, lambda : 0)
        with self.assertRaises(ExceptionMock):
            self.assertRaises(ValueError, Stub)

    def testAssertRaisesContext(self):

        class ExceptionMock(Exception):
            pass

        def Stub():
            raise ExceptionMock('We expect')

        with self.assertRaises(ExceptionMock):
            Stub()
        with self.assertRaises((ValueError, ExceptionMock)) as (cm):
            Stub()
        self.assertIsInstance(cm.exception, ExceptionMock)
        self.assertEqual(cm.exception.args[0], 'We expect')
        with self.assertRaises(ValueError):
            int('19', base=8)
        with self.assertRaises(self.failureException):
            with self.assertRaises(ExceptionMock):
                pass
        with self.assertRaises(ExceptionMock):
            self.assertRaises(ValueError, Stub)

    def testAssertRaisesRegexp(self):

        class ExceptionMock(Exception):
            pass

        def Stub():
            raise ExceptionMock('We expect')

        self.assertRaisesRegexp(ExceptionMock, re.compile('expect$'), Stub)
        self.assertRaisesRegexp(ExceptionMock, 'expect$', Stub)
        self.assertRaisesRegexp(ExceptionMock, 'expect$', Stub)

    def testAssertNotRaisesRegexp(self):
        self.assertRaisesRegexp(self.failureException, '^Exception not raised$', self.assertRaisesRegexp, Exception, re.compile('x'), lambda : None)
        self.assertRaisesRegexp(self.failureException, '^Exception not raised$', self.assertRaisesRegexp, Exception, 'x', lambda : None)
        self.assertRaisesRegexp(self.failureException, '^Exception not raised$', self.assertRaisesRegexp, Exception, 'x', lambda : None)

    def testAssertRaisesRegexpInvalidRegexp(self):

        class MyExc(Exception):
            pass

        self.assertRaises(TypeError, self.assertRaisesRegexp, MyExc, lambda : True)

    def testAssertRaisesRegexpMismatch(self):

        def Stub():
            raise Exception('Unexpected')

        self.assertRaisesRegexp(self.failureException, '"\\^Expected\\$" does not match "Unexpected"', self.assertRaisesRegexp, Exception, '^Expected$', Stub)
        self.assertRaisesRegexp(self.failureException, '"\\^Expected\\$" does not match "Unexpected"', self.assertRaisesRegexp, Exception, '^Expected$', Stub)
        self.assertRaisesRegexp(self.failureException, '"\\^Expected\\$" does not match "Unexpected"', self.assertRaisesRegexp, Exception, re.compile('^Expected$'), Stub)

    def testAssertRaisesExcValue(self):

        class ExceptionMock(Exception):
            pass

        def Stub(foo):
            raise ExceptionMock(foo)

        v = 'particular value'
        ctx = self.assertRaises(ExceptionMock)
        with ctx:
            Stub(v)
        e = ctx.exception
        self.assertIsInstance(e, ExceptionMock)
        self.assertEqual(e.args[0], v)

    def testSynonymAssertMethodNames(self):
        self.assertNotEquals(3, 5)
        self.assertEquals(3, 3)
        self.assertAlmostEquals(2.0, 2.0)
        self.assertNotAlmostEquals(3.0, 5.0)
        self.assert_(True)

    def testPendingDeprecationMethodNames(self):
        with test_support.check_warnings():
            self.failIfEqual(3, 5)
            self.failUnlessEqual(3, 3)
            self.failUnlessAlmostEqual(2.0, 2.0)
            self.failIfAlmostEqual(3.0, 5.0)
            self.failUnless(True)
            self.failUnlessRaises(TypeError, lambda _: 3.14 + 'spam')
            self.failIf(False)

    def testDeepcopy(self):

        class TestableTest(unittest.TestCase):

            def testNothing(self):
                pass

        test = TestableTest('testNothing')
        deepcopy(test)

    def testKeyboardInterrupt(self):

        def _raise(self=None):
            raise KeyboardInterrupt

        def nothing(self):
            pass

        class Test1(unittest.TestCase):
            test_something = _raise

        class Test2(unittest.TestCase):
            setUp = _raise
            test_something = nothing

        class Test3(unittest.TestCase):
            test_something = nothing
            tearDown = _raise

        class Test4(unittest.TestCase):

            def test_something(self):
                self.addCleanup(_raise)

        for klass in (Test1, Test2, Test3, Test4):
            with self.assertRaises(KeyboardInterrupt):
                klass('test_something').run()

        return

    def testSystemExit(self):

        def _raise(self=None):
            raise SystemExit

        def nothing(self):
            pass

        class Test1(unittest.TestCase):
            test_something = _raise

        class Test2(unittest.TestCase):
            setUp = _raise
            test_something = nothing

        class Test3(unittest.TestCase):
            test_something = nothing
            tearDown = _raise

        class Test4(unittest.TestCase):

            def test_something(self):
                self.addCleanup(_raise)

        for klass in (Test1, Test2, Test3, Test4):
            result = unittest.TestResult()
            klass('test_something').run(result)
            self.assertEqual(len(result.errors), 1)
            self.assertEqual(result.testsRun, 1)

        return

    def testPickle(self):
        test = unittest.TestCase('run')
        for protocol in range(pickle.HIGHEST_PROTOCOL + 1):
            pickled_test = pickle.dumps(test, protocol=protocol)
            unpickled_test = pickle.loads(pickled_test)
            self.assertEqual(test, unpickled_test)


if __name__ == '__main__':
    unittest.main()