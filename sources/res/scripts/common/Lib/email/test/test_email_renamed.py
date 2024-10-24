import os, sys, time, base64, difflib, unittest, warnings
from cStringIO import StringIO
import email
from email.charset import Charset
from email.header import Header, decode_header, make_header
from email.parser import Parser, HeaderParser
from email.generator import Generator, DecodedGenerator
from email.message import Message
from email.mime.application import MIMEApplication
from email.mime.audio import MIMEAudio
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.message import MIMEMessage
from email.mime.multipart import MIMEMultipart
from email import utils
from email import errors
from email import encoders
from email import iterators
from email import base64mime
from email import quoprimime
from test.test_support import findfile, run_unittest
from email.test import __file__ as landmark
NL = '\n'
EMPTYSTRING = ''
SPACE = ' '

def openfile(filename, mode='r'):
    path = os.path.join(os.path.dirname(landmark), 'data', filename)
    return open(path, mode)


class TestEmailBase(unittest.TestCase):

    def ndiffAssertEqual(self, first, second):
        if first != second:
            sfirst = str(first)
            ssecond = str(second)
            diff = difflib.ndiff(sfirst.splitlines(), ssecond.splitlines())
            fp = StringIO()
            print >> fp, NL, NL.join(diff)
            raise self.failureException, fp.getvalue()

    def _msgobj(self, filename):
        fp = openfile(findfile(filename))
        try:
            msg = email.message_from_file(fp)
        finally:
            fp.close()

        return msg


class TestMessageAPI(TestEmailBase):

    def test_get_all(self):
        eq = self.assertEqual
        msg = self._msgobj('msg_20.txt')
        eq(msg.get_all('cc'), ['ccc@zzz.org', 'ddd@zzz.org', 'eee@zzz.org'])
        eq(msg.get_all('xx', 'n/a'), 'n/a')

    def test_getset_charset(self):
        eq = self.assertEqual
        msg = Message()
        eq(msg.get_charset(), None)
        charset = Charset('iso-8859-1')
        msg.set_charset(charset)
        eq(msg['mime-version'], '1.0')
        eq(msg.get_content_type(), 'text/plain')
        eq(msg['content-type'], 'text/plain; charset="iso-8859-1"')
        eq(msg.get_param('charset'), 'iso-8859-1')
        eq(msg['content-transfer-encoding'], 'quoted-printable')
        eq(msg.get_charset().input_charset, 'iso-8859-1')
        msg.set_charset(None)
        eq(msg.get_charset(), None)
        eq(msg['content-type'], 'text/plain')
        msg = Message()
        msg['MIME-Version'] = '2.0'
        msg['Content-Type'] = 'text/x-weird'
        msg['Content-Transfer-Encoding'] = 'quinted-puntable'
        msg.set_charset(charset)
        eq(msg['mime-version'], '2.0')
        eq(msg['content-type'], 'text/x-weird; charset="iso-8859-1"')
        eq(msg['content-transfer-encoding'], 'quinted-puntable')
        return

    def test_set_charset_from_string(self):
        eq = self.assertEqual
        msg = Message()
        msg.set_charset('us-ascii')
        eq(msg.get_charset().input_charset, 'us-ascii')
        eq(msg['content-type'], 'text/plain; charset="us-ascii"')

    def test_set_payload_with_charset(self):
        msg = Message()
        charset = Charset('iso-8859-1')
        msg.set_payload('This is a string payload', charset)
        self.assertEqual(msg.get_charset().input_charset, 'iso-8859-1')

    def test_get_charsets(self):
        eq = self.assertEqual
        msg = self._msgobj('msg_08.txt')
        charsets = msg.get_charsets()
        eq(charsets, [None, 'us-ascii', 'iso-8859-1', 'iso-8859-2', 'koi8-r'])
        msg = self._msgobj('msg_09.txt')
        charsets = msg.get_charsets('dingbat')
        eq(charsets, ['dingbat', 'us-ascii', 'iso-8859-1', 'dingbat',
         'koi8-r'])
        msg = self._msgobj('msg_12.txt')
        charsets = msg.get_charsets()
        eq(charsets, [None, 'us-ascii', 'iso-8859-1', None, 'iso-8859-2',
         'iso-8859-3', 'us-ascii', 'koi8-r'])
        return

    def test_get_filename(self):
        eq = self.assertEqual
        msg = self._msgobj('msg_04.txt')
        filenames = [ p.get_filename() for p in msg.get_payload() ]
        eq(filenames, ['msg.txt', 'msg.txt'])
        msg = self._msgobj('msg_07.txt')
        subpart = msg.get_payload(1)
        eq(subpart.get_filename(), 'dingusfish.gif')

    def test_get_filename_with_name_parameter(self):
        eq = self.assertEqual
        msg = self._msgobj('msg_44.txt')
        filenames = [ p.get_filename() for p in msg.get_payload() ]
        eq(filenames, ['msg.txt', 'msg.txt'])

    def test_get_boundary(self):
        eq = self.assertEqual
        msg = self._msgobj('msg_07.txt')
        eq(msg.get_boundary(), 'BOUNDARY')

    def test_set_boundary(self):
        eq = self.assertEqual
        msg = self._msgobj('msg_01.txt')
        msg.set_boundary('BOUNDARY')
        header, value = msg.items()[4]
        eq(header.lower(), 'content-type')
        eq(value, 'text/plain; charset="us-ascii"; boundary="BOUNDARY"')
        msg = self._msgobj('msg_04.txt')
        msg.set_boundary('BOUNDARY')
        header, value = msg.items()[4]
        eq(header.lower(), 'content-type')
        eq(value, 'multipart/mixed; boundary="BOUNDARY"')
        msg = self._msgobj('msg_03.txt')
        self.assertRaises(errors.HeaderParseError, msg.set_boundary, 'BOUNDARY')

    def test_get_decoded_payload(self):
        eq = self.assertEqual
        msg = self._msgobj('msg_10.txt')
        eq(msg.get_payload(decode=True), None)
        eq(msg.get_payload(0).get_payload(decode=True), 'This is a 7bit encoded message.\n')
        eq(msg.get_payload(1).get_payload(decode=True), b'\xa1This is a Quoted Printable encoded message!\n')
        eq(msg.get_payload(2).get_payload(decode=True), 'This is a Base64 encoded message.')
        eq(msg.get_payload(3).get_payload(decode=True), 'This is a Base64 encoded message.\n')
        eq(msg.get_payload(4).get_payload(decode=True), 'This has no Content-Transfer-Encoding: header.\n')
        return

    def test_get_decoded_uu_payload(self):
        eq = self.assertEqual
        msg = Message()
        msg.set_payload('begin 666 -\n+:&5L;&\\@=V]R;&0 \n \nend\n')
        for cte in ('x-uuencode', 'uuencode', 'uue', 'x-uue'):
            msg['content-transfer-encoding'] = cte
            eq(msg.get_payload(decode=True), 'hello world')

        msg.set_payload('foo')
        eq(msg.get_payload(decode=True), 'foo')

    def test_decoded_generator(self):
        eq = self.assertEqual
        msg = self._msgobj('msg_07.txt')
        fp = openfile('msg_17.txt')
        try:
            text = fp.read()
        finally:
            fp.close()

        s = StringIO()
        g = DecodedGenerator(s)
        g.flatten(msg)
        eq(s.getvalue(), text)

    def test__contains__(self):
        msg = Message()
        msg['From'] = 'Me'
        msg['to'] = 'You'
        self.assertIn('from', msg)
        self.assertIn('From', msg)
        self.assertIn('FROM', msg)
        self.assertIn('to', msg)
        self.assertIn('To', msg)
        self.assertIn('TO', msg)

    def test_as_string(self):
        eq = self.assertEqual
        msg = self._msgobj('msg_01.txt')
        fp = openfile('msg_01.txt')
        try:
            text = fp.read().replace('\t', ' ')
        finally:
            fp.close()

        self.ndiffAssertEqual(text, msg.as_string())
        fullrepr = str(msg)
        lines = fullrepr.split('\n')
        self.assertTrue(lines[0].startswith('From '))
        eq(text, NL.join(lines[1:]))

    def test_bad_param(self):
        msg = email.message_from_string('Content-Type: blarg; baz; boo\n')
        self.assertEqual(msg.get_param('baz'), '')

    def test_missing_filename(self):
        msg = email.message_from_string('From: foo\n')
        self.assertEqual(msg.get_filename(), None)
        return

    def test_bogus_filename(self):
        msg = email.message_from_string('Content-Disposition: blarg; filename\n')
        self.assertEqual(msg.get_filename(), '')

    def test_missing_boundary(self):
        msg = email.message_from_string('From: foo\n')
        self.assertEqual(msg.get_boundary(), None)
        return

    def test_get_params(self):
        eq = self.assertEqual
        msg = email.message_from_string('X-Header: foo=one; bar=two; baz=three\n')
        eq(msg.get_params(header='x-header'), [
         ('foo', 'one'), ('bar', 'two'), ('baz', 'three')])
        msg = email.message_from_string('X-Header: foo; bar=one; baz=two\n')
        eq(msg.get_params(header='x-header'), [
         ('foo', ''), ('bar', 'one'), ('baz', 'two')])
        eq(msg.get_params(), None)
        msg = email.message_from_string('X-Header: foo; bar="one"; baz=two\n')
        eq(msg.get_params(header='x-header'), [
         ('foo', ''), ('bar', 'one'), ('baz', 'two')])
        return

    def test_get_param_liberal(self):
        msg = Message()
        msg['Content-Type'] = 'Content-Type: Multipart/mixed; boundary = "CPIMSSMTPC06p5f3tG"'
        self.assertEqual(msg.get_param('boundary'), 'CPIMSSMTPC06p5f3tG')

    def test_get_param(self):
        eq = self.assertEqual
        msg = email.message_from_string('X-Header: foo=one; bar=two; baz=three\n')
        eq(msg.get_param('bar', header='x-header'), 'two')
        eq(msg.get_param('quuz', header='x-header'), None)
        eq(msg.get_param('quuz'), None)
        msg = email.message_from_string('X-Header: foo; bar="one"; baz=two\n')
        eq(msg.get_param('foo', header='x-header'), '')
        eq(msg.get_param('bar', header='x-header'), 'one')
        eq(msg.get_param('baz', header='x-header'), 'two')
        return

    def test_get_param_funky_continuation_lines(self):
        msg = self._msgobj('msg_22.txt')
        self.assertEqual(msg.get_payload(1).get_param('name'), 'wibble.JPG')

    def test_get_param_with_semis_in_quotes(self):
        msg = email.message_from_string('Content-Type: image/pjpeg; name="Jim&amp;&amp;Jill"\n')
        self.assertEqual(msg.get_param('name'), 'Jim&amp;&amp;Jill')
        self.assertEqual(msg.get_param('name', unquote=False), '"Jim&amp;&amp;Jill"')

    def test_has_key(self):
        msg = email.message_from_string('Header: exists')
        self.assertTrue(msg.has_key('header'))
        self.assertTrue(msg.has_key('Header'))
        self.assertTrue(msg.has_key('HEADER'))
        self.assertFalse(msg.has_key('headeri'))

    def test_set_param(self):
        eq = self.assertEqual
        msg = Message()
        msg.set_param('charset', 'iso-2022-jp')
        eq(msg.get_param('charset'), 'iso-2022-jp')
        msg.set_param('importance', 'high value')
        eq(msg.get_param('importance'), 'high value')
        eq(msg.get_param('importance', unquote=False), '"high value"')
        eq(msg.get_params(), [('text/plain', ''),
         ('charset', 'iso-2022-jp'),
         ('importance', 'high value')])
        eq(msg.get_params(unquote=False), [('text/plain', ''),
         ('charset', '"iso-2022-jp"'),
         ('importance', '"high value"')])
        msg.set_param('charset', 'iso-9999-xx', header='X-Jimmy')
        eq(msg.get_param('charset', header='X-Jimmy'), 'iso-9999-xx')

    def test_del_param(self):
        eq = self.assertEqual
        msg = self._msgobj('msg_05.txt')
        eq(msg.get_params(), [
         ('multipart/report', ''), ('report-type', 'delivery-status'),
         ('boundary', 'D1690A7AC1.996856090/mail.example.com')])
        old_val = msg.get_param('report-type')
        msg.del_param('report-type')
        eq(msg.get_params(), [
         ('multipart/report', ''),
         ('boundary', 'D1690A7AC1.996856090/mail.example.com')])
        msg.set_param('report-type', old_val)
        eq(msg.get_params(), [
         ('multipart/report', ''),
         ('boundary', 'D1690A7AC1.996856090/mail.example.com'),
         (
          'report-type', old_val)])

    def test_del_param_on_other_header(self):
        msg = Message()
        msg.add_header('Content-Disposition', 'attachment', filename='bud.gif')
        msg.del_param('filename', 'content-disposition')
        self.assertEqual(msg['content-disposition'], 'attachment')

    def test_set_type(self):
        eq = self.assertEqual
        msg = Message()
        self.assertRaises(ValueError, msg.set_type, 'text')
        msg.set_type('text/plain')
        eq(msg['content-type'], 'text/plain')
        msg.set_param('charset', 'us-ascii')
        eq(msg['content-type'], 'text/plain; charset="us-ascii"')
        msg.set_type('text/html')
        eq(msg['content-type'], 'text/html; charset="us-ascii"')

    def test_set_type_on_other_header(self):
        msg = Message()
        msg['X-Content-Type'] = 'text/plain'
        msg.set_type('application/octet-stream', 'X-Content-Type')
        self.assertEqual(msg['x-content-type'], 'application/octet-stream')

    def test_get_content_type_missing(self):
        msg = Message()
        self.assertEqual(msg.get_content_type(), 'text/plain')

    def test_get_content_type_missing_with_default_type(self):
        msg = Message()
        msg.set_default_type('message/rfc822')
        self.assertEqual(msg.get_content_type(), 'message/rfc822')

    def test_get_content_type_from_message_implicit(self):
        msg = self._msgobj('msg_30.txt')
        self.assertEqual(msg.get_payload(0).get_content_type(), 'message/rfc822')

    def test_get_content_type_from_message_explicit(self):
        msg = self._msgobj('msg_28.txt')
        self.assertEqual(msg.get_payload(0).get_content_type(), 'message/rfc822')

    def test_get_content_type_from_message_text_plain_implicit(self):
        msg = self._msgobj('msg_03.txt')
        self.assertEqual(msg.get_content_type(), 'text/plain')

    def test_get_content_type_from_message_text_plain_explicit(self):
        msg = self._msgobj('msg_01.txt')
        self.assertEqual(msg.get_content_type(), 'text/plain')

    def test_get_content_maintype_missing(self):
        msg = Message()
        self.assertEqual(msg.get_content_maintype(), 'text')

    def test_get_content_maintype_missing_with_default_type(self):
        msg = Message()
        msg.set_default_type('message/rfc822')
        self.assertEqual(msg.get_content_maintype(), 'message')

    def test_get_content_maintype_from_message_implicit(self):
        msg = self._msgobj('msg_30.txt')
        self.assertEqual(msg.get_payload(0).get_content_maintype(), 'message')

    def test_get_content_maintype_from_message_explicit(self):
        msg = self._msgobj('msg_28.txt')
        self.assertEqual(msg.get_payload(0).get_content_maintype(), 'message')

    def test_get_content_maintype_from_message_text_plain_implicit(self):
        msg = self._msgobj('msg_03.txt')
        self.assertEqual(msg.get_content_maintype(), 'text')

    def test_get_content_maintype_from_message_text_plain_explicit(self):
        msg = self._msgobj('msg_01.txt')
        self.assertEqual(msg.get_content_maintype(), 'text')

    def test_get_content_subtype_missing(self):
        msg = Message()
        self.assertEqual(msg.get_content_subtype(), 'plain')

    def test_get_content_subtype_missing_with_default_type(self):
        msg = Message()
        msg.set_default_type('message/rfc822')
        self.assertEqual(msg.get_content_subtype(), 'rfc822')

    def test_get_content_subtype_from_message_implicit(self):
        msg = self._msgobj('msg_30.txt')
        self.assertEqual(msg.get_payload(0).get_content_subtype(), 'rfc822')

    def test_get_content_subtype_from_message_explicit(self):
        msg = self._msgobj('msg_28.txt')
        self.assertEqual(msg.get_payload(0).get_content_subtype(), 'rfc822')

    def test_get_content_subtype_from_message_text_plain_implicit(self):
        msg = self._msgobj('msg_03.txt')
        self.assertEqual(msg.get_content_subtype(), 'plain')

    def test_get_content_subtype_from_message_text_plain_explicit(self):
        msg = self._msgobj('msg_01.txt')
        self.assertEqual(msg.get_content_subtype(), 'plain')

    def test_get_content_maintype_error(self):
        msg = Message()
        msg['Content-Type'] = 'no-slash-in-this-string'
        self.assertEqual(msg.get_content_maintype(), 'text')

    def test_get_content_subtype_error(self):
        msg = Message()
        msg['Content-Type'] = 'no-slash-in-this-string'
        self.assertEqual(msg.get_content_subtype(), 'plain')

    def test_replace_header(self):
        eq = self.assertEqual
        msg = Message()
        msg.add_header('First', 'One')
        msg.add_header('Second', 'Two')
        msg.add_header('Third', 'Three')
        eq(msg.keys(), ['First', 'Second', 'Third'])
        eq(msg.values(), ['One', 'Two', 'Three'])
        msg.replace_header('Second', 'Twenty')
        eq(msg.keys(), ['First', 'Second', 'Third'])
        eq(msg.values(), ['One', 'Twenty', 'Three'])
        msg.add_header('First', 'Eleven')
        msg.replace_header('First', 'One Hundred')
        eq(msg.keys(), ['First', 'Second', 'Third', 'First'])
        eq(msg.values(), ['One Hundred', 'Twenty', 'Three', 'Eleven'])
        self.assertRaises(KeyError, msg.replace_header, 'Fourth', 'Missing')

    def test_broken_base64_payload(self):
        x = 'AwDp0P7//y6LwKEAcPa/6Q=9'
        msg = Message()
        msg['content-type'] = 'audio/x-midi'
        msg['content-transfer-encoding'] = 'base64'
        msg.set_payload(x)
        self.assertEqual(msg.get_payload(decode=True), x)


