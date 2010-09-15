#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unicodedata
import pickle
import sys
import codecs
import urllib
from table_parser import *

tmp=r'''
\documentclass[avery5371,grid,frame]{flashcards}
\usepackage{fontspec}
\setmainfont{Sazanami Mincho}

\cardfrontstyle[\large\slshape]{headings}
\cardbackstyle{empty}
\begin{document}
\cardfrontfoot{Genki I}
'''

card=r'''
\begin{flashcard}[@3]{\huge{@1}}
\medskip
\Large{@2}
\end{flashcard}
'''

latex_pre=unicode(tmp, 'utf-8')
del tmp

out = codecs.getwriter('utf-8')(sys.stdout)

def make_card(buf):
    pass

out.write(latex_pre)
for i in range(1, 24):
    f = urllib.urlopen('../genki/genki_vocab_table.php?lesson=%d' % (i))
    p = TableParser()
    p.feed(f.read())
    f.close()
    for lst in p.doc[0][1:]:
        sys.stdout.flush()
        c = card
        kana = lst[0]
        kanji = lst[1]
        eng = lst[-1]
        if kanji != '':
            kana = kanji + r' \\ ' + kana
        c = c.replace('@1', kana)
        c = c.replace('@2', eng)
        c = c.replace('@3', "Lesson %d" % (i))
        out.write(c)
out.write(r'\end{document}')
