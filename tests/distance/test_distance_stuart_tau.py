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

"""abydos.tests.distance.test_distance_stuart_tau.

This module contains unit tests for abydos.distance.StuartTau
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

from abydos.distance import StuartTau


class StuartTauTestCases(unittest.TestCase):
    """Test StuartTau functions.

    abydos.distance.StuartTau
    """

    cmp = StuartTau()
    cmp_no_d = StuartTau(alphabet=0)

    def test_stuart_tau_sim(self):
        """Test abydos.distance.StuartTau.sim."""
        # Base cases
        self.assertEqual(self.cmp.sim('', ''), 0.00510204081632653)
        self.assertEqual(self.cmp.sim('a', ''), 0.005076009995835068)
        self.assertEqual(self.cmp.sim('', 'a'), 0.005076009995835068)
        self.assertEqual(self.cmp.sim('abc', ''), 0.005049979175343606)
        self.assertEqual(self.cmp.sim('', 'abc'), 0.005049979175343606)
        self.assertEqual(self.cmp.sim('abc', 'abc'), 0.00510204081632653)
        self.assertEqual(self.cmp.sim('abcd', 'efgh'), 0.0049718867138692216)

        self.assertAlmostEqual(self.cmp.sim('Nigel', 'Niall'), 0.0050239484)
        self.assertAlmostEqual(self.cmp.sim('Niall', 'Nigel'), 0.0050239484)
        self.assertAlmostEqual(self.cmp.sim('Colin', 'Coiln'), 0.0050239484)
        self.assertAlmostEqual(self.cmp.sim('Coiln', 'Colin'), 0.0050239484)
        self.assertAlmostEqual(
            self.cmp.sim('ATCAACGAGT', 'AACGATTAG'), 0.0050109329
        )

        # Tests with alphabet=0 (no d factor)
        self.assertEqual(self.cmp_no_d.sim('', ''), 4.0)
        self.assertEqual(self.cmp_no_d.sim('a', ''), -2.0)
        self.assertEqual(self.cmp_no_d.sim('', 'a'), -2.0)
        self.assertEqual(self.cmp_no_d.sim('abc', ''), -1.0)
        self.assertEqual(self.cmp_no_d.sim('', 'abc'), -1.0)
        self.assertEqual(self.cmp_no_d.sim('abc', 'abc'), 1.0)
        self.assertEqual(self.cmp_no_d.sim('abcd', 'efgh'), -0.4)

        self.assertAlmostEqual(
            self.cmp_no_d.sim('Nigel', 'Niall'), -0.1481481481
        )
        self.assertAlmostEqual(
            self.cmp_no_d.sim('Niall', 'Nigel'), -0.1481481481
        )
        self.assertAlmostEqual(
            self.cmp_no_d.sim('Colin', 'Coiln'), -0.1481481481
        )
        self.assertAlmostEqual(
            self.cmp_no_d.sim('Coiln', 'Colin'), -0.1481481481
        )
        self.assertAlmostEqual(
            self.cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG'), 0.0
        )

    def test_stuart_tau_dist(self):
        """Test abydos.distance.StuartTau.dist."""
        # Base cases
        self.assertEqual(self.cmp.dist('', ''), 0.9948979591836735)
        self.assertEqual(self.cmp.dist('a', ''), 0.994923990004165)
        self.assertEqual(self.cmp.dist('', 'a'), 0.994923990004165)
        self.assertEqual(self.cmp.dist('abc', ''), 0.9949500208246564)
        self.assertEqual(self.cmp.dist('', 'abc'), 0.9949500208246564)
        self.assertEqual(self.cmp.dist('abc', 'abc'), 0.9948979591836735)
        self.assertEqual(self.cmp.dist('abcd', 'efgh'), 0.9950281132861308)

        self.assertAlmostEqual(self.cmp.dist('Nigel', 'Niall'), 0.9949760516)
        self.assertAlmostEqual(self.cmp.dist('Niall', 'Nigel'), 0.9949760516)
        self.assertAlmostEqual(self.cmp.dist('Colin', 'Coiln'), 0.9949760516)
        self.assertAlmostEqual(self.cmp.dist('Coiln', 'Colin'), 0.9949760516)
        self.assertAlmostEqual(
            self.cmp.dist('ATCAACGAGT', 'AACGATTAG'), 0.9949890671
        )

        # Tests with alphabet=0 (no d factor)
        self.assertEqual(self.cmp_no_d.dist('', ''), -3.0)
        self.assertEqual(self.cmp_no_d.dist('a', ''), 3.0)
        self.assertEqual(self.cmp_no_d.dist('', 'a'), 3.0)
        self.assertEqual(self.cmp_no_d.dist('abc', ''), 2.0)
        self.assertEqual(self.cmp_no_d.dist('', 'abc'), 2.0)
        self.assertEqual(self.cmp_no_d.dist('abc', 'abc'), 0.0)
        self.assertEqual(self.cmp_no_d.dist('abcd', 'efgh'), 1.4)

        self.assertAlmostEqual(
            self.cmp_no_d.dist('Nigel', 'Niall'), 1.1481481481
        )
        self.assertAlmostEqual(
            self.cmp_no_d.dist('Niall', 'Nigel'), 1.1481481481
        )
        self.assertAlmostEqual(
            self.cmp_no_d.dist('Colin', 'Coiln'), 1.1481481481
        )
        self.assertAlmostEqual(
            self.cmp_no_d.dist('Coiln', 'Colin'), 1.1481481481
        )
        self.assertAlmostEqual(
            self.cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG'), 1.0
        )


if __name__ == '__main__':
    unittest.main()
