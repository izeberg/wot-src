import os, string, unittest
from test_all import db, verbose, get_new_database_path

class GetReturnsNoneTestCase(unittest.TestCase):

    def setUp(self):
        self.filename = get_new_database_path()

    def tearDown(self):
        try:
            os.remove(self.filename)
        except os.error:
            pass

    def test01_get_returns_none(self):
        d = db.DB()
        d.open(self.filename, db.DB_BTREE, db.DB_CREATE)
        d.set_get_returns_none(1)
        for x in string.ascii_letters:
            d.put(x, x * 40)

        data = d.get('bad key')
        self.assertEqual(data, None)
        data = d.get(string.ascii_letters[0])
        self.assertEqual(data, string.ascii_letters[0] * 40)
        count = 0
        c = d.cursor()
        rec = c.first()
        while rec:
            count = count + 1
            rec = c.next()

        self.assertEqual(rec, None)
        self.assertEqual(count, len(string.ascii_letters))
        c.close()
        d.close()
        return

    def test02_get_raises_exception(self):
        d = db.DB()
        d.open(self.filename, db.DB_BTREE, db.DB_CREATE)
        d.set_get_returns_none(0)
        for x in string.ascii_letters:
            d.put(x, x * 40)

        self.assertRaises(db.DBNotFoundError, d.get, 'bad key')
        self.assertRaises(KeyError, d.get, 'bad key')
        data = d.get(string.ascii_letters[0])
        self.assertEqual(data, string.ascii_letters[0] * 40)
        count = 0
        exceptionHappened = 0
        c = d.cursor()
        rec = c.first()
        while rec:
            count = count + 1
            try:
                rec = c.next()
            except db.DBNotFoundError:
                exceptionHappened = 1
                break

        self.assertNotEqual(rec, None)
        self.assertTrue(exceptionHappened)
        self.assertEqual(count, len(string.ascii_letters))
        c.close()
        d.close()
        return


def test_suite():
    return unittest.makeSuite(GetReturnsNoneTestCase)


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')