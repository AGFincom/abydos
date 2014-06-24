#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""features_csv_to_dict.py

This script converts a CSV document of feature values to a Python dict.

The CSV document is of the format
<phonetic symbol(s)>,<variant number>,<segmental>,<feature>+

    Phonetic symbols are IPA (or other system) symbols.
    Variant number refers to one of the following codes:
         0 = IPA
         1 = Americanist
         2 = IPA variant
         3 = Americanist variant
         9 = other
    Segmental must be either 1 (segmental) or 0 (featural). Featural symbols
    replace features on the preceding segmental symbol.
    Features may be 1 (+), -1 (-), or 0 (0) to indicate feature values.

Lines beginning with # are interpreted as comments


Copyright 2014 by Christopher C. Little.
This file is part of Abydos.

Abydos is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Abydos is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Abydos. If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import unicode_literals
import sys, getopt, codecs
import unicodedata

def main(argv):
    """Main conversion script
    """
    def print_usage():
        """Print usage statement
        """
        print 'features_csv_to_dict.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
        
    def binarize(num):
        """Replace 0, -1, 1 with 11, 10, 01
        """
        if num == '0':
            return '11'
        elif num == '-1':
            return '10'
        elif num == '1':
            return '01'


    ifile = ''
    ofile = ''
    try:
        opts = getopt.getopt(argv, "hi:o:", ["ifile=","ofile="])[0]
    except getopt.GetoptError:
        print_usage()
    for opt, arg in opts:
        if opt == '-h':
            print_usage()
        elif opt in ("-i", "--ifile"):
            ifile = codecs.open(arg, 'r', 'utf-8')
        elif opt in ("-o", "--ofile"):
            ofile = codecs.open(arg, 'w', 'utf-8')
    if not ifile:
        print_usage()

    oline = 'PHONETIC_FEATURES = {'
    if not ofile:
        print(oline)
    else:
        ofile.write(oline+'\n')

    next(ifile)
    for line in ifile:
        if not line.startswith('#'):
            line = line.strip().split(',')
            symbol = line[0]
            variant = int(line[1])
            segmental = bool(line[2])
            features = '0b' + ''.join([binarize(val) for val in line[3:]])
            if not segmental:
                features = '-' + features

            if variant == 0 or variant == 2:
                oline = '                     \'{}\': {},'.format(symbol,
                                                                  features)
                if not ofile:
                    print(oline)
                else:
                    ofile.write(oline+'\n')

    oline = '                    }'
    if not ofile:
        print(oline)
    else:
        ofile.write(oline+'\n')


if __name__ == "__main__":
    main(sys.argv[1:])