class TestEncoders(unittest.TestCase):

    def test_encode_empty_payload(self):
        eq = self.assertEqual
        msg = Message()
        msg.set_charset('us-ascii')
        eq(msg['content-transfer-encoding'], '7bit')

    def test_default_cte(self):
        eq = self.assertEqual
        msg = MIMEText('hello world')
        eq(msg['content-transfer-encoding'], '7bit')
        msg = MIMEText(b'hello \xf8 world')
        eq(msg['content-transfer-encoding'], '8bit')
        msg = MIMEText(b'hello \xf8 world', _charset='iso-8859-1')
        eq(msg['content-transfer-encoding'], 'quoted-printable')


class TestLongHeaders(TestEmailBase):

    def test_split_long_continuation(self):
        eq = self.ndiffAssertEqual
        msg = email.message_from_string('Subject: bug demonstration\n\t12345678911234567892123456789312345678941234567895123456789612345678971234567898112345678911234567892123456789112345678911234567892123456789\n\tmore text\n\ntest\n')
        sfp = StringIO()
        g = Generator(sfp)
        g.flatten(msg)
        eq(sfp.getvalue(), 'Subject: bug demonstration\n 12345678911234567892123456789312345678941234567895123456789612345678971234567898112345678911234567892123456789112345678911234567892123456789\n more text\n\ntest\n')

    def test_another_long_almost_unsplittable_header(self):
        eq = self.ndiffAssertEqual
        hstr = 'bug demonstration\n\t12345678911234567892123456789312345678941234567895123456789612345678971234567898112345678911234567892123456789112345678911234567892123456789\n\tmore text'
        h = Header(hstr, continuation_ws='\t')
        eq(h.encode(), 'bug demonstration\n\t12345678911234567892123456789312345678941234567895123456789612345678971234567898112345678911234567892123456789112345678911234567892123456789\n\tmore text')
        h = Header(hstr)
        eq(h.encode(), 'bug demonstration\n 12345678911234567892123456789312345678941234567895123456789612345678971234567898112345678911234567892123456789112345678911234567892123456789\n more text')

    def test_long_nonstring(self):
        eq = self.ndiffAssertEqual
        g = Charset('iso-8859-1')
        cz = Charset('iso-8859-2')
        utf8 = Charset('utf-8')
        g_head = b'Die Mieter treten hier ein werden mit einem Foerderband komfortabel den Korridor entlang, an s\xfcdl\xfcndischen Wandgem\xe4lden vorbei, gegen die rotierenden Klingen bef\xf6rdert. '
        cz_head = b'Finan\xe8ni metropole se hroutily pod tlakem jejich d\xf9vtipu.. '
        utf8_head = ('正確に言うと翻訳はされていません。一部はドイツ語ですが、あとはでたらめです。実際には「Wenn ist das Nunstuck git und Slotermeyer? Ja! Beiherhund das Oder die Flipperwaldt gersput.」と言っています。').encode('utf-8')
        h = Header(g_head, g, header_name='Subject')
        h.append(cz_head, cz)
        h.append(utf8_head, utf8)
        msg = Message()
        msg['Subject'] = h
        sfp = StringIO()
        g = Generator(sfp)
        g.flatten(msg)
        eq(sfp.getvalue(), 'Subject: =?iso-8859-1?q?Die_Mieter_treten_hier_ein_werden_mit_einem_Foerd?=\n =?iso-8859-1?q?erband_komfortabel_den_Korridor_entlang=2C_an_s=FCdl=FCndi?=\n =?iso-8859-1?q?schen_Wandgem=E4lden_vorbei=2C_gegen_die_rotierenden_Kling?=\n =?iso-8859-1?q?en_bef=F6rdert=2E_?= =?iso-8859-2?q?Finan=E8ni_met?=\n =?iso-8859-2?q?ropole_se_hroutily_pod_tlakem_jejich_d=F9vtipu=2E=2E_?=\n =?utf-8?b?5q2j56K644Gr6KiA44GG44Go57+76Kiz44Gv44GV44KM44Gm44GE?=\n =?utf-8?b?44G+44Gb44KT44CC5LiA6YOo44Gv44OJ44Kk44OE6Kqe44Gn44GZ44GM44CB?=\n =?utf-8?b?44GC44Go44Gv44Gn44Gf44KJ44KB44Gn44GZ44CC5a6f6Zqb44Gr44Gv44CM?=\n =?utf-8?q?Wenn_ist_das_Nunstuck_git_und_Slotermeyer=3F_Ja!_Beiherhund_das?=\n =?utf-8?b?IE9kZXIgZGllIEZsaXBwZXJ3YWxkdCBnZXJzcHV0LuOAjeOBqOiogOOBow==?=\n =?utf-8?b?44Gm44GE44G+44GZ44CC?=\n\n')
        eq(h.encode(), '=?iso-8859-1?q?Die_Mieter_treten_hier_ein_werden_mit_einem_Foerd?=\n =?iso-8859-1?q?erband_komfortabel_den_Korridor_entlang=2C_an_s=FCdl=FCndi?=\n =?iso-8859-1?q?schen_Wandgem=E4lden_vorbei=2C_gegen_die_rotierenden_Kling?=\n =?iso-8859-1?q?en_bef=F6rdert=2E_?= =?iso-8859-2?q?Finan=E8ni_met?=\n =?iso-8859-2?q?ropole_se_hroutily_pod_tlakem_jejich_d=F9vtipu=2E=2E_?=\n =?utf-8?b?5q2j56K644Gr6KiA44GG44Go57+76Kiz44Gv44GV44KM44Gm44GE?=\n =?utf-8?b?44G+44Gb44KT44CC5LiA6YOo44Gv44OJ44Kk44OE6Kqe44Gn44GZ44GM44CB?=\n =?utf-8?b?44GC44Go44Gv44Gn44Gf44KJ44KB44Gn44GZ44CC5a6f6Zqb44Gr44Gv44CM?=\n =?utf-8?q?Wenn_ist_das_Nunstuck_git_und_Slotermeyer=3F_Ja!_Beiherhund_das?=\n =?utf-8?b?IE9kZXIgZGllIEZsaXBwZXJ3YWxkdCBnZXJzcHV0LuOAjeOBqOiogOOBow==?=\n =?utf-8?b?44Gm44GE44G+44GZ44CC?=')

    def test_long_header_encode(self):
        eq = self.ndiffAssertEqual
        h = Header('wasnipoop; giraffes="very-long-necked-animals"; spooge="yummy"; hippos="gargantuan"; marshmallows="gooey"', header_name='X-Foobar-Spoink-Defrobnit')
        eq(h.encode(), 'wasnipoop; giraffes="very-long-necked-animals";\n spooge="yummy"; hippos="gargantuan"; marshmallows="gooey"')

    def test_long_header_encode_with_tab_continuation(self):
        eq = self.ndiffAssertEqual
        h = Header('wasnipoop; giraffes="very-long-necked-animals"; spooge="yummy"; hippos="gargantuan"; marshmallows="gooey"', header_name='X-Foobar-Spoink-Defrobnit', continuation_ws='\t')
        eq(h.encode(), 'wasnipoop; giraffes="very-long-necked-animals";\n\tspooge="yummy"; hippos="gargantuan"; marshmallows="gooey"')

    def test_header_splitter(self):
        eq = self.ndiffAssertEqual
        msg = MIMEText('')
        msg['X-Foobar-Spoink-Defrobnit'] = 'wasnipoop; giraffes="very-long-necked-animals"; spooge="yummy"; hippos="gargantuan"; marshmallows="gooey"'
        sfp = StringIO()
        g = Generator(sfp)
        g.flatten(msg)
        eq(sfp.getvalue(), 'Content-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\nX-Foobar-Spoink-Defrobnit: wasnipoop; giraffes="very-long-necked-animals";\n spooge="yummy"; hippos="gargantuan"; marshmallows="gooey"\n\n')

    def test_no_semis_header_splitter(self):
        eq = self.ndiffAssertEqual
        msg = Message()
        msg['From'] = 'test@dom.ain'
        msg['References'] = SPACE.join([ '<%d@dom.ain>' % i for i in range(10) ])
        msg.set_payload('Test')
        sfp = StringIO()
        g = Generator(sfp)
        g.flatten(msg)
        eq(sfp.getvalue(), 'From: test@dom.ain\nReferences: <0@dom.ain> <1@dom.ain> <2@dom.ain> <3@dom.ain> <4@dom.ain>\n <5@dom.ain> <6@dom.ain> <7@dom.ain> <8@dom.ain> <9@dom.ain>\n\nTest')

    def test_no_split_long_header(self):
        eq = self.ndiffAssertEqual
        hstr = 'References: ' + 'x' * 80
        h = Header(hstr, continuation_ws='\t')
        eq(h.encode(), 'References: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    def test_splitting_multiple_long_lines(self):
        eq = self.ndiffAssertEqual
        hstr = 'from babylon.socal-raves.org (localhost [127.0.0.1]); by babylon.socal-raves.org (Postfix) with ESMTP id B570E51B81; for <mailman-admin@babylon.socal-raves.org>; Sat, 2 Feb 2002 17:00:06 -0800 (PST)\n\tfrom babylon.socal-raves.org (localhost [127.0.0.1]); by babylon.socal-raves.org (Postfix) with ESMTP id B570E51B81; for <mailman-admin@babylon.socal-raves.org>; Sat, 2 Feb 2002 17:00:06 -0800 (PST)\n\tfrom babylon.socal-raves.org (localhost [127.0.0.1]); by babylon.socal-raves.org (Postfix) with ESMTP id B570E51B81; for <mailman-admin@babylon.socal-raves.org>; Sat, 2 Feb 2002 17:00:06 -0800 (PST)\n'
        h = Header(hstr, continuation_ws='\t')
        eq(h.encode(), 'from babylon.socal-raves.org (localhost [127.0.0.1]);\n\tby babylon.socal-raves.org (Postfix) with ESMTP id B570E51B81;\n\tfor <mailman-admin@babylon.socal-raves.org>;\n\tSat, 2 Feb 2002 17:00:06 -0800 (PST)\n\tfrom babylon.socal-raves.org (localhost [127.0.0.1]);\n\tby babylon.socal-raves.org (Postfix) with ESMTP id B570E51B81;\n\tfor <mailman-admin@babylon.socal-raves.org>;\n\tSat, 2 Feb 2002 17:00:06 -0800 (PST)\n\tfrom babylon.socal-raves.org (localhost [127.0.0.1]);\n\tby babylon.socal-raves.org (Postfix) with ESMTP id B570E51B81;\n\tfor <mailman-admin@babylon.socal-raves.org>;\n\tSat, 2 Feb 2002 17:00:06 -0800 (PST)')

    def test_splitting_first_line_only_is_long(self):
        eq = self.ndiffAssertEqual
        hstr = 'from modemcable093.139-201-24.que.mc.videotron.ca ([24.201.139.93] helo=cthulhu.gerg.ca)\n\tby kronos.mems-exchange.org with esmtp (Exim 4.05)\n\tid 17k4h5-00034i-00\n\tfor test@mems-exchange.org; Wed, 28 Aug 2002 11:25:20 -0400'
        h = Header(hstr, maxlinelen=78, header_name='Received', continuation_ws='\t')
        eq(h.encode(), 'from modemcable093.139-201-24.que.mc.videotron.ca ([24.201.139.93]\n\thelo=cthulhu.gerg.ca)\n\tby kronos.mems-exchange.org with esmtp (Exim 4.05)\n\tid 17k4h5-00034i-00\n\tfor test@mems-exchange.org; Wed, 28 Aug 2002 11:25:20 -0400')

    def test_long_8bit_header(self):
        eq = self.ndiffAssertEqual
        msg = Message()
        h = Header('Britische Regierung gibt', 'iso-8859-1', header_name='Subject')
        h.append(b'gr\xfcnes Licht f\xfcr Offshore-Windkraftprojekte')
        msg['Subject'] = h
        eq(msg.as_string(), 'Subject: =?iso-8859-1?q?Britische_Regierung_gibt?= =?iso-8859-1?q?gr=FCnes?=\n =?iso-8859-1?q?_Licht_f=FCr_Offshore-Windkraftprojekte?=\n\n')

    def test_long_8bit_header_no_charset(self):
        eq = self.ndiffAssertEqual
        msg = Message()
        msg['Reply-To'] = b'Britische Regierung gibt gr\xfcnes Licht f\xfcr Offshore-Windkraftprojekte <a-very-long-address@example.com>'
        eq(msg.as_string(), b'Reply-To: Britische Regierung gibt gr\xfcnes Licht f\xfcr Offshore-Windkraftprojekte <a-very-long-address@example.com>\n\n')

    def test_long_to_header(self):
        eq = self.ndiffAssertEqual
        to = '"Someone Test #A" <someone@eecs.umich.edu>,<someone@eecs.umich.edu>,"Someone Test #B" <someone@umich.edu>, "Someone Test #C" <someone@eecs.umich.edu>, "Someone Test #D" <someone@eecs.umich.edu>'
        msg = Message()
        msg['To'] = to
        eq(msg.as_string(0), 'To: "Someone Test #A" <someone@eecs.umich.edu>, <someone@eecs.umich.edu>,\n "Someone Test #B" <someone@umich.edu>,\n "Someone Test #C" <someone@eecs.umich.edu>,\n "Someone Test #D" <someone@eecs.umich.edu>\n\n')

    def test_long_line_after_append(self):
        eq = self.ndiffAssertEqual
        s = 'This is an example of string which has almost the limit of header length.'
        h = Header(s)
        h.append('Add another line.')
        eq(h.encode(), 'This is an example of string which has almost the limit of header length.\n Add another line.')

    def test_shorter_line_with_append(self):
        eq = self.ndiffAssertEqual
        s = 'This is a shorter line.'
        h = Header(s)
        h.append('Add another sentence. (Surprise?)')
        eq(h.encode(), 'This is a shorter line. Add another sentence. (Surprise?)')

    def test_long_field_name(self):
        eq = self.ndiffAssertEqual
        fn = 'X-Very-Very-Very-Long-Header-Name'
        gs = b'Die Mieter treten hier ein werden mit einem Foerderband komfortabel den Korridor entlang, an s\xfcdl\xfcndischen Wandgem\xe4lden vorbei, gegen die rotierenden Klingen bef\xf6rdert. '
        h = Header(gs, 'iso-8859-1', header_name=fn)
        eq(h.encode(), '=?iso-8859-1?q?Die_Mieter_treten_hier_?=\n =?iso-8859-1?q?ein_werden_mit_einem_Foerderband_komfortabel_den_Korridor_?=\n =?iso-8859-1?q?entlang=2C_an_s=FCdl=FCndischen_Wandgem=E4lden_vorbei=2C_g?=\n =?iso-8859-1?q?egen_die_rotierenden_Klingen_bef=F6rdert=2E_?=')

    def test_long_received_header(self):
        h = 'from FOO.TLD (vizworld.acl.foo.tld [123.452.678.9]) by hrothgar.la.mastaler.com (tmda-ofmipd) with ESMTP; Wed, 05 Mar 2003 18:10:18 -0700'
        msg = Message()
        msg['Received-1'] = Header(h, continuation_ws='\t')
        msg['Received-2'] = h
        self.ndiffAssertEqual(msg.as_string(), 'Received-1: from FOO.TLD (vizworld.acl.foo.tld [123.452.678.9]) by\n\throthgar.la.mastaler.com (tmda-ofmipd) with ESMTP;\n\tWed, 05 Mar 2003 18:10:18 -0700\nReceived-2: from FOO.TLD (vizworld.acl.foo.tld [123.452.678.9]) by\n hrothgar.la.mastaler.com (tmda-ofmipd) with ESMTP;\n Wed, 05 Mar 2003 18:10:18 -0700\n\n')

    def test_string_headerinst_eq(self):
        h = '<15975.17901.207240.414604@sgigritzmann1.mathematik.tu-muenchen.de> (David Bremner\'s message of "Thu, 6 Mar 2003 13:58:21 +0100")'
        msg = Message()
        msg['Received'] = Header(h, header_name='Received-1', continuation_ws='\t')
        msg['Received'] = h
        self.ndiffAssertEqual(msg.as_string(), 'Received: <15975.17901.207240.414604@sgigritzmann1.mathematik.tu-muenchen.de>\n\t(David Bremner\'s message of "Thu, 6 Mar 2003 13:58:21 +0100")\nReceived: <15975.17901.207240.414604@sgigritzmann1.mathematik.tu-muenchen.de>\n (David Bremner\'s message of "Thu, 6 Mar 2003 13:58:21 +0100")\n\n')

    def test_long_unbreakable_lines_with_continuation(self):
        eq = self.ndiffAssertEqual
        msg = Message()
        t = ' iVBORw0KGgoAAAANSUhEUgAAADAAAAAwBAMAAAClLOS0AAAAGFBMVEUAAAAkHiJeRUIcGBi9\n locQDQ4zJykFBAXJfWDjAAACYUlEQVR4nF2TQY/jIAyFc6lydlG5x8Nyp1Y69wj1PN2I5gzp'
        msg['Face-1'] = t
        msg['Face-2'] = Header(t, header_name='Face-2')
        eq(msg.as_string(), 'Face-1: iVBORw0KGgoAAAANSUhEUgAAADAAAAAwBAMAAAClLOS0AAAAGFBMVEUAAAAkHiJeRUIcGBi9\n locQDQ4zJykFBAXJfWDjAAACYUlEQVR4nF2TQY/jIAyFc6lydlG5x8Nyp1Y69wj1PN2I5gzp\nFace-2: iVBORw0KGgoAAAANSUhEUgAAADAAAAAwBAMAAAClLOS0AAAAGFBMVEUAAAAkHiJeRUIcGBi9\n locQDQ4zJykFBAXJfWDjAAACYUlEQVR4nF2TQY/jIAyFc6lydlG5x8Nyp1Y69wj1PN2I5gzp\n\n')

    def test_another_long_multiline_header(self):
        eq = self.ndiffAssertEqual
        m = 'Received: from siimage.com ([172.25.1.3]) by zima.siliconimage.com with Microsoft SMTPSVC(5.0.2195.4905);\n Wed, 16 Oct 2002 07:41:11 -0700'
        msg = email.message_from_string(m)
        eq(msg.as_string(), 'Received: from siimage.com ([172.25.1.3]) by zima.siliconimage.com with\n Microsoft SMTPSVC(5.0.2195.4905); Wed, 16 Oct 2002 07:41:11 -0700\n\n')

    def test_long_lines_with_different_header(self):
        eq = self.ndiffAssertEqual
        h = 'List-Unsubscribe: <https://lists.sourceforge.net/lists/listinfo/spamassassin-talk>,\n        <mailto:spamassassin-talk-request@lists.sourceforge.net?subject=unsubscribe>'
        msg = Message()
        msg['List'] = h
        msg['List'] = Header(h, header_name='List')
        self.ndiffAssertEqual(msg.as_string(), 'List: List-Unsubscribe: <https://lists.sourceforge.net/lists/listinfo/spamassassin-talk>,\n <mailto:spamassassin-talk-request@lists.sourceforge.net?subject=unsubscribe>\nList: List-Unsubscribe: <https://lists.sourceforge.net/lists/listinfo/spamassassin-talk>,\n <mailto:spamassassin-talk-request@lists.sourceforge.net?subject=unsubscribe>\n\n')


class TestFromMangling(unittest.TestCase):

    def setUp(self):
        self.msg = Message()
        self.msg['From'] = 'aaa@bbb.org'
        self.msg.set_payload('From the desk of A.A.A.:\nBlah blah blah\n')

    def test_mangled_from(self):
        s = StringIO()
        g = Generator(s, mangle_from_=True)
        g.flatten(self.msg)
        self.assertEqual(s.getvalue(), 'From: aaa@bbb.org\n\n>From the desk of A.A.A.:\nBlah blah blah\n')

    def test_dont_mangle_from(self):
        s = StringIO()
        g = Generator(s, mangle_from_=False)
        g.flatten(self.msg)
        self.assertEqual(s.getvalue(), 'From: aaa@bbb.org\n\nFrom the desk of A.A.A.:\nBlah blah blah\n')


class TestMIMEAudio(unittest.TestCase):

    def setUp(self):
        datadir = os.path.join(os.path.dirname(landmark), 'data', '')
        fp = open(findfile('audiotest.au', datadir), 'rb')
        try:
            self._audiodata = fp.read()
        finally:
            fp.close()

        self._au = MIMEAudio(self._audiodata)

    def test_guess_minor_type(self):
        self.assertEqual(self._au.get_content_type(), 'audio/basic')

    def test_encoding(self):
        payload = self._au.get_payload()
        self.assertEqual(base64.decodestring(payload), self._audiodata)

    def test_checkSetMinor(self):
        au = MIMEAudio(self._audiodata, 'fish')
        self.assertEqual(au.get_content_type(), 'audio/fish')

    def test_add_header(self):
        eq = self.assertEqual
        self._au.add_header('Content-Disposition', 'attachment', filename='audiotest.au')
        eq(self._au['content-disposition'], 'attachment; filename="audiotest.au"')
        eq(self._au.get_params(header='content-disposition'), [
         ('attachment', ''), ('filename', 'audiotest.au')])
        eq(self._au.get_param('filename', header='content-disposition'), 'audiotest.au')
        missing = []
        eq(self._au.get_param('attachment', header='content-disposition'), '')
        self.assertIs(self._au.get_param('foo', failobj=missing, header='content-disposition'), missing)
        self.assertIs(self._au.get_param('foobar', missing), missing)
        self.assertIs(self._au.get_param('attachment', missing, header='foobar'), missing)


class TestMIMEImage(unittest.TestCase):

    def setUp(self):
        fp = openfile('PyBanner048.gif')
        try:
            self._imgdata = fp.read()
        finally:
            fp.close()

        self._im = MIMEImage(self._imgdata)

    def test_guess_minor_type(self):
        self.assertEqual(self._im.get_content_type(), 'image/gif')

    def test_encoding(self):
        payload = self._im.get_payload()
        self.assertEqual(base64.decodestring(payload), self._imgdata)

    def test_checkSetMinor(self):
        im = MIMEImage(self._imgdata, 'fish')
        self.assertEqual(im.get_content_type(), 'image/fish')

    def test_add_header(self):
        eq = self.assertEqual
        self._im.add_header('Content-Disposition', 'attachment', filename='dingusfish.gif')
        eq(self._im['content-disposition'], 'attachment; filename="dingusfish.gif"')
        eq(self._im.get_params(header='content-disposition'), [
         ('attachment', ''), ('filename', 'dingusfish.gif')])
        eq(self._im.get_param('filename', header='content-disposition'), 'dingusfish.gif')
        missing = []
        eq(self._im.get_param('attachment', header='content-disposition'), '')
        self.assertIs(self._im.get_param('foo', failobj=missing, header='content-disposition'), missing)
        self.assertIs(self._im.get_param('foobar', missing), missing)
        self.assertIs(self._im.get_param('attachment', missing, header='foobar'), missing)


class TestMIMEApplication(unittest.TestCase):

    def test_headers(self):
        eq = self.assertEqual
        msg = MIMEApplication(b'\xfa\xfb\xfc\xfd\xfe\xff')
        eq(msg.get_content_type(), 'application/octet-stream')
        eq(msg['content-transfer-encoding'], 'base64')

    def test_body(self):
        eq = self.assertEqual
        bytes = b'\xfa\xfb\xfc\xfd\xfe\xff'
        msg = MIMEApplication(bytes)
        eq(msg.get_payload(), '+vv8/f7/')
        eq(msg.get_payload(decode=True), bytes)

    def test_binary_body_with_encode_7or8bit(self):
        bytesdata = b'\xfa\xfb\xfc\xfd\xfe\xff'
        msg = MIMEApplication(bytesdata, _encoder=encoders.encode_7or8bit)
        self.assertEqual(msg.get_payload(), bytesdata)
        self.assertEqual(msg.get_payload(decode=True), bytesdata)
        self.assertEqual(msg['Content-Transfer-Encoding'], '8bit')
        s = StringIO()
        g = Generator(s)
        g.flatten(msg)
        wireform = s.getvalue()
        msg2 = email.message_from_string(wireform)
        self.assertEqual(msg.get_payload(), bytesdata)
        self.assertEqual(msg2.get_payload(decode=True), bytesdata)
        self.assertEqual(msg2['Content-Transfer-Encoding'], '8bit')

    def test_binary_body_with_encode_noop(self):
        bytesdata = b'\xfa\xfb\xfc\xfd\xfe\xff'
        msg = MIMEApplication(bytesdata, _encoder=encoders.encode_noop)
        self.assertEqual(msg.get_payload(), bytesdata)
        self.assertEqual(msg.get_payload(decode=True), bytesdata)
        s = StringIO()
        g = Generator(s)
        g.flatten(msg)
        wireform = s.getvalue()
        msg2 = email.message_from_string(wireform)
        self.assertEqual(msg.get_payload(), bytesdata)
        self.assertEqual(msg2.get_payload(decode=True), bytesdata)


class TestMIMEText(unittest.TestCase):

    def setUp(self):
        self._msg = MIMEText('hello there')

    def test_types(self):
        eq = self.assertEqual
        eq(self._msg.get_content_type(), 'text/plain')
        eq(self._msg.get_param('charset'), 'us-ascii')
        missing = []
        self.assertIs(self._msg.get_param('foobar', missing), missing)
        self.assertIs(self._msg.get_param('charset', missing, header='foobar'), missing)

    def test_payload(self):
        self.assertEqual(self._msg.get_payload(), 'hello there')
        self.assertFalse(self._msg.is_multipart())

    def test_charset(self):
        eq = self.assertEqual
        msg = MIMEText('hello there', _charset='us-ascii')
        eq(msg.get_charset().input_charset, 'us-ascii')
        eq(msg['content-type'], 'text/plain; charset="us-ascii"')


class TestMultipart(TestEmailBase):

    def setUp(self):
        fp = openfile('PyBanner048.gif')
        try:
            data = fp.read()
        finally:
            fp.close()

        container = MIMEBase('multipart', 'mixed', boundary='BOUNDARY')
        image = MIMEImage(data, name='dingusfish.gif')
        image.add_header('content-disposition', 'attachment', filename='dingusfish.gif')
        intro = MIMEText('Hi there,\n\nThis is the dingus fish.\n')
        container.attach(intro)
        container.attach(image)
        container['From'] = 'Barry <barry@digicool.com>'
        container['To'] = 'Dingus Lovers <cravindogs@cravindogs.com>'
        container['Subject'] = 'Here is your dingus fish'
        now = 987809702.548486
        timetuple = time.localtime(now)
        if timetuple[(-1)] == 0:
            tzsecs = time.timezone
        else:
            tzsecs = time.altzone
        if tzsecs > 0:
            sign = '-'
        else:
            sign = '+'
        tzoffset = ' %s%04d' % (sign, tzsecs // 36)
        container['Date'] = time.strftime('%a, %d %b %Y %H:%M:%S', time.localtime(now)) + tzoffset
        self._msg = container
        self._im = image
        self._txt = intro

    def test_hierarchy(self):
        eq = self.assertEqual
        raises = self.assertRaises
        m = self._msg
        self.assertTrue(m.is_multipart())
        eq(m.get_content_type(), 'multipart/mixed')
        eq(len(m.get_payload()), 2)
        raises(IndexError, m.get_payload, 2)
        m0 = m.get_payload(0)
        m1 = m.get_payload(1)
        self.assertIs(m0, self._txt)
        self.assertIs(m1, self._im)
        eq(m.get_payload(), [m0, m1])
        self.assertFalse(m0.is_multipart())
        self.assertFalse(m1.is_multipart())

    def test_empty_multipart_idempotent(self):
        text = 'Content-Type: multipart/mixed; boundary="BOUNDARY"\nMIME-Version: 1.0\nSubject: A subject\nTo: aperson@dom.ain\nFrom: bperson@dom.ain\n\n\n--BOUNDARY\n\n\n--BOUNDARY--\n'
        msg = Parser().parsestr(text)
        self.ndiffAssertEqual(text, msg.as_string())

    def test_no_parts_in_a_multipart_with_none_epilogue(self):
        outer = MIMEBase('multipart', 'mixed')
        outer['Subject'] = 'A subject'
        outer['To'] = 'aperson@dom.ain'
        outer['From'] = 'bperson@dom.ain'
        outer.set_boundary('BOUNDARY')
        self.ndiffAssertEqual(outer.as_string(), 'Content-Type: multipart/mixed; boundary="BOUNDARY"\nMIME-Version: 1.0\nSubject: A subject\nTo: aperson@dom.ain\nFrom: bperson@dom.ain\n\n--BOUNDARY\n\n--BOUNDARY--\n')

    def test_no_parts_in_a_multipart_with_empty_epilogue(self):
        outer = MIMEBase('multipart', 'mixed')
        outer['Subject'] = 'A subject'
        outer['To'] = 'aperson@dom.ain'
        outer['From'] = 'bperson@dom.ain'
        outer.preamble = ''
        outer.epilogue = ''
        outer.set_boundary('BOUNDARY')
        self.ndiffAssertEqual(outer.as_string(), 'Content-Type: multipart/mixed; boundary="BOUNDARY"\nMIME-Version: 1.0\nSubject: A subject\nTo: aperson@dom.ain\nFrom: bperson@dom.ain\n\n\n--BOUNDARY\n\n--BOUNDARY--\n')

    def test_one_part_in_a_multipart(self):
        eq = self.ndiffAssertEqual
        outer = MIMEBase('multipart', 'mixed')
        outer['Subject'] = 'A subject'
        outer['To'] = 'aperson@dom.ain'
        outer['From'] = 'bperson@dom.ain'
        outer.set_boundary('BOUNDARY')
        msg = MIMEText('hello world')
        outer.attach(msg)
        eq(outer.as_string(), 'Content-Type: multipart/mixed; boundary="BOUNDARY"\nMIME-Version: 1.0\nSubject: A subject\nTo: aperson@dom.ain\nFrom: bperson@dom.ain\n\n--BOUNDARY\nContent-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\n\nhello world\n--BOUNDARY--\n')

    def test_seq_parts_in_a_multipart_with_empty_preamble(self):
        eq = self.ndiffAssertEqual
        outer = MIMEBase('multipart', 'mixed')
        outer['Subject'] = 'A subject'
        outer['To'] = 'aperson@dom.ain'
        outer['From'] = 'bperson@dom.ain'
        outer.preamble = ''
        msg = MIMEText('hello world')
        outer.attach(msg)
        outer.set_boundary('BOUNDARY')
        eq(outer.as_string(), 'Content-Type: multipart/mixed; boundary="BOUNDARY"\nMIME-Version: 1.0\nSubject: A subject\nTo: aperson@dom.ain\nFrom: bperson@dom.ain\n\n\n--BOUNDARY\nContent-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\n\nhello world\n--BOUNDARY--\n')

    def test_seq_parts_in_a_multipart_with_none_preamble(self):
        eq = self.ndiffAssertEqual
        outer = MIMEBase('multipart', 'mixed')
        outer['Subject'] = 'A subject'
        outer['To'] = 'aperson@dom.ain'
        outer['From'] = 'bperson@dom.ain'
        outer.preamble = None
        msg = MIMEText('hello world')
        outer.attach(msg)
        outer.set_boundary('BOUNDARY')
        eq(outer.as_string(), 'Content-Type: multipart/mixed; boundary="BOUNDARY"\nMIME-Version: 1.0\nSubject: A subject\nTo: aperson@dom.ain\nFrom: bperson@dom.ain\n\n--BOUNDARY\nContent-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\n\nhello world\n--BOUNDARY--\n')
        return

    def test_seq_parts_in_a_multipart_with_none_epilogue(self):
        eq = self.ndiffAssertEqual
        outer = MIMEBase('multipart', 'mixed')
        outer['Subject'] = 'A subject'
        outer['To'] = 'aperson@dom.ain'
        outer['From'] = 'bperson@dom.ain'
        outer.epilogue = None
        msg = MIMEText('hello world')
        outer.attach(msg)
        outer.set_boundary('BOUNDARY')
        eq(outer.as_string(), 'Content-Type: multipart/mixed; boundary="BOUNDARY"\nMIME-Version: 1.0\nSubject: A subject\nTo: aperson@dom.ain\nFrom: bperson@dom.ain\n\n--BOUNDARY\nContent-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\n\nhello world\n--BOUNDARY--\n')
        return

    def test_seq_parts_in_a_multipart_with_empty_epilogue(self):
        eq = self.ndiffAssertEqual
        outer = MIMEBase('multipart', 'mixed')
        outer['Subject'] = 'A subject'
        outer['To'] = 'aperson@dom.ain'
        outer['From'] = 'bperson@dom.ain'
        outer.epilogue = ''
        msg = MIMEText('hello world')
        outer.attach(msg)
        outer.set_boundary('BOUNDARY')
        eq(outer.as_string(), 'Content-Type: multipart/mixed; boundary="BOUNDARY"\nMIME-Version: 1.0\nSubject: A subject\nTo: aperson@dom.ain\nFrom: bperson@dom.ain\n\n--BOUNDARY\nContent-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\n\nhello world\n--BOUNDARY--\n')

    def test_seq_parts_in_a_multipart_with_nl_epilogue(self):
        eq = self.ndiffAssertEqual
        outer = MIMEBase('multipart', 'mixed')
        outer['Subject'] = 'A subject'
        outer['To'] = 'aperson@dom.ain'
        outer['From'] = 'bperson@dom.ain'
        outer.epilogue = '\n'
        msg = MIMEText('hello world')
        outer.attach(msg)
        outer.set_boundary('BOUNDARY')
        eq(outer.as_string(), 'Content-Type: multipart/mixed; boundary="BOUNDARY"\nMIME-Version: 1.0\nSubject: A subject\nTo: aperson@dom.ain\nFrom: bperson@dom.ain\n\n--BOUNDARY\nContent-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\n\nhello world\n--BOUNDARY--\n\n')

    def test_message_external_body(self):
        eq = self.assertEqual
        msg = self._msgobj('msg_36.txt')
        eq(len(msg.get_payload()), 2)
        msg1 = msg.get_payload(1)
        eq(msg1.get_content_type(), 'multipart/alternative')
        eq(len(msg1.get_payload()), 2)
        for subpart in msg1.get_payload():
            eq(subpart.get_content_type(), 'message/external-body')
            eq(len(subpart.get_payload()), 1)
            subsubpart = subpart.get_payload(0)
            eq(subsubpart.get_content_type(), 'text/plain')

    def test_double_boundary(self):
        msg = self._msgobj('msg_37.txt')
        self.assertEqual(len(msg.get_payload()), 3)

    def test_nested_inner_contains_outer_boundary(self):
        eq = self.ndiffAssertEqual
        msg = self._msgobj('msg_38.txt')
        sfp = StringIO()
        iterators._structure(msg, sfp)
        eq(sfp.getvalue(), 'multipart/mixed\n    multipart/mixed\n        multipart/alternative\n            text/plain\n        text/plain\n    text/plain\n    text/plain\n')

    def test_nested_with_same_boundary(self):
        eq = self.ndiffAssertEqual
        msg = self._msgobj('msg_39.txt')
        sfp = StringIO()
        iterators._structure(msg, sfp)
        eq(sfp.getvalue(), 'multipart/mixed\n    multipart/mixed\n        multipart/alternative\n        application/octet-stream\n        application/octet-stream\n    text/plain\n')

    def test_boundary_in_non_multipart(self):
        msg = self._msgobj('msg_40.txt')
        self.assertEqual(msg.as_string(), 'MIME-Version: 1.0\nContent-Type: text/html; boundary="--961284236552522269"\n\n----961284236552522269\nContent-Type: text/html;\nContent-Transfer-Encoding: 7Bit\n\n<html></html>\n\n----961284236552522269--\n')

    def test_boundary_with_leading_space(self):
        eq = self.assertEqual
        msg = email.message_from_string('MIME-Version: 1.0\nContent-Type: multipart/mixed; boundary="    XXXX"\n\n--    XXXX\nContent-Type: text/plain\n\n\n--    XXXX\nContent-Type: text/plain\n\n--    XXXX--\n')
        self.assertTrue(msg.is_multipart())
        eq(msg.get_boundary(), '    XXXX')
        eq(len(msg.get_payload()), 2)

    def test_boundary_without_trailing_newline(self):
        m = Parser().parsestr('Content-Type: multipart/mixed; boundary="===============0012394164=="\nMIME-Version: 1.0\n\n--===============0012394164==\nContent-Type: image/file1.jpg\nMIME-Version: 1.0\nContent-Transfer-Encoding: base64\n\nYXNkZg==\n--===============0012394164==--')
        self.assertEqual(m.get_payload(0).get_payload(), 'YXNkZg==')


class TestNonConformant(TestEmailBase):

    def test_parse_missing_minor_type(self):
        eq = self.assertEqual
        msg = self._msgobj('msg_14.txt')
        eq(msg.get_content_type(), 'text/plain')
        eq(msg.get_content_maintype(), 'text')
        eq(msg.get_content_subtype(), 'plain')

    def test_same_boundary_inner_outer(self):
        msg = self._msgobj('msg_15.txt')
        inner = msg.get_payload(0)
        self.assertTrue(hasattr(inner, 'defects'))
        self.assertEqual(len(inner.defects), 1)
        self.assertIsInstance(inner.defects[0], errors.StartBoundaryNotFoundDefect)

    def test_multipart_no_boundary(self):
        msg = self._msgobj('msg_25.txt')
        self.assertIsInstance(msg.get_payload(), str)
        self.assertEqual(len(msg.defects), 2)
        self.assertIsInstance(msg.defects[0], errors.NoBoundaryInMultipartDefect)
        self.assertIsInstance(msg.defects[1], errors.MultipartInvariantViolationDefect)

    def test_invalid_content_type(self):
        eq = self.assertEqual
        neq = self.ndiffAssertEqual
        msg = Message()
        msg['Content-Type'] = 'text'
        eq(msg.get_content_maintype(), 'text')
        eq(msg.get_content_subtype(), 'plain')
        eq(msg.get_content_type(), 'text/plain')
        del msg['content-type']
        msg['Content-Type'] = 'foo'
        eq(msg.get_content_maintype(), 'text')
        eq(msg.get_content_subtype(), 'plain')
        eq(msg.get_content_type(), 'text/plain')
        s = StringIO()
        g = Generator(s)
        g.flatten(msg)
        neq(s.getvalue(), 'Content-Type: foo\n\n')

    def test_no_start_boundary(self):
        eq = self.ndiffAssertEqual
        msg = self._msgobj('msg_31.txt')
        eq(msg.get_payload(), '--BOUNDARY\nContent-Type: text/plain\n\nmessage 1\n\n--BOUNDARY\nContent-Type: text/plain\n\nmessage 2\n\n--BOUNDARY--\n')

    def test_no_separating_blank_line(self):
        eq = self.ndiffAssertEqual
        msg = self._msgobj('msg_35.txt')
        eq(msg.as_string(), "From: aperson@dom.ain\nTo: bperson@dom.ain\nSubject: here's something interesting\n\ncounter to RFC 2822, there's no separating newline here\n")

    def test_lying_multipart(self):
        msg = self._msgobj('msg_41.txt')
        self.assertTrue(hasattr(msg, 'defects'))
        self.assertEqual(len(msg.defects), 2)
        self.assertIsInstance(msg.defects[0], errors.NoBoundaryInMultipartDefect)
        self.assertIsInstance(msg.defects[1], errors.MultipartInvariantViolationDefect)

    def test_missing_start_boundary(self):
        outer = self._msgobj('msg_42.txt')
        bad = outer.get_payload(1).get_payload(0)
        self.assertEqual(len(bad.defects), 1)
        self.assertIsInstance(bad.defects[0], errors.StartBoundaryNotFoundDefect)

    def test_first_line_is_continuation_header(self):
        eq = self.assertEqual
        m = ' Line 1\nLine 2\nLine 3'
        msg = email.message_from_string(m)
        eq(msg.keys(), [])
        eq(msg.get_payload(), 'Line 2\nLine 3')
        eq(len(msg.defects), 1)
        self.assertIsInstance(msg.defects[0], errors.FirstHeaderLineIsContinuationDefect)
        eq(msg.defects[0].line, ' Line 1\n')


class TestRFC2047(unittest.TestCase):

    def test_rfc2047_multiline(self):
        eq = self.assertEqual
        s = 'Re: =?mac-iceland?q?r=8Aksm=9Arg=8Cs?= baz\n foo bar =?mac-iceland?q?r=8Aksm=9Arg=8Cs?='
        dh = decode_header(s)
        eq(dh, [
         ('Re:', None),
         (b'r\x8aksm\x9arg\x8cs', 'mac-iceland'),
         ('baz foo bar', None),
         (b'r\x8aksm\x9arg\x8cs', 'mac-iceland')])
        eq(str(make_header(dh)), 'Re: =?mac-iceland?q?r=8Aksm=9Arg=8Cs?= baz foo bar\n =?mac-iceland?q?r=8Aksm=9Arg=8Cs?=')
        return

    def test_whitespace_eater_unicode(self):
        eq = self.assertEqual
        s = '=?ISO-8859-1?Q?Andr=E9?= Pirard <pirard@dom.ain>'
        dh = decode_header(s)
        eq(dh, [(b'Andr\xe9', 'iso-8859-1'), ('Pirard <pirard@dom.ain>', None)])
        hu = unicode(make_header(dh)).encode('latin-1')
        eq(hu, b'Andr\xe9 Pirard <pirard@dom.ain>')
        return

    def test_whitespace_eater_unicode_2(self):
        eq = self.assertEqual
        s = 'The =?iso-8859-1?b?cXVpY2sgYnJvd24gZm94?= jumped over the =?iso-8859-1?b?bGF6eSBkb2c=?='
        dh = decode_header(s)
        eq(dh, [('The', None), ('quick brown fox', 'iso-8859-1'),
         ('jumped over the', None), ('lazy dog', 'iso-8859-1')])
        hu = make_header(dh).__unicode__()
        eq(hu, 'The quick brown fox jumped over the lazy dog')
        return

    def test_rfc2047_missing_whitespace(self):
        s = 'Sm=?ISO-8859-1?B?9g==?=rg=?ISO-8859-1?B?5Q==?=sbord'
        dh = decode_header(s)
        self.assertEqual(dh, [(s, None)])
        return

    def test_rfc2047_with_whitespace(self):
        s = 'Sm =?ISO-8859-1?B?9g==?= rg =?ISO-8859-1?B?5Q==?= sbord'
        dh = decode_header(s)
        self.assertEqual(dh, [('Sm', None), (b'\xf6', 'iso-8859-1'),
         ('rg', None), (b'\xe5', 'iso-8859-1'),
         ('sbord', None)])
        return


class TestMIMEMessage(TestEmailBase):

    def setUp(self):
        fp = openfile('msg_11.txt')
        try:
            self._text = fp.read()
        finally:
            fp.close()

    def test_type_error(self):
        self.assertRaises(TypeError, MIMEMessage, 'a plain string')

    def test_valid_argument(self):
        eq = self.assertEqual
        subject = 'A sub-message'
        m = Message()
        m['Subject'] = subject
        r = MIMEMessage(m)
        eq(r.get_content_type(), 'message/rfc822')
        payload = r.get_payload()
        self.assertIsInstance(payload, list)
        eq(len(payload), 1)
        subpart = payload[0]
        self.assertIs(subpart, m)
        eq(subpart['subject'], subject)

    def test_bad_multipart(self):
        eq = self.assertEqual
        msg1 = Message()
        msg1['Subject'] = 'subpart 1'
        msg2 = Message()
        msg2['Subject'] = 'subpart 2'
        r = MIMEMessage(msg1)
        self.assertRaises(errors.MultipartConversionError, r.attach, msg2)

    def test_generate(self):
        m = Message()
        m['Subject'] = 'An enclosed message'
        m.set_payload('Here is the body of the message.\n')
        r = MIMEMessage(m)
        r['Subject'] = 'The enclosing message'
        s = StringIO()
        g = Generator(s)
        g.flatten(r)
        self.assertEqual(s.getvalue(), 'Content-Type: message/rfc822\nMIME-Version: 1.0\nSubject: The enclosing message\n\nSubject: An enclosed message\n\nHere is the body of the message.\n')

    def test_parse_message_rfc822(self):
        eq = self.assertEqual
        msg = self._msgobj('msg_11.txt')
        eq(msg.get_content_type(), 'message/rfc822')
        payload = msg.get_payload()
        self.assertIsInstance(payload, list)
        eq(len(payload), 1)
        submsg = payload[0]
        self.assertIsInstance(submsg, Message)
        eq(submsg['subject'], 'An enclosed message')
        eq(submsg.get_payload(), 'Here is the body of the message.\n')

    def test_dsn(self):
        eq = self.assertEqual
        msg = self._msgobj('msg_16.txt')
        eq(msg.get_content_type(), 'multipart/report')
        self.assertTrue(msg.is_multipart())
        eq(len(msg.get_payload()), 3)
        subpart = msg.get_payload(0)
        eq(subpart.get_content_type(), 'text/plain')
        eq(subpart.get_payload(), 'This report relates to a message you sent with the following header fields:\n\n  Message-id: <002001c144a6$8752e060$56104586@oxy.edu>\n  Date: Sun, 23 Sep 2001 20:10:55 -0700\n  From: "Ian T. Henry" <henryi@oxy.edu>\n  To: SoCal Raves <scr@socal-raves.org>\n  Subject: [scr] yeah for Ians!!\n\nYour message cannot be delivered to the following recipients:\n\n  Recipient address: jangel1@cougar.noc.ucla.edu\n  Reason: recipient reached disk quota\n\n')
        subpart = msg.get_payload(1)
        eq(subpart.get_content_type(), 'message/delivery-status')
        eq(len(subpart.get_payload()), 2)
        dsn1 = subpart.get_payload(0)
        self.assertIsInstance(dsn1, Message)
        eq(dsn1['original-envelope-id'], '0GK500B4HD0888@cougar.noc.ucla.edu')
        eq(dsn1.get_param('dns', header='reporting-mta'), '')
        eq(dsn1.get_param('nsd', header='reporting-mta'), None)
        dsn2 = subpart.get_payload(1)
        self.assertIsInstance(dsn2, Message)
        eq(dsn2['action'], 'failed')
        eq(dsn2.get_params(header='original-recipient'), [
         ('rfc822', ''), ('jangel1@cougar.noc.ucla.edu', '')])
        eq(dsn2.get_param('rfc822', header='final-recipient'), '')
        subpart = msg.get_payload(2)
        eq(subpart.get_content_type(), 'message/rfc822')
        payload = subpart.get_payload()
        self.assertIsInstance(payload, list)
        eq(len(payload), 1)
        subsubpart = payload[0]
        self.assertIsInstance(subsubpart, Message)
        eq(subsubpart.get_content_type(), 'text/plain')
        eq(subsubpart['message-id'], '<002001c144a6$8752e060$56104586@oxy.edu>')
        return

    def test_epilogue(self):
        eq = self.ndiffAssertEqual
        fp = openfile('msg_21.txt')
        try:
            text = fp.read()
        finally:
            fp.close()

        msg = Message()
        msg['From'] = 'aperson@dom.ain'
        msg['To'] = 'bperson@dom.ain'
        msg['Subject'] = 'Test'
        msg.preamble = 'MIME message'
        msg.epilogue = 'End of MIME message\n'
        msg1 = MIMEText('One')
        msg2 = MIMEText('Two')
        msg.add_header('Content-Type', 'multipart/mixed', boundary='BOUNDARY')
        msg.attach(msg1)
        msg.attach(msg2)
        sfp = StringIO()
        g = Generator(sfp)
        g.flatten(msg)
        eq(sfp.getvalue(), text)

    def test_no_nl_preamble(self):
        eq = self.ndiffAssertEqual
        msg = Message()
        msg['From'] = 'aperson@dom.ain'
        msg['To'] = 'bperson@dom.ain'
        msg['Subject'] = 'Test'
        msg.preamble = 'MIME message'
        msg.epilogue = ''
        msg1 = MIMEText('One')
        msg2 = MIMEText('Two')
        msg.add_header('Content-Type', 'multipart/mixed', boundary='BOUNDARY')
        msg.attach(msg1)
        msg.attach(msg2)
        eq(msg.as_string(), 'From: aperson@dom.ain\nTo: bperson@dom.ain\nSubject: Test\nContent-Type: multipart/mixed; boundary="BOUNDARY"\n\nMIME message\n--BOUNDARY\nContent-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\n\nOne\n--BOUNDARY\nContent-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\n\nTwo\n--BOUNDARY--\n')

    def test_default_type(self):
        eq = self.assertEqual
        fp = openfile('msg_30.txt')
        try:
            msg = email.message_from_file(fp)
        finally:
            fp.close()

        container1 = msg.get_payload(0)
        eq(container1.get_default_type(), 'message/rfc822')
        eq(container1.get_content_type(), 'message/rfc822')
        container2 = msg.get_payload(1)
        eq(container2.get_default_type(), 'message/rfc822')
        eq(container2.get_content_type(), 'message/rfc822')
        container1a = container1.get_payload(0)
        eq(container1a.get_default_type(), 'text/plain')
        eq(container1a.get_content_type(), 'text/plain')
        container2a = container2.get_payload(0)
        eq(container2a.get_default_type(), 'text/plain')
        eq(container2a.get_content_type(), 'text/plain')

    def test_default_type_with_explicit_container_type(self):
        eq = self.assertEqual
        fp = openfile('msg_28.txt')
        try:
            msg = email.message_from_file(fp)
        finally:
            fp.close()

        container1 = msg.get_payload(0)
        eq(container1.get_default_type(), 'message/rfc822')
        eq(container1.get_content_type(), 'message/rfc822')
        container2 = msg.get_payload(1)
        eq(container2.get_default_type(), 'message/rfc822')
        eq(container2.get_content_type(), 'message/rfc822')
        container1a = container1.get_payload(0)
        eq(container1a.get_default_type(), 'text/plain')
        eq(container1a.get_content_type(), 'text/plain')
        container2a = container2.get_payload(0)
        eq(container2a.get_default_type(), 'text/plain')
        eq(container2a.get_content_type(), 'text/plain')

    def test_default_type_non_parsed(self):
        eq = self.assertEqual
        neq = self.ndiffAssertEqual
        container = MIMEMultipart('digest', 'BOUNDARY')
        container.epilogue = ''
        subpart1a = MIMEText('message 1\n')
        subpart2a = MIMEText('message 2\n')
        subpart1 = MIMEMessage(subpart1a)
        subpart2 = MIMEMessage(subpart2a)
        container.attach(subpart1)
        container.attach(subpart2)
        eq(subpart1.get_content_type(), 'message/rfc822')
        eq(subpart1.get_default_type(), 'message/rfc822')
        eq(subpart2.get_content_type(), 'message/rfc822')
        eq(subpart2.get_default_type(), 'message/rfc822')
        neq(container.as_string(0), 'Content-Type: multipart/digest; boundary="BOUNDARY"\nMIME-Version: 1.0\n\n--BOUNDARY\nContent-Type: message/rfc822\nMIME-Version: 1.0\n\nContent-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\n\nmessage 1\n\n--BOUNDARY\nContent-Type: message/rfc822\nMIME-Version: 1.0\n\nContent-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\n\nmessage 2\n\n--BOUNDARY--\n')
        del subpart1['content-type']
        del subpart1['mime-version']
        del subpart2['content-type']
        del subpart2['mime-version']
        eq(subpart1.get_content_type(), 'message/rfc822')
        eq(subpart1.get_default_type(), 'message/rfc822')
        eq(subpart2.get_content_type(), 'message/rfc822')
        eq(subpart2.get_default_type(), 'message/rfc822')
        neq(container.as_string(0), 'Content-Type: multipart/digest; boundary="BOUNDARY"\nMIME-Version: 1.0\n\n--BOUNDARY\n\nContent-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\n\nmessage 1\n\n--BOUNDARY\n\nContent-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\n\nmessage 2\n\n--BOUNDARY--\n')

    def test_mime_attachments_in_constructor(self):
        eq = self.assertEqual
        text1 = MIMEText('')
        text2 = MIMEText('')
        msg = MIMEMultipart(_subparts=(text1, text2))
        eq(len(msg.get_payload()), 2)
        eq(msg.get_payload(0), text1)
        eq(msg.get_payload(1), text2)


class TestIdempotent(TestEmailBase):

    def _msgobj(self, filename):
        fp = openfile(filename)
        try:
            data = fp.read()
        finally:
            fp.close()

        msg = email.message_from_string(data)
        return (msg, data)

    def _idempotent(self, msg, text):
        eq = self.ndiffAssertEqual
        s = StringIO()
        g = Generator(s, maxheaderlen=0)
        g.flatten(msg)
        eq(text, s.getvalue())

    def test_parse_text_message(self):
        eq = self.assertEqual
        msg, text = self._msgobj('msg_01.txt')
        eq(msg.get_content_type(), 'text/plain')
        eq(msg.get_content_maintype(), 'text')
        eq(msg.get_content_subtype(), 'plain')
        eq(msg.get_params()[1], ('charset', 'us-ascii'))
        eq(msg.get_param('charset'), 'us-ascii')
        eq(msg.preamble, None)
        eq(msg.epilogue, None)
        self._idempotent(msg, text)
        return

    def test_parse_untyped_message(self):
        eq = self.assertEqual
        msg, text = self._msgobj('msg_03.txt')
        eq(msg.get_content_type(), 'text/plain')
        eq(msg.get_params(), None)
        eq(msg.get_param('charset'), None)
        self._idempotent(msg, text)
        return

    def test_simple_multipart(self):
        msg, text = self._msgobj('msg_04.txt')
        self._idempotent(msg, text)

    def test_MIME_digest(self):
        msg, text = self._msgobj('msg_02.txt')
        self._idempotent(msg, text)

    def test_long_header(self):
        msg, text = self._msgobj('msg_27.txt')
        self._idempotent(msg, text)

    def test_MIME_digest_with_part_headers(self):
        msg, text = self._msgobj('msg_28.txt')
        self._idempotent(msg, text)

    def test_mixed_with_image(self):
        msg, text = self._msgobj('msg_06.txt')
        self._idempotent(msg, text)

    def test_multipart_report(self):
        msg, text = self._msgobj('msg_05.txt')
        self._idempotent(msg, text)

    def test_dsn(self):
        msg, text = self._msgobj('msg_16.txt')
        self._idempotent(msg, text)

    def test_preamble_epilogue(self):
        msg, text = self._msgobj('msg_21.txt')
        self._idempotent(msg, text)

    def test_multipart_one_part(self):
        msg, text = self._msgobj('msg_23.txt')
        self._idempotent(msg, text)

    def test_multipart_no_parts(self):
        msg, text = self._msgobj('msg_24.txt')
        self._idempotent(msg, text)

    def test_no_start_boundary(self):
        msg, text = self._msgobj('msg_31.txt')
        self._idempotent(msg, text)

    def test_rfc2231_charset(self):
        msg, text = self._msgobj('msg_32.txt')
        self._idempotent(msg, text)

    def test_more_rfc2231_parameters(self):
        msg, text = self._msgobj('msg_33.txt')
        self._idempotent(msg, text)

    def test_text_plain_in_a_multipart_digest(self):
        msg, text = self._msgobj('msg_34.txt')
        self._idempotent(msg, text)

    def test_nested_multipart_mixeds(self):
        msg, text = self._msgobj('msg_12a.txt')
        self._idempotent(msg, text)

    def test_message_external_body_idempotent(self):
        msg, text = self._msgobj('msg_36.txt')
        self._idempotent(msg, text)

    def test_content_type(self):
        eq = self.assertEqual
        msg, text = self._msgobj('msg_05.txt')
        eq(msg.get_content_type(), 'multipart/report')
        params = {}
        for pk, pv in msg.get_params():
            params[pk] = pv

        eq(params['report-type'], 'delivery-status')
        eq(params['boundary'], 'D1690A7AC1.996856090/mail.example.com')
        eq(msg.preamble, 'This is a MIME-encapsulated message.\n')
        eq(msg.epilogue, '\n')
        eq(len(msg.get_payload()), 3)
        msg1 = msg.get_payload(0)
        eq(msg1.get_content_type(), 'text/plain')
        eq(msg1.get_payload(), 'Yadda yadda yadda\n')
        msg2 = msg.get_payload(1)
        eq(msg2.get_content_type(), 'text/plain')
        eq(msg2.get_payload(), 'Yadda yadda yadda\n')
        msg3 = msg.get_payload(2)
        eq(msg3.get_content_type(), 'message/rfc822')
        self.assertIsInstance(msg3, Message)
        payload = msg3.get_payload()
        self.assertIsInstance(payload, list)
        eq(len(payload), 1)
        msg4 = payload[0]
        self.assertIsInstance(msg4, Message)
        eq(msg4.get_payload(), 'Yadda yadda yadda\n')

    def test_parser(self):
        eq = self.assertEqual
        msg, text = self._msgobj('msg_06.txt')
        eq(msg.get_content_type(), 'message/rfc822')
        payload = msg.get_payload()
        self.assertIsInstance(payload, list)
        eq(len(payload), 1)
        msg1 = payload[0]
        self.assertIsInstance(msg1, Message)
        eq(msg1.get_content_type(), 'text/plain')
        self.assertIsInstance(msg1.get_payload(), str)
        eq(msg1.get_payload(), '\n')


class TestMiscellaneous(TestEmailBase):

    def test_message_from_string(self):
        fp = openfile('msg_01.txt')
        try:
            text = fp.read()
        finally:
            fp.close()

        msg = email.message_from_string(text)
        s = StringIO()
        g = Generator(s, maxheaderlen=0)
        g.flatten(msg)
        self.assertEqual(text, s.getvalue())

    def test_message_from_file(self):
        fp = openfile('msg_01.txt')
        try:
            text = fp.read()
            fp.seek(0)
            msg = email.message_from_file(fp)
            s = StringIO()
            g = Generator(s, maxheaderlen=0)
            g.flatten(msg)
            self.assertEqual(text, s.getvalue())
        finally:
            fp.close()

    def test_message_from_string_with_class(self):
        fp = openfile('msg_01.txt')
        try:
            text = fp.read()
        finally:
            fp.close()

        class MyMessage(Message):
            pass

        msg = email.message_from_string(text, MyMessage)
        self.assertIsInstance(msg, MyMessage)
        fp = openfile('msg_02.txt')
        try:
            text = fp.read()
        finally:
            fp.close()

        msg = email.message_from_string(text, MyMessage)
        for subpart in msg.walk():
            self.assertIsInstance(subpart, MyMessage)

    def test_message_from_file_with_class(self):

        class MyMessage(Message):
            pass

        fp = openfile('msg_01.txt')
        try:
            msg = email.message_from_file(fp, MyMessage)
        finally:
            fp.close()

        self.assertIsInstance(msg, MyMessage)
        fp = openfile('msg_02.txt')
        try:
            msg = email.message_from_file(fp, MyMessage)
        finally:
            fp.close()

        for subpart in msg.walk():
            self.assertIsInstance(subpart, MyMessage)

    def test__all__(self):
        module = __import__('email')
        all = module.__all__[:]
        all.sort()
        self.assertEqual(all, [
         'Charset', 'Encoders', 'Errors', 'Generator',
         'Header', 'Iterators', 'MIMEAudio', 'MIMEBase',
         'MIMEImage', 'MIMEMessage', 'MIMEMultipart',
         'MIMENonMultipart', 'MIMEText', 'Message',
         'Parser', 'Utils', 'base64MIME',
         'base64mime', 'charset', 'encoders', 'errors', 'generator',
         'header', 'iterators', 'message', 'message_from_file',
         'message_from_string', 'mime', 'parser',
         'quopriMIME', 'quoprimime', 'utils'])

    def test_formatdate(self):
        now = time.time()
        self.assertEqual(utils.parsedate(utils.formatdate(now))[:6], time.gmtime(now)[:6])

    def test_formatdate_localtime(self):
        now = time.time()
        self.assertEqual(utils.parsedate(utils.formatdate(now, localtime=True))[:6], time.localtime(now)[:6])

    def test_formatdate_usegmt(self):
        now = time.time()
        self.assertEqual(utils.formatdate(now, localtime=False), time.strftime('%a, %d %b %Y %H:%M:%S -0000', time.gmtime(now)))
        self.assertEqual(utils.formatdate(now, localtime=False, usegmt=True), time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(now)))

    def test_parsedate_none(self):
        self.assertEqual(utils.parsedate(''), None)
        return

    def test_parsedate_compact(self):
        self.assertEqual(utils.parsedate('Wed,3 Apr 2002 14:58:26 +0800'), utils.parsedate('Wed, 3 Apr 2002 14:58:26 +0800'))

    def test_parsedate_no_dayofweek(self):
        eq = self.assertEqual
        eq(utils.parsedate_tz('25 Feb 2003 13:47:26 -0800'), (2003, 2, 25, 13, 47,
                                                              26, 0, 1, -1, -28800))

    def test_parsedate_compact_no_dayofweek(self):
        eq = self.assertEqual
        eq(utils.parsedate_tz('5 Feb 2003 13:47:26 -0800'), (2003, 2, 5, 13, 47, 26,
                                                             0, 1, -1, -28800))

    def test_parsedate_acceptable_to_time_functions(self):
        eq = self.assertEqual
        timetup = utils.parsedate('5 Feb 2003 13:47:26 -0800')
        t = int(time.mktime(timetup))
        eq(time.localtime(t)[:6], timetup[:6])
        eq(int(time.strftime('%Y', timetup)), 2003)
        timetup = utils.parsedate_tz('5 Feb 2003 13:47:26 -0800')
        t = int(time.mktime(timetup[:9]))
        eq(time.localtime(t)[:6], timetup[:6])
        eq(int(time.strftime('%Y', timetup[:9])), 2003)

    def test_parseaddr_empty(self):
        self.assertEqual(utils.parseaddr('<>'), ('', ''))
        self.assertEqual(utils.formataddr(utils.parseaddr('<>')), '')

    def test_noquote_dump(self):
        self.assertEqual(utils.formataddr(('A Silly Person', 'person@dom.ain')), 'A Silly Person <person@dom.ain>')

    def test_escape_dump(self):
        self.assertEqual(utils.formataddr(('A (Very) Silly Person', 'person@dom.ain')), '"A \\(Very\\) Silly Person" <person@dom.ain>')
        a = 'A \\(Special\\) Person'
        b = 'person@dom.ain'
        self.assertEqual(utils.parseaddr(utils.formataddr((a, b))), (a, b))

    def test_escape_backslashes(self):
        self.assertEqual(utils.formataddr(('Arthur \\Backslash\\ Foobar', 'person@dom.ain')), '"Arthur \\\\Backslash\\\\ Foobar" <person@dom.ain>')
        a = 'Arthur \\Backslash\\ Foobar'
        b = 'person@dom.ain'
        self.assertEqual(utils.parseaddr(utils.formataddr((a, b))), (a, b))

    def test_name_with_dot(self):
        x = 'John X. Doe <jxd@example.com>'
        y = '"John X. Doe" <jxd@example.com>'
        a, b = ('John X. Doe', 'jxd@example.com')
        self.assertEqual(utils.parseaddr(x), (a, b))
        self.assertEqual(utils.parseaddr(y), (a, b))
        self.assertEqual(utils.formataddr((a, b)), y)

    def test_multiline_from_comment(self):
        x = 'Foo\n\tBar <foo@example.com>'
        self.assertEqual(utils.parseaddr(x), ('Foo Bar', 'foo@example.com'))

    def test_quote_dump(self):
        self.assertEqual(utils.formataddr(('A Silly; Person', 'person@dom.ain')), '"A Silly; Person" <person@dom.ain>')

    def test_fix_eols(self):
        eq = self.assertEqual
        eq(utils.fix_eols('hello'), 'hello')
        eq(utils.fix_eols('hello\n'), 'hello\r\n')
        eq(utils.fix_eols('hello\r'), 'hello\r\n')
        eq(utils.fix_eols('hello\r\n'), 'hello\r\n')
        eq(utils.fix_eols('hello\n\r'), 'hello\r\n\r\n')

    def test_charset_richcomparisons(self):
        eq = self.assertEqual
        ne = self.assertNotEqual
        cset1 = Charset()
        cset2 = Charset()
        eq(cset1, 'us-ascii')
        eq(cset1, 'US-ASCII')
        eq(cset1, 'Us-AsCiI')
        eq('us-ascii', cset1)
        eq('US-ASCII', cset1)
        eq('Us-AsCiI', cset1)
        ne(cset1, 'usascii')
        ne(cset1, 'USASCII')
        ne(cset1, 'UsAsCiI')
        ne('usascii', cset1)
        ne('USASCII', cset1)
        ne('UsAsCiI', cset1)
        eq(cset1, cset2)
        eq(cset2, cset1)

    def test_getaddresses(self):
        eq = self.assertEqual
        eq(utils.getaddresses(['aperson@dom.ain (Al Person)',
         'Bud Person <bperson@dom.ain>']), [
         ('Al Person', 'aperson@dom.ain'),
         ('Bud Person', 'bperson@dom.ain')])

    def test_getaddresses_nasty(self):
        eq = self.assertEqual
        eq(utils.getaddresses(['foo: ;']), [('', '')])
        eq(utils.getaddresses([
         '[]*-- =~$']), [
         ('', ''), ('', ''), ('', '*--')])
        eq(utils.getaddresses([
         'foo: ;', '"Jason R. Mastaler" <jason@dom.ain>']), [
         ('', ''), ('Jason R. Mastaler', 'jason@dom.ain')])

    def test_getaddresses_embedded_comment(self):
        eq = self.assertEqual
        addrs = utils.getaddresses(['User ((nested comment)) <foo@bar.com>'])
        eq(addrs[0][1], 'foo@bar.com')

    def test_utils_quote_unquote(self):
        eq = self.assertEqual
        msg = Message()
        msg.add_header('content-disposition', 'attachment', filename='foo\\wacky"name')
        eq(msg.get_filename(), 'foo\\wacky"name')

    def test_get_body_encoding_with_bogus_charset(self):
        charset = Charset('not a charset')
        self.assertEqual(charset.get_body_encoding(), 'base64')

    def test_get_body_encoding_with_uppercase_charset(self):
        eq = self.assertEqual
        msg = Message()
        msg['Content-Type'] = 'text/plain; charset=UTF-8'
        eq(msg['content-type'], 'text/plain; charset=UTF-8')
        charsets = msg.get_charsets()
        eq(len(charsets), 1)
        eq(charsets[0], 'utf-8')
        charset = Charset(charsets[0])
        eq(charset.get_body_encoding(), 'base64')
        msg.set_payload('hello world', charset=charset)
        eq(msg.get_payload(), 'aGVsbG8gd29ybGQ=\n')
        eq(msg.get_payload(decode=True), 'hello world')
        eq(msg['content-transfer-encoding'], 'base64')
        msg = Message()
        msg['Content-Type'] = 'text/plain; charset="US-ASCII"'
        charsets = msg.get_charsets()
        eq(len(charsets), 1)
        eq(charsets[0], 'us-ascii')
        charset = Charset(charsets[0])
        eq(charset.get_body_encoding(), encoders.encode_7or8bit)
        msg.set_payload('hello world', charset=charset)
        eq(msg.get_payload(), 'hello world')
        eq(msg['content-transfer-encoding'], '7bit')

    def test_charsets_case_insensitive(self):
        lc = Charset('us-ascii')
        uc = Charset('US-ASCII')
        self.assertEqual(lc.get_body_encoding(), uc.get_body_encoding())

    def test_partial_falls_inside_message_delivery_status(self):
        eq = self.ndiffAssertEqual
        msg = self._msgobj('msg_43.txt')
        sfp = StringIO()
        iterators._structure(msg, sfp)
        eq(sfp.getvalue(), 'multipart/report\n    text/plain\n    message/delivery-status\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n        text/plain\n    text/rfc822-headers\n')


class TestIterators(TestEmailBase):

    def test_body_line_iterator(self):
        eq = self.assertEqual
        neq = self.ndiffAssertEqual
        msg = self._msgobj('msg_01.txt')
        it = iterators.body_line_iterator(msg)
        lines = list(it)
        eq(len(lines), 6)
        neq(EMPTYSTRING.join(lines), msg.get_payload())
        msg = self._msgobj('msg_02.txt')
        it = iterators.body_line_iterator(msg)
        lines = list(it)
        eq(len(lines), 43)
        fp = openfile('msg_19.txt')
        try:
            neq(EMPTYSTRING.join(lines), fp.read())
        finally:
            fp.close()

    def test_typed_subpart_iterator(self):
        eq = self.assertEqual
        msg = self._msgobj('msg_04.txt')
        it = iterators.typed_subpart_iterator(msg, 'text')
        lines = []
        subparts = 0
        for subpart in it:
            subparts += 1
            lines.append(subpart.get_payload())

        eq(subparts, 2)
        eq(EMPTYSTRING.join(lines), 'a simple kind of mirror\nto reflect upon our own\na simple kind of mirror\nto reflect upon our own\n')

    def test_typed_subpart_iterator_default_type(self):
        eq = self.assertEqual
        msg = self._msgobj('msg_03.txt')
        it = iterators.typed_subpart_iterator(msg, 'text', 'plain')
        lines = []
        subparts = 0
        for subpart in it:
            subparts += 1
            lines.append(subpart.get_payload())

        eq(subparts, 1)
        eq(EMPTYSTRING.join(lines), '\nHi,\n\nDo you like this message?\n\n-Me\n')


class TestParsers(TestEmailBase):

    def test_header_parser(self):
        eq = self.assertEqual
        fp = openfile('msg_02.txt')
        try:
            msg = HeaderParser().parse(fp)
        finally:
            fp.close()

        eq(msg['from'], 'ppp-request@zzz.org')
        eq(msg['to'], 'ppp@zzz.org')
        eq(msg.get_content_type(), 'multipart/mixed')
        self.assertFalse(msg.is_multipart())
        self.assertIsInstance(msg.get_payload(), str)

    def test_whitespace_continuation(self):
        eq = self.assertEqual
        msg = email.message_from_string("From: aperson@dom.ain\nTo: bperson@dom.ain\nSubject: the next line has a space on it\n \nDate: Mon, 8 Apr 2002 15:09:19 -0400\nMessage-ID: spam\n\nHere's the message body\n")
        eq(msg['subject'], 'the next line has a space on it\n ')
        eq(msg['message-id'], 'spam')
        eq(msg.get_payload(), "Here's the message body\n")

    def test_whitespace_continuation_last_header(self):
        eq = self.assertEqual
        msg = email.message_from_string("From: aperson@dom.ain\nTo: bperson@dom.ain\nDate: Mon, 8 Apr 2002 15:09:19 -0400\nMessage-ID: spam\nSubject: the next line has a space on it\n \n\nHere's the message body\n")
        eq(msg['subject'], 'the next line has a space on it\n ')
        eq(msg['message-id'], 'spam')
        eq(msg.get_payload(), "Here's the message body\n")

    def test_crlf_separation(self):
        eq = self.assertEqual
        fp = openfile('msg_26.txt', mode='rb')
        try:
            msg = Parser().parse(fp)
        finally:
            fp.close()

        eq(len(msg.get_payload()), 2)
        part1 = msg.get_payload(0)
        eq(part1.get_content_type(), 'text/plain')
        eq(part1.get_payload(), 'Simple email with attachment.\r\n\r\n')
        part2 = msg.get_payload(1)
        eq(part2.get_content_type(), 'application/riscos')

    def test_multipart_digest_with_extra_mime_headers(self):
        eq = self.assertEqual
        neq = self.ndiffAssertEqual
        fp = openfile('msg_28.txt')
        try:
            msg = email.message_from_file(fp)
        finally:
            fp.close()

        eq(msg.is_multipart(), 1)
        eq(len(msg.get_payload()), 2)
        part1 = msg.get_payload(0)
        eq(part1.get_content_type(), 'message/rfc822')
        eq(part1.is_multipart(), 1)
        eq(len(part1.get_payload()), 1)
        part1a = part1.get_payload(0)
        eq(part1a.is_multipart(), 0)
        eq(part1a.get_content_type(), 'text/plain')
        neq(part1a.get_payload(), 'message 1\n')
        part2 = msg.get_payload(1)
        eq(part2.get_content_type(), 'message/rfc822')
        eq(part2.is_multipart(), 1)
        eq(len(part2.get_payload()), 1)
        part2a = part2.get_payload(0)
        eq(part2a.is_multipart(), 0)
        eq(part2a.get_content_type(), 'text/plain')
        neq(part2a.get_payload(), 'message 2\n')

    def test_three_lines(self):
        lines = [
         'From: Andrew Person <aperson@dom.ain',
         'Subject: Test',
         'Date: Tue, 20 Aug 2002 16:43:45 +1000']
        msg = email.message_from_string(NL.join(lines))
        self.assertEqual(msg['date'], 'Tue, 20 Aug 2002 16:43:45 +1000')

    def test_strip_line_feed_and_carriage_return_in_headers(self):
        eq = self.assertEqual
        value1 = 'text'
        value2 = 'more text'
        m = 'Header: %s\r\nNext-Header: %s\r\n\r\nBody\r\n\r\n' % (
         value1, value2)
        msg = email.message_from_string(m)
        eq(msg.get('Header'), value1)
        eq(msg.get('Next-Header'), value2)

    def test_rfc2822_header_syntax(self):
        eq = self.assertEqual
        m = '>From: foo\nFrom: bar\n!"#QUX;~: zoo\n\nbody'
        msg = email.message_from_string(m)
        eq(len(msg.keys()), 3)
        keys = msg.keys()
        keys.sort()
        eq(keys, ['!"#QUX;~', '>From', 'From'])
        eq(msg.get_payload(), 'body')

    def test_rfc2822_space_not_allowed_in_header(self):
        eq = self.assertEqual
        m = '>From foo@example.com 11:25:53\nFrom: bar\n!"#QUX;~: zoo\n\nbody'
        msg = email.message_from_string(m)
        eq(len(msg.keys()), 0)

    def test_rfc2822_one_character_header(self):
        eq = self.assertEqual
        m = 'A: first header\nB: second header\nCC: third header\n\nbody'
        msg = email.message_from_string(m)
        headers = msg.keys()
        headers.sort()
        eq(headers, ['A', 'B', 'CC'])
        eq(msg.get_payload(), 'body')


class TestBase64(unittest.TestCase):

    def test_len(self):
        eq = self.assertEqual
        eq(base64mime.base64_len('hello'), len(base64mime.encode('hello', eol='')))
        for size in range(15):
            if size == 0:
                bsize = 0
            elif size <= 3:
                bsize = 4
            elif size <= 6:
                bsize = 8
            elif size <= 9:
                bsize = 12
            elif size <= 12:
                bsize = 16
            else:
                bsize = 20
            eq(base64mime.base64_len('x' * size), bsize)

    def test_decode(self):
        eq = self.assertEqual
        eq(base64mime.decode(''), '')
        eq(base64mime.decode('aGVsbG8='), 'hello')
        eq(base64mime.decode('aGVsbG8=', 'X'), 'hello')
        eq(base64mime.decode('aGVsbG8NCndvcmxk\n', 'X'), 'helloXworld')

    def test_encode(self):
        eq = self.assertEqual
        eq(base64mime.encode(''), '')
        eq(base64mime.encode('hello'), 'aGVsbG8=\n')
        eq(base64mime.encode('hello\n'), 'aGVsbG8K\n')
        eq(base64mime.encode('hello\n', 0), 'aGVsbG8NCg==\n')
        eq(base64mime.encode('xxxx ' * 20, maxlinelen=40), 'eHh4eCB4eHh4IHh4eHggeHh4eCB4eHh4IHh4eHgg\neHh4eCB4eHh4IHh4eHggeHh4eCB4eHh4IHh4eHgg\neHh4eCB4eHh4IHh4eHggeHh4eCB4eHh4IHh4eHgg\neHh4eCB4eHh4IA==\n')
        eq(base64mime.encode('xxxx ' * 20, maxlinelen=40, eol='\r\n'), 'eHh4eCB4eHh4IHh4eHggeHh4eCB4eHh4IHh4eHgg\r\neHh4eCB4eHh4IHh4eHggeHh4eCB4eHh4IHh4eHgg\r\neHh4eCB4eHh4IHh4eHggeHh4eCB4eHh4IHh4eHgg\r\neHh4eCB4eHh4IA==\r\n')

    def test_header_encode(self):
        eq = self.assertEqual
        he = base64mime.header_encode
        eq(he('hello'), '=?iso-8859-1?b?aGVsbG8=?=')
        eq(he('hello\nworld'), '=?iso-8859-1?b?aGVsbG8NCndvcmxk?=')
        eq(he('hello', charset='iso-8859-2'), '=?iso-8859-2?b?aGVsbG8=?=')
        eq(he('hello\nworld', keep_eols=True), '=?iso-8859-1?b?aGVsbG8Kd29ybGQ=?=')
        eq(he('xxxx ' * 20, maxlinelen=40), '=?iso-8859-1?b?eHh4eCB4eHh4IHh4eHggeHg=?=\n =?iso-8859-1?b?eHggeHh4eCB4eHh4IHh4eHg=?=\n =?iso-8859-1?b?IHh4eHggeHh4eCB4eHh4IHg=?=\n =?iso-8859-1?b?eHh4IHh4eHggeHh4eCB4eHg=?=\n =?iso-8859-1?b?eCB4eHh4IHh4eHggeHh4eCA=?=\n =?iso-8859-1?b?eHh4eCB4eHh4IHh4eHgg?=')
        eq(he('xxxx ' * 20, maxlinelen=40, eol='\r\n'), '=?iso-8859-1?b?eHh4eCB4eHh4IHh4eHggeHg=?=\r\n =?iso-8859-1?b?eHggeHh4eCB4eHh4IHh4eHg=?=\r\n =?iso-8859-1?b?IHh4eHggeHh4eCB4eHh4IHg=?=\r\n =?iso-8859-1?b?eHh4IHh4eHggeHh4eCB4eHg=?=\r\n =?iso-8859-1?b?eCB4eHh4IHh4eHggeHh4eCA=?=\r\n =?iso-8859-1?b?eHh4eCB4eHh4IHh4eHgg?=')


class TestQuopri(unittest.TestCase):

    def setUp(self):
        self.hlit = [ chr(x) for x in range(ord('a'), ord('z') + 1) ] + [ chr(x) for x in range(ord('A'), ord('Z') + 1) ] + [ chr(x) for x in range(ord('0'), ord('9') + 1) ] + [
         '!', '*', '+', '-', '/', ' ']
        self.hnon = [ chr(x) for x in range(256) if chr(x) not in self.hlit ]
        self.blit = [ chr(x) for x in range(ord(' '), ord('~') + 1) ] + ['\t']
        self.blit.remove('=')
        self.bnon = [ chr(x) for x in range(256) if chr(x) not in self.blit ]

    def test_header_quopri_check(self):
        for c in self.hlit:
            self.assertFalse(quoprimime.header_quopri_check(c))

        for c in self.hnon:
            self.assertTrue(quoprimime.header_quopri_check(c))

    def test_body_quopri_check(self):
        for c in self.blit:
            self.assertFalse(quoprimime.body_quopri_check(c))

        for c in self.bnon:
            self.assertTrue(quoprimime.body_quopri_check(c))

    def test_header_quopri_len(self):
        eq = self.assertEqual
        hql = quoprimime.header_quopri_len
        enc = quoprimime.header_encode
        for s in ('hello', 'h@e@l@l@o@'):
            eq(hql(s), len(enc(s, charset='', eol='')) - 7)

        for c in self.hlit:
            eq(hql(c), 1)

        for c in self.hnon:
            eq(hql(c), 3)

    def test_body_quopri_len(self):
        eq = self.assertEqual
        bql = quoprimime.body_quopri_len
        for c in self.blit:
            eq(bql(c), 1)

        for c in self.bnon:
            eq(bql(c), 3)

    def test_quote_unquote_idempotent(self):
        for x in range(256):
            c = chr(x)
            self.assertEqual(quoprimime.unquote(quoprimime.quote(c)), c)

    def test_header_encode(self):
        eq = self.assertEqual
        he = quoprimime.header_encode
        eq(he('hello'), '=?iso-8859-1?q?hello?=')
        eq(he('hello\nworld'), '=?iso-8859-1?q?hello=0D=0Aworld?=')
        eq(he('hello', charset='iso-8859-2'), '=?iso-8859-2?q?hello?=')
        eq(he('hello\nworld', keep_eols=True), '=?iso-8859-1?q?hello=0Aworld?=')
        eq(he(b'hello\xc7there'), '=?iso-8859-1?q?hello=C7there?=')
        eq(he('xxxx ' * 20, maxlinelen=40), '=?iso-8859-1?q?xxxx_xxxx_xxxx_xxxx_xx?=\n =?iso-8859-1?q?xx_xxxx_xxxx_xxxx_xxxx?=\n =?iso-8859-1?q?_xxxx_xxxx_xxxx_xxxx_x?=\n =?iso-8859-1?q?xxx_xxxx_xxxx_xxxx_xxx?=\n =?iso-8859-1?q?x_xxxx_xxxx_?=')
        eq(he('xxxx ' * 20, maxlinelen=40, eol='\r\n'), '=?iso-8859-1?q?xxxx_xxxx_xxxx_xxxx_xx?=\r\n =?iso-8859-1?q?xx_xxxx_xxxx_xxxx_xxxx?=\r\n =?iso-8859-1?q?_xxxx_xxxx_xxxx_xxxx_x?=\r\n =?iso-8859-1?q?xxx_xxxx_xxxx_xxxx_xxx?=\r\n =?iso-8859-1?q?x_xxxx_xxxx_?=')

    def test_decode(self):
        eq = self.assertEqual
        eq(quoprimime.decode(''), '')
        eq(quoprimime.decode('hello'), 'hello')
        eq(quoprimime.decode('hello', 'X'), 'hello')
        eq(quoprimime.decode('hello\nworld', 'X'), 'helloXworld')

    def test_encode(self):
        eq = self.assertEqual
        eq(quoprimime.encode(''), '')
        eq(quoprimime.encode('hello'), 'hello')
        eq(quoprimime.encode('hello\r\nworld'), 'hello\nworld')
        eq(quoprimime.encode('hello\r\nworld', 0), 'hello\nworld')
        eq(quoprimime.encode('xxxx ' * 20, maxlinelen=40), 'xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx=\n xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxx=\nx xxxx xxxx xxxx xxxx=20')
        eq(quoprimime.encode('xxxx ' * 20, maxlinelen=40, eol='\r\n'), 'xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx=\r\n xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxx=\r\nx xxxx xxxx xxxx xxxx=20')
        eq(quoprimime.encode('one line\n\ntwo line'), 'one line\n\ntwo line')


class TestCharset(unittest.TestCase):

    def tearDown(self):
        from email import charset as CharsetModule
        try:
            del CharsetModule.CHARSETS['fake']
        except KeyError:
            pass

    def test_idempotent(self):
        eq = self.assertEqual
        c = Charset('us-ascii')
        s = 'Hello World!'
        sp = c.to_splittable(s)
        eq(s, c.from_splittable(sp))
        s = b'\xa4\xa2\xa4\xa4\xa4\xa6\xa4\xa8\xa4\xaa'
        sp = c.to_splittable(s)
        eq(s, c.from_splittable(sp))

    def test_body_encode(self):
        eq = self.assertEqual
        c = Charset('iso-8859-1')
        eq('hello w=F6rld', c.body_encode(b'hello w\xf6rld'))
        c = Charset('utf-8')
        eq('aGVsbG8gd29ybGQ=\n', c.body_encode('hello world'))
        c = Charset('us-ascii')
        eq('hello world', c.body_encode('hello world'))
        c = Charset('euc-jp')
        try:
            eq('\x1b$B5FCO;~IW\x1b(B', c.body_encode(b'\xb5\xc6\xc3\xcf\xbb\xfe\xc9\xd7'))
            eq(b'\xb5\xc6\xc3\xcf\xbb\xfe\xc9\xd7', c.body_encode(b'\xb5\xc6\xc3\xcf\xbb\xfe\xc9\xd7', False))
        except LookupError:
            pass

        from email import charset as CharsetModule
        CharsetModule.add_charset('fake', CharsetModule.QP, None)
        c = Charset('fake')
        eq(b'hello w\xf6rld', c.body_encode(b'hello w\xf6rld'))
        return

    def test_unicode_charset_name(self):
        charset = Charset('us-ascii')
        self.assertEqual(str(charset), 'us-ascii')
        self.assertRaises(errors.CharsetError, Charset, b'asc\xffii')


class TestHeader(TestEmailBase):

    def test_simple(self):
        eq = self.ndiffAssertEqual
        h = Header('Hello World!')
        eq(h.encode(), 'Hello World!')
        h.append(' Goodbye World!')
        eq(h.encode(), 'Hello World!  Goodbye World!')

    def test_simple_surprise(self):
        eq = self.ndiffAssertEqual
        h = Header('Hello World!')
        eq(h.encode(), 'Hello World!')
        h.append('Goodbye World!')
        eq(h.encode(), 'Hello World! Goodbye World!')

    def test_header_needs_no_decoding(self):
        h = 'no decoding needed'
        self.assertEqual(decode_header(h), [(h, None)])
        return

    def test_long(self):
        h = Header("I am the very model of a modern Major-General; I've information vegetable, animal, and mineral; I know the kings of England, and I quote the fights historical from Marathon to Waterloo, in order categorical; I'm very well acquainted, too, with matters mathematical; I understand equations, both the simple and quadratical; about binomial theorem I'm teeming with a lot o' news, with many cheerful facts about the square of the hypotenuse.", maxlinelen=76)
        for l in h.encode(splitchars=' ').split('\n '):
            self.assertLessEqual(len(l), 76)

    def test_multilingual(self):
        eq = self.ndiffAssertEqual
        g = Charset('iso-8859-1')
        cz = Charset('iso-8859-2')
        utf8 = Charset('utf-8')
        g_head = b'Die Mieter treten hier ein werden mit einem Foerderband komfortabel den Korridor entlang, an s\xfcdl\xfcndischen Wandgem\xe4lden vorbei, gegen die rotierenden Klingen bef\xf6rdert. '
        cz_head = b'Finan\xe8ni metropole se hroutily pod tlakem jejich d\xf9vtipu.. '
        utf8_head = ('正確に言うと翻訳はされていません。一部はドイツ語ですが、あとはでたらめです。実際には「Wenn ist das Nunstuck git und Slotermeyer? Ja! Beiherhund das Oder die Flipperwaldt gersput.」と言っています。').encode('utf-8')
        h = Header(g_head, g)
        h.append(cz_head, cz)
        h.append(utf8_head, utf8)
        enc = h.encode()
        eq(enc, '=?iso-8859-1?q?Die_Mieter_treten_hier_ein_werden_mit_einem_Foerderband_ko?=\n =?iso-8859-1?q?mfortabel_den_Korridor_entlang=2C_an_s=FCdl=FCndischen_Wan?=\n =?iso-8859-1?q?dgem=E4lden_vorbei=2C_gegen_die_rotierenden_Klingen_bef=F6?=\n =?iso-8859-1?q?rdert=2E_?= =?iso-8859-2?q?Finan=E8ni_metropole_se_hroutily?=\n =?iso-8859-2?q?_pod_tlakem_jejich_d=F9vtipu=2E=2E_?= =?utf-8?b?5q2j56K6?=\n =?utf-8?b?44Gr6KiA44GG44Go57+76Kiz44Gv44GV44KM44Gm44GE44G+44Gb44KT44CC?=\n =?utf-8?b?5LiA6YOo44Gv44OJ44Kk44OE6Kqe44Gn44GZ44GM44CB44GC44Go44Gv44Gn?=\n =?utf-8?b?44Gf44KJ44KB44Gn44GZ44CC5a6f6Zqb44Gr44Gv44CMV2VubiBpc3QgZGFz?=\n =?utf-8?q?_Nunstuck_git_und_Slotermeyer=3F_Ja!_Beiherhund_das_Oder_die_Fl?=\n =?utf-8?b?aXBwZXJ3YWxkdCBnZXJzcHV0LuOAjeOBqOiogOOBo+OBpuOBhOOBvuOBmQ==?=\n =?utf-8?b?44CC?=')
        eq(decode_header(enc), [
         (
          g_head, 'iso-8859-1'), (cz_head, 'iso-8859-2'),
         (
          utf8_head, 'utf-8')])
        ustr = unicode(h)
        eq(ustr.encode('utf-8'), 'Die Mieter treten hier ein werden mit einem Foerderband komfortabel den Korridor entlang, an südlündischen Wandgemälden vorbei, gegen die rotierenden Klingen befördert. Finančni metropole se hroutily pod tlakem jejich důvtipu.. 正確に言うと翻訳はされていません。一部はドイツ語ですが、あとはでたらめです。実際には「Wenn ist das Nunstuck git und Slotermeyer? Ja! Beiherhund das Oder die Flipperwaldt gersput.」と言っています。')
        newh = make_header(decode_header(enc))
        eq(newh, enc)

    def test_header_ctor_default_args(self):
        eq = self.ndiffAssertEqual
        h = Header()
        eq(h, '')
        h.append('foo', Charset('iso-8859-1'))
        eq(h, '=?iso-8859-1?q?foo?=')

    def test_explicit_maxlinelen(self):
        eq = self.ndiffAssertEqual
        hstr = 'A very long line that must get split to something other than at the 76th character boundary to test the non-default behavior'
        h = Header(hstr)
        eq(h.encode(), 'A very long line that must get split to something other than at the 76th\n character boundary to test the non-default behavior')
        h = Header(hstr, header_name='Subject')
        eq(h.encode(), 'A very long line that must get split to something other than at the\n 76th character boundary to test the non-default behavior')
        h = Header(hstr, maxlinelen=1024, header_name='Subject')
        eq(h.encode(), hstr)

    def test_us_ascii_header(self):
        eq = self.assertEqual
        s = 'hello'
        x = decode_header(s)
        eq(x, [('hello', None)])
        h = make_header(x)
        eq(s, h.encode())
        return

    def test_string_charset(self):
        eq = self.assertEqual
        h = Header()
        h.append('hello', 'iso-8859-1')
        eq(h, '=?iso-8859-1?q?hello?=')

    def test_utf8_shortest(self):
        eq = self.assertEqual
        h = Header('pöstal', 'utf-8')
        eq(h.encode(), '=?utf-8?q?p=C3=B6stal?=')
        h = Header('菊地時夫', 'utf-8')
        eq(h.encode(), '=?utf-8?b?6I+K5Zyw5pmC5aSr?=')

    def test_bad_8bit_header(self):
        raises = self.assertRaises
        eq = self.assertEqual
        x = b'Ynwp4dUEbay Auction Semiar- No Charge \x96 Earn Big'
        raises(UnicodeError, Header, x)
        h = Header()
        raises(UnicodeError, h.append, x)
        eq(str(Header(x, errors='replace')), x)
        h.append(x, errors='replace')
        eq(str(h), x)

    def test_encoded_adjacent_nonencoded(self):
        eq = self.assertEqual
        h = Header()
        h.append('hello', 'iso-8859-1')
        h.append('world')
        s = h.encode()
        eq(s, '=?iso-8859-1?q?hello?= world')
        h = make_header(decode_header(s))
        eq(h.encode(), s)

    def test_whitespace_eater(self):
        eq = self.assertEqual
        s = 'Subject: =?koi8-r?b?8NLP18XSy8EgzsEgxsnOwczYztk=?= =?koi8-r?q?=CA?= zz.'
        parts = decode_header(s)
        eq(parts, [('Subject:', None), (b'\xf0\xd2\xcf\xd7\xc5\xd2\xcb\xc1 \xce\xc1 \xc6\xc9\xce\xc1\xcc\xd8\xce\xd9\xca',
 'koi8-r'), ('zz.', None)])
        hdr = make_header(parts)
        eq(hdr.encode(), 'Subject: =?koi8-r?b?8NLP18XSy8EgzsEgxsnOwczYztnK?= zz.')
        return

    def test_broken_base64_header(self):
        raises = self.assertRaises
        s = 'Subject: =?EUC-KR?B?CSixpLDtKSC/7Liuvsax4iC6uLmwMcijIKHaILzSwd/H0SC8+LCjwLsgv7W/+Mj3I ?='
        raises(errors.HeaderParseError, decode_header, s)


class TestRFC2231(TestEmailBase):

    def test_get_param(self):
        eq = self.assertEqual
        msg = self._msgobj('msg_29.txt')
        eq(msg.get_param('title'), ('us-ascii', 'en', "This is even more ***fun*** isn't it!"))
        eq(msg.get_param('title', unquote=False), ('us-ascii', 'en', '"This is even more ***fun*** isn\'t it!"'))

    def test_set_param(self):
        eq = self.assertEqual
        msg = Message()
        msg.set_param('title', "This is even more ***fun*** isn't it!", charset='us-ascii')
        eq(msg.get_param('title'), ('us-ascii', '', "This is even more ***fun*** isn't it!"))
        msg.set_param('title', "This is even more ***fun*** isn't it!", charset='us-ascii', language='en')
        eq(msg.get_param('title'), ('us-ascii', 'en', "This is even more ***fun*** isn't it!"))
        msg = self._msgobj('msg_01.txt')
        msg.set_param('title', "This is even more ***fun*** isn't it!", charset='us-ascii', language='en')
        self.ndiffAssertEqual(msg.as_string(), 'Return-Path: <bbb@zzz.org>\nDelivered-To: bbb@zzz.org\nReceived: by mail.zzz.org (Postfix, from userid 889)\n id 27CEAD38CC; Fri,  4 May 2001 14:05:44 -0400 (EDT)\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\nMessage-ID: <15090.61304.110929.45684@aaa.zzz.org>\nFrom: bbb@ddd.com (John X. Doe)\nTo: bbb@zzz.org\nSubject: This is a test message\nDate: Fri, 4 May 2001 14:05:44 -0400\nContent-Type: text/plain; charset=us-ascii;\n title*="us-ascii\'en\'This%20is%20even%20more%20%2A%2A%2Afun%2A%2A%2A%20isn%27t%20it%21"\n\n\nHi,\n\nDo you like this message?\n\n-Me\n')

    def test_del_param(self):
        eq = self.ndiffAssertEqual
        msg = self._msgobj('msg_01.txt')
        msg.set_param('foo', 'bar', charset='us-ascii', language='en')
        msg.set_param('title', "This is even more ***fun*** isn't it!", charset='us-ascii', language='en')
        msg.del_param('foo', header='Content-Type')
        eq(msg.as_string(), 'Return-Path: <bbb@zzz.org>\nDelivered-To: bbb@zzz.org\nReceived: by mail.zzz.org (Postfix, from userid 889)\n id 27CEAD38CC; Fri,  4 May 2001 14:05:44 -0400 (EDT)\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\nMessage-ID: <15090.61304.110929.45684@aaa.zzz.org>\nFrom: bbb@ddd.com (John X. Doe)\nTo: bbb@zzz.org\nSubject: This is a test message\nDate: Fri, 4 May 2001 14:05:44 -0400\nContent-Type: text/plain; charset="us-ascii";\n title*="us-ascii\'en\'This%20is%20even%20more%20%2A%2A%2Afun%2A%2A%2A%20isn%27t%20it%21"\n\n\nHi,\n\nDo you like this message?\n\n-Me\n')

    def test_rfc2231_get_content_charset(self):
        eq = self.assertEqual
        msg = self._msgobj('msg_32.txt')
        eq(msg.get_content_charset(), 'us-ascii')

    def test_rfc2231_no_language_or_charset(self):
        m = 'Content-Transfer-Encoding: 8bit\nContent-Disposition: inline; filename="file____C__DOCUMENTS_20AND_20SETTINGS_FABIEN_LOCAL_20SETTINGS_TEMP_nsmail.htm"\nContent-Type: text/html; NAME*0=file____C__DOCUMENTS_20AND_20SETTINGS_FABIEN_LOCAL_20SETTINGS_TEM; NAME*1=P_nsmail.htm\n\n'
        msg = email.message_from_string(m)
        param = msg.get_param('NAME')
        self.assertFalse(isinstance(param, tuple))
        self.assertEqual(param, 'file____C__DOCUMENTS_20AND_20SETTINGS_FABIEN_LOCAL_20SETTINGS_TEMP_nsmail.htm')

    def test_rfc2231_no_language_or_charset_in_filename(self):
        m = 'Content-Disposition: inline;\n\tfilename*0*="\'\'This%20is%20even%20more%20";\n\tfilename*1*="%2A%2A%2Afun%2A%2A%2A%20";\n\tfilename*2="is it not.pdf"\n\n'
        msg = email.message_from_string(m)
        self.assertEqual(msg.get_filename(), 'This is even more ***fun*** is it not.pdf')

    def test_rfc2231_no_language_or_charset_in_filename_encoded(self):
        m = 'Content-Disposition: inline;\n\tfilename*0*="\'\'This%20is%20even%20more%20";\n\tfilename*1*="%2A%2A%2Afun%2A%2A%2A%20";\n\tfilename*2="is it not.pdf"\n\n'
        msg = email.message_from_string(m)
        self.assertEqual(msg.get_filename(), 'This is even more ***fun*** is it not.pdf')

    def test_rfc2231_partly_encoded(self):
        m = 'Content-Disposition: inline;\n\tfilename*0="\'\'This%20is%20even%20more%20";\n\tfilename*1*="%2A%2A%2Afun%2A%2A%2A%20";\n\tfilename*2="is it not.pdf"\n\n'
        msg = email.message_from_string(m)
        self.assertEqual(msg.get_filename(), 'This%20is%20even%20more%20***fun*** is it not.pdf')

    def test_rfc2231_partly_nonencoded(self):
        m = 'Content-Disposition: inline;\n\tfilename*0="This%20is%20even%20more%20";\n\tfilename*1="%2A%2A%2Afun%2A%2A%2A%20";\n\tfilename*2="is it not.pdf"\n\n'
        msg = email.message_from_string(m)
        self.assertEqual(msg.get_filename(), 'This%20is%20even%20more%20%2A%2A%2Afun%2A%2A%2A%20is it not.pdf')

    def test_rfc2231_no_language_or_charset_in_boundary(self):
        m = 'Content-Type: multipart/alternative;\n\tboundary*0*="\'\'This%20is%20even%20more%20";\n\tboundary*1*="%2A%2A%2Afun%2A%2A%2A%20";\n\tboundary*2="is it not.pdf"\n\n'
        msg = email.message_from_string(m)
        self.assertEqual(msg.get_boundary(), 'This is even more ***fun*** is it not.pdf')

    def test_rfc2231_no_language_or_charset_in_charset(self):
        m = 'Content-Type: text/plain;\n\tcharset*0*="This%20is%20even%20more%20";\n\tcharset*1*="%2A%2A%2Afun%2A%2A%2A%20";\n\tcharset*2="is it not.pdf"\n\n'
        msg = email.message_from_string(m)
        self.assertEqual(msg.get_content_charset(), 'this is even more ***fun*** is it not.pdf')

    def test_rfc2231_bad_encoding_in_filename(self):
        m = 'Content-Disposition: inline;\n\tfilename*0*="bogus\'xx\'This%20is%20even%20more%20";\n\tfilename*1*="%2A%2A%2Afun%2A%2A%2A%20";\n\tfilename*2="is it not.pdf"\n\n'
        msg = email.message_from_string(m)
        self.assertEqual(msg.get_filename(), 'This is even more ***fun*** is it not.pdf')

    def test_rfc2231_bad_encoding_in_charset(self):
        m = "Content-Type: text/plain; charset*=bogus''utf-8%E2%80%9D\n\n"
        msg = email.message_from_string(m)
        self.assertEqual(msg.get_content_charset(), None)
        return

    def test_rfc2231_bad_character_in_charset(self):
        m = "Content-Type: text/plain; charset*=ascii''utf-8%E2%80%9D\n\n"
        msg = email.message_from_string(m)
        self.assertEqual(msg.get_content_charset(), None)
        return

    def test_rfc2231_bad_character_in_filename(self):
        m = 'Content-Disposition: inline;\n\tfilename*0*="ascii\'xx\'This%20is%20even%20more%20";\n\tfilename*1*="%2A%2A%2Afun%2A%2A%2A%20";\n\tfilename*2*="is it not.pdf%E2"\n\n'
        msg = email.message_from_string(m)
        self.assertEqual(msg.get_filename(), 'This is even more ***fun*** is it not.pdf�')

    def test_rfc2231_unknown_encoding(self):
        m = "Content-Transfer-Encoding: 8bit\nContent-Disposition: inline; filename*=X-UNKNOWN''myfile.txt\n\n"
        msg = email.message_from_string(m)
        self.assertEqual(msg.get_filename(), 'myfile.txt')

    def test_rfc2231_single_tick_in_filename_extended(self):
        eq = self.assertEqual
        m = 'Content-Type: application/x-foo;\n\tname*0*="Frank\'s"; name*1*=" Document"\n\n'
        msg = email.message_from_string(m)
        charset, language, s = msg.get_param('name')
        eq(charset, None)
        eq(language, None)
        eq(s, "Frank's Document")
        return

    def test_rfc2231_single_tick_in_filename(self):
        m = 'Content-Type: application/x-foo; name*0="Frank\'s"; name*1=" Document"\n\n'
        msg = email.message_from_string(m)
        param = msg.get_param('name')
        self.assertFalse(isinstance(param, tuple))
        self.assertEqual(param, "Frank's Document")

    def test_rfc2231_tick_attack_extended(self):
        eq = self.assertEqual
        m = 'Content-Type: application/x-foo;\n\tname*0*="us-ascii\'en-us\'Frank\'s"; name*1*=" Document"\n\n'
        msg = email.message_from_string(m)
        charset, language, s = msg.get_param('name')
        eq(charset, 'us-ascii')
        eq(language, 'en-us')
        eq(s, "Frank's Document")

    def test_rfc2231_tick_attack(self):
        m = 'Content-Type: application/x-foo;\n\tname*0="us-ascii\'en-us\'Frank\'s"; name*1=" Document"\n\n'
        msg = email.message_from_string(m)
        param = msg.get_param('name')
        self.assertFalse(isinstance(param, tuple))
        self.assertEqual(param, "us-ascii'en-us'Frank's Document")

    def test_rfc2231_no_extended_values(self):
        eq = self.assertEqual
        m = 'Content-Type: application/x-foo; name="Frank\'s Document"\n\n'
        msg = email.message_from_string(m)
        eq(msg.get_param('name'), "Frank's Document")

    def test_rfc2231_encoded_then_unencoded_segments(self):
        eq = self.assertEqual
        m = 'Content-Type: application/x-foo;\n\tname*0*="us-ascii\'en-us\'My";\n\tname*1=" Document";\n\tname*2*=" For You"\n\n'
        msg = email.message_from_string(m)
        charset, language, s = msg.get_param('name')
        eq(charset, 'us-ascii')
        eq(language, 'en-us')
        eq(s, 'My Document For You')

    def test_rfc2231_unencoded_then_encoded_segments(self):
        eq = self.assertEqual
        m = 'Content-Type: application/x-foo;\n\tname*0="us-ascii\'en-us\'My";\n\tname*1*=" Document";\n\tname*2*=" For You"\n\n'
        msg = email.message_from_string(m)
        charset, language, s = msg.get_param('name')
        eq(charset, 'us-ascii')
        eq(language, 'en-us')
        eq(s, 'My Document For You')


def _testclasses():
    mod = sys.modules[__name__]
    return [ getattr(mod, name) for name in dir(mod) if name.startswith('Test') ]


def suite():
    suite = unittest.TestSuite()
    for testclass in _testclasses():
        suite.addTest(unittest.makeSuite(testclass))

    return suite


def test_main():
    for testclass in _testclasses():
        run_unittest(testclass)


if __name__ == '__main__':
    unittest.main(defaultTest='suite')