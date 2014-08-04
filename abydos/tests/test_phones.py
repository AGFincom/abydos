# -*- coding: utf-8 -*-
"""abydos.tests.test_phones

This module contains unit tests for abydos.phones

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
import unittest
from abydos.phones import ipa_to_features, get_feature, cmp_features
from math import isnan


class IpaFeaturesTestCases(unittest.TestCase):
    """test cases for abydos.phones.ipa_to_features
    """
    def test_ipa_to_features(self):
        """test abydos.phones.ipa_to_features
        """
        self.assertEqual(ipa_to_features('medçen'),
                         [2709662981243185770,
                          1826957430176000426,
                          2783230754501864106,
                          2783233463150094762,
                          1826957430176000426,
                          2711173160463936106])
        self.assertEqual(ipa_to_features('axtuŋ'),
                         [1826957425952336298,
                          2783233462881659306,
                          2783230754502126250,
                          1825831513894594986,
                          2711175868843469418])
        self.assertEqual(ipa_to_features('iç'),
                         [1826957412996131242,
                          2783233463150094762])
        self.assertEqual(ipa_to_features('bakofen'),
                         [2781720575281113770,
                          1826957425952336298,
                          2783233462881659562,
                          1825831531074464170,
                          2781702983095331242,
                          1826957430176000426,
                          2711173160463936106])
        self.assertEqual(ipa_to_features('dʒuŋel'),
                         [2783230754501864106,
                          2783231556184353178,
                          1825831513894594986,
                          2711175868843469418,
                          1826957430176000426,
                          2693158761954453926])
        self.assertEqual(ipa_to_features('kvatʃ'),
                         [2783233462881659562,
                          2781702983095069098,
                          1826957425952336298,
                          2783230754502126250,
                          2783231556184615322])
        self.assertEqual(ipa_to_features('nitʃe'),
                         [2711173160463936106,
                          1826957412996131242,
                          2783230754502126250,
                          2783231556184615322,
                          1826957430176000426])
        self.assertEqual(ipa_to_features('klø'),
                         [2783233462881659562,
                          2693158761954453926,
                          1825831530269157802])
        self.assertEqual(ipa_to_features('kybax'),
                         [2783233462881659562,
                          1825831513089288618,
                          2781720575281113770,
                          1826957425952336298,
                          2783233462881659306])
        self.assertEqual(ipa_to_features('i@c'),
                         [1826957412996131242,
                          -1,
                          2783233463150095018])


class HasFeatureTestCases(unittest.TestCase):
    """test cases for abydos.phones.get_feature
    """
    def test_ipa_to_features(self):
        """test abydos.phones.get_feature
        """
        self.assertEqual(get_feature(ipa_to_features('medçen'), 'nasal'),
                         [1, -1, -1, -1, -1, 1])
        self.assertRaises(AttributeError, get_feature,
                          ipa_to_features('medçen'), 'vocalic')

        self.assertEqual(get_feature(ipa_to_features('nitʃe'), 'nasal'),
                         [1, -1, -1, -1, -1])
        self.assertEqual(get_feature(ipa_to_features('nitʃe'), 'strident'),
                         [-1, -1, -1, 1, -1])
        self.assertEqual(get_feature(ipa_to_features('nitʃe'), 'syllabic'),
                         [-1, 1, -1, -1, 1])
        self.assertEqual(get_feature(ipa_to_features('nitʃe'), 'continuant'),
                         [-1, 1, -1, 1, 1])

        self.assertEqual(get_feature(ipa_to_features('nit͡ʃe'), 'nasal'),
                         [1, -1, -1, -1])
        self.assertEqual(get_feature(ipa_to_features('nit͡ʃe'), 'strident'),
                         [-1, -1, 1, -1])
        self.assertEqual(get_feature(ipa_to_features('nit͡ʃe'), 'syllabic'),
                         [-1, 1, -1, 1])
        self.assertEqual(get_feature(ipa_to_features('nit͡ʃe'), 'continuant'),
                         [-1, 1, 2, 1])

        self.assertEqual(get_feature(ipa_to_features('løvenbroy'), 'atr'),
                         [0, 1, 0, 1, 0, 0, 0, 1, 1])
        self.assertNotEqual(get_feature(ipa_to_features('i@c'), 'syllabic'),
                            [1, float('NaN'), -1])
        self.assertTrue(isnan(get_feature(ipa_to_features('i@c'),
                                              'syllabic')[1]))


class CmpFeaturesTestCases(unittest.TestCase):
    """test cases for abydos.phones.cmp_features
    """
    def test_cmp_features(self):
        """test abydos.phones.cmp_features
        """
        ## negatives
        self.assertEqual(cmp_features(-1, 1826957425952336298), -1)
        self.assertEqual(cmp_features(1826957425952336298, -1), -1)
        self.assertEqual(cmp_features(-1, -1), -1)
        ## equals
        self.assertEqual(cmp_features(0, 0), 1)
        self.assertEqual(cmp_features(1826957425952336298,
                                      1826957425952336298), 1)

        ## unequals
        # pre-calc everything
        cced = ipa_to_features('ç')[0]
        esh = ipa_to_features('ʃ')[0]
        tesh = ipa_to_features('t͡ʃ')[0]

        cmp_cced_tesh = cmp_features(cced, tesh)
        cmp_cced_esh = cmp_features(cced, esh)
        cmp_esh_tesh = cmp_features(esh, tesh)

        cmp_tesh_cced = cmp_features(tesh, cced)
        cmp_esh_cced = cmp_features(esh, cced)
        cmp_tesh_esh = cmp_features(tesh, esh)

        # check symmetric equality
        self.assertEqual(cmp_cced_tesh, cmp_tesh_cced)
        self.assertEqual(cmp_cced_esh, cmp_esh_cced)
        self.assertEqual(cmp_esh_tesh, cmp_tesh_esh)

        # check that they're all greater than 0
        self.assertGreater(cmp_cced_tesh, 0)
        self.assertGreater(cmp_cced_esh, 0)
        self.assertGreater(cmp_esh_tesh, 0)

        # check that they're all less than 1
        self.assertLess(cmp_cced_tesh, 1)
        self.assertLess(cmp_cced_esh, 1)
        self.assertLess(cmp_esh_tesh, 1)

        # ʃ and t͡ʃ should be more similar than either of these and ç
        self.assertGreater(cmp_esh_tesh, cmp_cced_tesh)
        self.assertGreater(cmp_esh_tesh, cmp_cced_esh)


if __name__ == '__main__':
    unittest.main()
