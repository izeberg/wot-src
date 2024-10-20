import os, sys, errno
from pprint import pprint
import string, unittest
from test_all import db, test_support, verbose, get_new_environment_path, get_new_database_path

class SimpleRecnoTestCase(unittest.TestCase):
    if sys.version_info < (2, 7) or sys.version_info >= (3, 0) and sys.version_info < (3,
                                                                                       2):

        def assertIsInstance(self, obj, datatype, msg=None):
            return self.assertEqual(type(obj), datatype, msg=msg)

        def assertGreaterEqual(self, a, b, msg=None):
            return self.assertGreaterEqual(a, b, msg=msg)

    def setUp(self):
        self.filename = get_new_database_path()
        self.homeDir = None
        return

    def tearDown(self):
        test_support.unlink(self.filename)
        if self.homeDir:
            test_support.rmtree(self.homeDir)

    def test01_basic(self):
        d = db.DB()
        get_returns_none = d.set_get_returns_none(2)
        d.set_get_returns_none(get_returns_none)
        d.open(self.filename, db.DB_RECNO, db.DB_CREATE)
        for x in string.ascii_letters:
            recno = d.append(x * 60)
            self.assertIsInstance(recno, int)
            self.assertGreaterEqual(recno, 1)
            if verbose:
                print recno,

        if verbose:
            print
        stat = d.stat()
        if verbose:
            pprint(stat)
        for recno in range(1, len(d) + 1):
            data = d[recno]
            if verbose:
                print data
            self.assertIsInstance(data, str)
            self.assertEqual(data, d.get(recno))

        try:
            data = d[0]
        except db.DBInvalidArgError as val:
            if sys.version_info < (2, 6):
                self.assertEqual(val[0], db.EINVAL)
            else:
                self.assertEqual(val.args[0], db.EINVAL)
            if verbose:
                print val
        else:
            self.fail('expected exception')

        try:
            d.has_key(0)
        except db.DBError as val:
            pass
        else:
            self.fail('has_key did not raise a proper exception')

        try:
            data = d[100]
        except KeyError:
            pass
        else:
            self.fail('expected exception')

        try:
            data = d.get(100)
        except db.DBNotFoundError as val:
            if get_returns_none:
                self.fail('unexpected exception')
        else:
            self.assertEqual(data, None)

        keys = d.keys()
        if verbose:
            print keys
        self.assertIsInstance(keys, list)
        self.assertIsInstance(keys[0], int)
        self.assertEqual(len(keys), len(d))
        items = d.items()
        if verbose:
            pprint(items)
        self.assertIsInstance(items, list)
        self.assertIsInstance(items[0], tuple)
        self.assertEqual(len(items[0]), 2)
        self.assertIsInstance(items[0][0], int)
        self.assertIsInstance(items[0][1], str)
        self.assertEqual(len(items), len(d))
        self.assertTrue(d.has_key(25))
        del d[25]
        self.assertFalse(d.has_key(25))
        d.delete(13)
        self.assertFalse(d.has_key(13))
        data = d.get_both(26, 'z' * 60)
        self.assertEqual(data, 'z' * 60, 'was %r' % data)
        if verbose:
            print data
        fd = d.fd()
        if verbose:
            print fd
        c = d.cursor()
        rec = c.first()
        while rec:
            if verbose:
                print rec
            rec = c.next()

        c.set(50)
        rec = c.current()
        if verbose:
            print rec
        c.put(-1, 'a replacement record', db.DB_CURRENT)
        c.set(50)
        rec = c.current()
        self.assertEqual(rec, (50, 'a replacement record'))
        if verbose:
            print rec
        rec = c.set_range(30)
        if verbose:
            print rec
        rec = c.set_range(999999)
        self.assertEqual(rec, None)
        if verbose:
            print rec
        c.close()
        d.close()
        d = db.DB()
        d.open(self.filename)
        c = d.cursor()
        d[100] = 'way out there'
        self.assertEqual(d[100], 'way out there')
        try:
            data = d[99]
        except KeyError:
            pass
        else:
            self.fail('expected exception')

        try:
            d.get(99)
        except db.DBKeyEmptyError as val:
            if get_returns_none:
                self.fail('unexpected DBKeyEmptyError exception')
            else:
                if sys.version_info < (2, 6):
                    self.assertEqual(val[0], db.DB_KEYEMPTY)
                else:
                    self.assertEqual(val.args[0], db.DB_KEYEMPTY)
                if verbose:
                    print val
        else:
            if not get_returns_none:
                self.fail('expected exception')
            rec = c.set(40)
            while rec:
                if verbose:
                    print rec
                rec = c.next()

        c.close()
        d.close()
        return

    def test02_WithSource(self):
        homeDir = get_new_environment_path()
        self.homeDir = homeDir
        source = os.path.join(homeDir, 'test_recno.txt')
        if not os.path.isdir(homeDir):
            os.mkdir(homeDir)
        f = open(source, 'w')
        f.close()
        d = db.DB()
        d.set_re_delim(10)
        d.set_re_delim('\n')
        d.set_re_source(source)
        d.open(self.filename, db.DB_RECNO, db.DB_CREATE)
        data = ('The quick brown fox jumped over the lazy dog').split()
        for datum in data:
            d.append(datum)

        d.sync()
        d.close()
        f = open(source, 'r')
        text = f.read()
        f.close()
        text = text.strip()
        if verbose:
            print text
            print data
            print text.split('\n')
        self.assertEqual(text.split('\n'), data)
        d = db.DB()
        d.set_re_source(source)
        d.open(self.filename, db.DB_RECNO)
        d[3] = 'reddish-brown'
        d[8] = 'comatose'
        d.sync()
        d.close()
        f = open(source, 'r')
        text = f.read()
        f.close()
        text = text.strip()
        if verbose:
            print text
            print text.split('\n')
        self.assertEqual(text.split('\n'), ('The quick reddish-brown fox jumped over the comatose dog').split())

    def test03_FixedLength(self):
        d = db.DB()
        d.set_re_len(40)
        d.set_re_pad('-')
        d.set_re_pad(45)
        d.open(self.filename, db.DB_RECNO, db.DB_CREATE)
        for x in string.ascii_letters:
            d.append(x * 35)

        d.append('.' * 40)
        try:
            d.append('bad' * 20)
        except db.DBInvalidArgError as val:
            if sys.version_info < (2, 6):
                self.assertEqual(val[0], db.EINVAL)
            else:
                self.assertEqual(val.args[0], db.EINVAL)
            if verbose:
                print val
        else:
            self.fail('expected exception')

        c = d.cursor()
        rec = c.first()
        while rec:
            if verbose:
                print rec
            rec = c.next()

        c.close()
        d.close()

    def test04_get_size_empty(self):
        d = db.DB()
        d.open(self.filename, dbtype=db.DB_RECNO, flags=db.DB_CREATE)
        row_id = d.append(' ')
        self.assertEqual(1, d.get_size(key=row_id))
        row_id = d.append('')
        self.assertEqual(0, d.get_size(key=row_id))


def test_suite():
    return unittest.makeSuite(SimpleRecnoTestCase)


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')