# -*- coding: utf-8 -*-

import re
import unicodedata
from ._compat import _unicode
from abydos.bmdata import bmdata, l_any, l_arabic, l_cyrillic, l_czech, \
    l_dutch, l_english, l_french, l_german, l_greek, l_greeklatin, l_hebrew, \
    l_hungarian, l_italian, l_polish, l_portuguese, l_romanian, l_russian, \
    l_spanish, l_turkish

lang_dict = {'any': l_any, 'arabic': l_arabic, 'cyrillic': l_cyrillic,
             'czech': l_czech, 'dutch': l_dutch, 'english': l_english,
             'french': l_french, 'german': l_german, 'greek': l_greek,
             'greeklatin': l_greeklatin, 'hebrew': l_hebrew,
             'hungarian': l_hungarian, 'italian': l_italian, 'polish': l_polish,
             'portuguese': l_portuguese, 'romanian': l_romanian,
             'russian': l_russian, 'spanish': l_spanish, 'turkish': l_turkish}

bmdata['gen']['discards'] = ('da ', 'dal ', 'de ', 'del ', 'dela ', 'de la ',
                             'della ', 'des ', 'di ', 'do ', 'dos ', 'du ',
                             'van ', 'von ', 'd\'')
bmdata['ash']['discards'] = ('bar', 'ben', 'da', 'de', 'van', 'von')
bmdata['sep']['discards'] = ('al', 'el', 'da', 'dal', 'de', 'del', 'dela',
                             'de la', 'della', 'des', 'di', 'do', 'dos', 'du',
                             'van', 'von')

name_type = 'gen' # other options include 'sep' & 'ash'

def language(name, rules, lang_choices):
    name = name.strip().lower()
    choices_remaining = lang_choices
    for rule in rules:
        letters, languages, accept = rule
        if re.search(letters, name) != None:
            if accept:
                choices_remaining &= languages
            else:
                choices_remaining &= (~languages) % (lang_choices+1)
    if choices_remaining == 0:
        choices_remaining = 1
    return choices_remaining

def redo_language(term, rules, final_rules1, final_rules2, language_arg, concat, lang_choices):
    lang_choices = language(term, language_arg, lang_choices)

def phonetic(term, rules, final_rules1, final_rules2, language_arg='', concat=False):
    term = term.replace('-', ' ').strip()
    


def bmpm(word, language='', ntype='gen'):
    """Return the Beider-Morse Phonetic Matching algorithm encoding(s) of a
    term

    Arguments:
    word -- the term to which to apply the Beider-Morse Phonetic Matching
            algorithm
    language -- the language of the term; supported values include:
                ....
    type -- the variant form of the algorithm: 'gen' (default),
            'ash' (Ashkenazi), or 'sep' (Sephardic)

    Description:
    The Beider-Morse Phonetic Matching algorithm is described at:
    http://stevemorse.org/phonetics/bmpm.htm
    The reference implementation is licensed under GPLv3 and available at:
    http://stevemorse.org/phoneticinfo.htm
    """
    word = unicodedata.normalize('NFC', _unicode(word.strip().lower()))

    global name_type
    name_type = ntype.strip().lower()[:3]
    if name_type not in ['ash', 'sep']:
        name_type = 'gen'
    if language not in lang_dict:
        language_choices = language(word, bmdata[name_type]['language_rules'])
    
    phonetic(word, )

    return word
