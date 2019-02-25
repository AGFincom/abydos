# -*- coding: utf-8 -*-

# Copyright 2019 by Christopher C. Little.
# This file is part of Abydos.
#
# Abydos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Abydos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Abydos. If not, see <http://www.gnu.org/licenses/>.

"""abydos.tests.distance.test_distance_kendall_tau.

This module contains unit tests for abydos.distance.KendallTau
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

from abydos.distance import KendallTau


class KendallTauTestCases(unittest.TestCase):
    """Test KendallTau functions.

    abydos.distance.KendallTau
    """

    cmp = KendallTau()
    cmp_no_d = KendallTau(alphabet=0)

    def test_kendall_tau_sim(self):
        """Test abydos.distance.KendallTau.sim."""
        # Base cases
        self.assertEqual(self.cmp.sim('', ''), 0.002554278416347382)
        self.assertEqual(self.cmp.sim('a', ''), 0.0025412463836109156)
        self.assertEqual(self.cmp.sim('', 'a'), 0.0025412463836109156)
        self.assertEqual(self.cmp.sim('abc', ''), 0.0025282143508744493)
        self.assertEqual(self.cmp.sim('', 'abc'), 0.0025282143508744493)
        self.assertEqual(self.cmp.sim('abc', 'abc'), 0.002554278416347382)
        self.assertEqual(self.cmp.sim('abcd', 'efgh'), 0.0024891182526650506)

        self.assertAlmostEqual(self.cmp.sim('Nigel', 'Niall'), 0.0025151823)
        self.assertAlmostEqual(self.cmp.sim('Niall', 'Nigel'), 0.0025151823)
        self.assertAlmostEqual(self.cmp.sim('Colin', 'Coiln'), 0.0025151823)
        self.assertAlmostEqual(self.cmp.sim('Coiln', 'Colin'), 0.0025151823)
        self.assertAlmostEqual(
            self.cmp.sim('ATCAACGAGT', 'AACGATTAG'), 0.0025086663
        )

        # Tests with alphabet=0 (no d factor)
        self.assertEqual(self.cmp_no_d.sim('', ''), float('nan'))
        self.assertEqual(self.cmp_no_d.sim('a', ''), -2.0)
        self.assertEqual(self.cmp_no_d.sim('', 'a'), -2.0)
        self.assertEqual(self.cmp_no_d.sim('abc', ''), -0.6666666666666666)
        self.assertEqual(self.cmp_no_d.sim('', 'abc'), -0.6666666666666666)
        self.assertEqual(self.cmp_no_d.sim('abc', 'abc'), 0.6666666666666666)
        self.assertEqual(
            self.cmp_no_d.sim('abcd', 'efgh'), -0.2222222222222222
        )

        self.assertAlmostEqual(
            self.cmp_no_d.sim('Nigel', 'Niall'), -0.0833333333
        )
        self.assertAlmostEqual(
            self.cmp_no_d.sim('Niall', 'Nigel'), -0.0833333333
        )
        self.assertAlmostEqual(
            self.cmp_no_d.sim('Colin', 'Coiln'), -0.0833333333
        )
        self.assertAlmostEqual(
            self.cmp_no_d.sim('Coiln', 'Colin'), -0.0833333333
        )
        self.assertAlmostEqual(
            self.cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG'), 0.0
        )

    def test_kendall_tau_dist(self):
        """Test abydos.distance.KendallTau.dist."""
        # Base cases
        self.assertEqual(self.cmp.dist('', ''), 0.9974457215836526)
        self.assertEqual(self.cmp.dist('a', ''), 0.9974587536163891)
        self.assertEqual(self.cmp.dist('', 'a'), 0.9974587536163891)
        self.assertEqual(self.cmp.dist('abc', ''), 0.9974717856491255)
        self.assertEqual(self.cmp.dist('', 'abc'), 0.9974717856491255)
        self.assertEqual(self.cmp.dist('abc', 'abc'), 0.9974457215836526)
        self.assertEqual(self.cmp.dist('abcd', 'efgh'), 0.9975108817473349)

        self.assertAlmostEqual(self.cmp.dist('Nigel', 'Niall'), 0.9974848177)
        self.assertAlmostEqual(self.cmp.dist('Niall', 'Nigel'), 0.9974848177)
        self.assertAlmostEqual(self.cmp.dist('Colin', 'Coiln'), 0.9974848177)
        self.assertAlmostEqual(self.cmp.dist('Coiln', 'Colin'), 0.9974848177)
        self.assertAlmostEqual(
            self.cmp.dist('ATCAACGAGT', 'AACGATTAG'), 0.9974913337
        )

        # Tests with alphabet=0 (no d factor)
        self.assertEqual(self.cmp_no_d.dist('', ''), float('nan'))
        self.assertEqual(self.cmp_no_d.dist('a', ''), 3.0)
        self.assertEqual(self.cmp_no_d.dist('', 'a'), 3.0)
        self.assertEqual(self.cmp_no_d.dist('abc', ''), 1.6666666666666665)
        self.assertEqual(self.cmp_no_d.dist('', 'abc'), 1.6666666666666665)
        self.assertEqual(self.cmp_no_d.dist('abc', 'abc'), 0.33333333333333337)
        self.assertEqual(
            self.cmp_no_d.dist('abcd', 'efgh'), 1.2222222222222223
        )

        self.assertAlmostEqual(
            self.cmp_no_d.dist('Nigel', 'Niall'), 1.0833333333
        )
        self.assertAlmostEqual(
            self.cmp_no_d.dist('Niall', 'Nigel'), 1.0833333333
        )
        self.assertAlmostEqual(
            self.cmp_no_d.dist('Colin', 'Coiln'), 1.0833333333
        )
        self.assertAlmostEqual(
            self.cmp_no_d.dist('Coiln', 'Colin'), 1.0833333333
        )
        self.assertAlmostEqual(
            self.cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG'), 1.0
        )


if __name__ == '__main__':
    unittest.main()
