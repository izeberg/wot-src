__author__ = 'Guido van Rossum <guido@python.org>'
__all__ = [
 'Driver', 'load_grammar']
import codecs, os, logging, pkgutil, StringIO, sys
from . import grammar, parse, token, tokenize, pgen

class Driver(object):

    def __init__(self, grammar, convert=None, logger=None):
        self.grammar = grammar
        if logger is None:
            logger = logging.getLogger()
        self.logger = logger
        self.convert = convert
        return

    def parse_tokens(self, tokens, debug=False):
        p = parse.Parser(self.grammar, self.convert)
        p.setup()
        lineno = 1
        column = 0
        type = value = start = end = line_text = None
        prefix = ''
        for quintuple in tokens:
            type, value, start, end, line_text = quintuple
            if start != (lineno, column):
                s_lineno, s_column = start
                if lineno < s_lineno:
                    prefix += '\n' * (s_lineno - lineno)
                    lineno = s_lineno
                    column = 0
                if column < s_column:
                    prefix += line_text[column:s_column]
                    column = s_column
            if type in (tokenize.COMMENT, tokenize.NL):
                prefix += value
                lineno, column = end
                if value.endswith('\n'):
                    lineno += 1
                    column = 0
                continue
            if type == token.OP:
                type = grammar.opmap[value]
            if debug:
                self.logger.debug('%s %r (prefix=%r)', token.tok_name[type], value, prefix)
            if p.addtoken(type, value, (prefix, start)):
                if debug:
                    self.logger.debug('Stop.')
                break
            prefix = ''
            lineno, column = end
            if value.endswith('\n'):
                lineno += 1
                column = 0
        else:
            raise parse.ParseError('incomplete input', type, value, (prefix, start))

        return p.rootnode

    def parse_stream_raw(self, stream, debug=False):
        tokens = tokenize.generate_tokens(stream.readline)
        return self.parse_tokens(tokens, debug)

    def parse_stream(self, stream, debug=False):
        return self.parse_stream_raw(stream, debug)

    def parse_file(self, filename, encoding=None, debug=False):
        stream = codecs.open(filename, 'r', encoding)
        try:
            return self.parse_stream(stream, debug)
        finally:
            stream.close()

    def parse_string(self, text, debug=False):
        tokens = tokenize.generate_tokens(StringIO.StringIO(text).readline)
        return self.parse_tokens(tokens, debug)


def _generate_pickle_name(gt):
    head, tail = os.path.splitext(gt)
    if tail == '.txt':
        tail = ''
    return head + tail + ('.').join(map(str, sys.version_info)) + '.pickle'


def load_grammar(gt='Grammar.txt', gp=None, save=True, force=False, logger=None):
    if logger is None:
        logger = logging.getLogger()
    gp = _generate_pickle_name(gt) if gp is None else gp
    if force or not _newer(gp, gt):
        logger.info('Generating grammar tables from %s', gt)
        g = pgen.generate_grammar(gt)
        if save:
            logger.info('Writing grammar tables to %s', gp)
            try:
                g.dump(gp)
            except IOError as e:
                logger.info('Writing failed: %s', e)

    else:
        g = grammar.Grammar()
        g.load(gp)
    return g


def _newer(a, b):
    if not os.path.exists(a):
        return False
    if not os.path.exists(b):
        return True
    return os.path.getmtime(a) >= os.path.getmtime(b)


def load_packaged_grammar(package, grammar_source):
    if os.path.isfile(grammar_source):
        return load_grammar(grammar_source)
    pickled_name = _generate_pickle_name(os.path.basename(grammar_source))
    data = pkgutil.get_data(package, pickled_name)
    g = grammar.Grammar()
    g.loads(data)
    return g


def main(*args):
    if not args:
        args = sys.argv[1:]
    logging.basicConfig(level=logging.INFO, stream=sys.stdout, format='%(message)s')
    for gt in args:
        load_grammar(gt, save=True, force=True)

    return True


if __name__ == '__main__':
    sys.exit(int(not main()))