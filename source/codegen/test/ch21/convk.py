'''
File code convertor from euc-kr to utf-8  or utf-8 to euc-kr
Usage :
        python convk.py -ue a.txt b.txt
        python convk.py -eu a.txt b.txt

Options:
        u : utf-8
        e : euc-kr
        eu : from euc-kr to utf-8
        ue : from utf-8 to euc-kr

Same file names are used to create new files.
i.e.  a.txt(euc-kr) --> a.txt(utf-8)

Gang Seong Lee
2001.11.9
'''

import codecs
import sys
import getopt

def euckr_to_utf8(msg):
        'convert string from euc-kr to utf-8'
        UTF8_encode = codecs.lookup('UTF-8')[0]
        return UTF8_encode(unicode(msg, "euc-kr"))[0]

def utf8_to_euckr(msg):
        'convert string from utf-8 to euc-kr'
        UTF8_decode = codecs.lookup('UTF-8')[1]
        EUCKR_encode = codecs.lookup('euc-kr')[0]
        return EUCKR_encode(UTF8_decode(msg)[0])[0]

def convert(fname_from, fname_to, mode):
        '''convert char set of file.
        fname_from --> fname_to
        mode : eu - euckr to utf8
        mode : ue - utf8 to euckr
        '''
        f = open(fname_from)
        s = f.read()
        if mode == 'eu': # euckr to utf8
                s = euckr_to_utf8(s)
        elif mode == 'ue': # utf8 to euckr
                s = utf8_to_euckr(s)
        f = open(fname_to, 'w')
        f.write(s)
        f.close()

if __name__ == '__main__':
        options, args = getopt.getopt(sys.argv[1:], 'eu')
        seq = []
        for op, p in options:
                if op in ('-e', '-u'):
                        seq.append(op[1])
                else:
                        print 'Unknown option', op
        seq = ''.join(seq)
        if seq not in ('eu', 'ue'):
                print __doc__
                sys.exit()
        for fname in args:
                print 'Converting', fname, '..'
                convert(fname, fname, seq)
        print 'done..'
