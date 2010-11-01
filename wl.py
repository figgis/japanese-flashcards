#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unicodedata
import sys
import codecs
import urllib
from table_parser import *

out = codecs.getwriter('utf-8')(sys.stdout)

for i in range(1, 24):
    f = urllib.urlopen('genki/genki_vocab_table.php?lesson=%d' % (i))
    p = TableParser()
    p.feed(f.read())
    f.close()
    for lst in p.doc[0][1:]:
        sys.stdout.flush()
#        print lst
#        sys.exit()
        kana = lst[0].strip()
        kanji = lst[1].strip()
        eng = lst[-1].strip()
        #skip na-adjektiv
        if u'（な）' in kana:
            out.write('type\n')
            if kanji is not '':
                out.write(kanji+'\n')
            out.write(kana+'\n')
            out.write(eng+'\n')
            out.write('\n')
        # skriv ut på formatet
        # -typ
        # -kanji
        # -kana
        # -engelska
#        out.write('type\n')
#        if kanji is not '':
#            out.write(kanji+'\n')
#        out.write(kana+'\n')
#        out.write(eng+'\n')
#        out.write('\n')
#        if u'to ' in eng:
#            out.write('type\n')
#            if kanji is not '':
#                out.write(kanji+'\n')
#            out.write(kana+'\n')
#            out.write(eng+'\n')
#            out.write('\n')
