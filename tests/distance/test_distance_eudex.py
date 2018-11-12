# -*- coding: utf-8 -*-

# Copyright 2018 by Christopher C. Little.
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

"""abydos.tests.distance.test_distance_eudex.

This module contains unit tests for abydos.distance.Eudex
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

from abydos.distance import Eudex, dist_eudex, eudex_hamming, sim_eudex


def _yield_1():
    while True:
        yield 1


class EudexTestCases(unittest.TestCase):
    """Test Eudex distance functions.

    abydos.distance.Eudex
    """
    cmp = Eudex()

    def test_eudex_dist_abs(self):
        """Test abydos.distance.Eudex.dist_abs."""

        # Base cases
        self.assertEqual(self.cmp.dist_abs('', ''), 0)
        self.assertEqual(self.cmp.dist_abs('', '', None), 0)
        self.assertEqual(self.cmp.dist_abs('', '', 'fibonacci'), 0)
        self.assertEqual(self.cmp.dist_abs('', '', [10, 1, 1, 1]), 0)
        self.assertEqual(self.cmp.dist_abs('', '', _yield_1), 0)
        self.assertEqual(self.cmp.dist_abs('', '', normalized=True), 0)

        self.assertEqual(self.cmp.dist_abs('Niall', 'Niall'), 0)
        self.assertEqual(self.cmp.dist_abs('Niall', 'Niall', None), 0)
        self.assertEqual(self.cmp.dist_abs('Niall', 'Niall', 'fibonacci'), 0)
        self.assertEqual(self.cmp.dist_abs('Niall', 'Niall', [10, 1, 1, 1]), 0)
        self.assertEqual(self.cmp.dist_abs('Niall', 'Niall', _yield_1), 0)
        self.assertEqual(self.cmp.dist_abs('Niall', 'Niall', normalized=True), 0)

        self.assertEqual(self.cmp.dist_abs('Niall', 'Neil'), 2)
        self.assertEqual(self.cmp.dist_abs('Niall', 'Neil', None), 1)
        self.assertEqual(self.cmp.dist_abs('Niall', 'Neil', 'fibonacci'), 2)
        self.assertEqual(self.cmp.dist_abs('Niall', 'Neil', [10, 1, 1, 1]), 1)
        self.assertEqual(self.cmp.dist_abs('Niall', 'Neil', _yield_1), 1)
        self.assertAlmostEqual(
            self.cmp.dist_abs('Niall', 'Neil', normalized=True), 0.00098039
        )

        self.assertEqual(self.cmp.dist_abs('Niall', 'Colin'), 524)
        self.assertEqual(self.cmp.dist_abs('Niall', 'Colin', None), 10)
        self.assertEqual(self.cmp.dist_abs('Niall', 'Colin', 'fibonacci'), 146)
        self.assertEqual(self.cmp.dist_abs('Niall', 'Colin', [10, 1, 1, 1]), 6)
        self.assertEqual(self.cmp.dist_abs('Niall', 'Colin', _yield_1), 10)
        self.assertAlmostEqual(
            self.cmp.dist_abs('Niall', 'Colin', normalized=True), 0.25686274
        )

        # Test wrapper
        self.assertEqual(eudex_hamming('Niall', 'Neil', 'fibonacci'), 2)

    def test_eudex_dist(self):
        """Test abydos.distance.Eudex.dist."""
        # Base cases
        self.assertEqual(self.cmp.dist('', ''), 0)
        self.assertEqual(self.cmp.dist('', '', None), 0)
        self.assertEqual(self.cmp.dist('', '', 'fibonacci'), 0)

        self.assertEqual(self.cmp.dist('Niall', 'Niall'), 0)
        self.assertEqual(self.cmp.dist('Niall', 'Niall', None), 0)
        self.assertEqual(self.cmp.dist('Niall', 'Niall', 'fibonacci'), 0)

        self.assertAlmostEqual(self.cmp.dist('Niall', 'Neil'), 0.00098039)
        self.assertAlmostEqual(self.cmp.dist('Niall', 'Neil', None), 0.11111111)
        self.assertAlmostEqual(
            self.cmp.dist('Niall', 'Neil', 'fibonacci'), 0.00287356
        )

        self.assertAlmostEqual(self.cmp.dist('Niall', 'Colin'), 0.25686275)
        self.assertAlmostEqual(self.cmp.dist('Niall', 'Colin', None), 0.16666667)
        self.assertAlmostEqual(
            self.cmp.dist('Niall', 'Colin', 'fibonacci'), 0.20977011
        )

        # Test wrapper
        self.assertAlmostEqual(
            dist_eudex('Niall', 'Neil', 'fibonacci'), 0.00287356
        )

    def test_eudex_sim(self):
        """Test abydos.distance.Eudex.sim."""
        # Base cases
        self.assertEqual(self.cmp.sim('', ''), 1)
        self.assertEqual(self.cmp.sim('', '', None), 1)
        self.assertEqual(self.cmp.sim('', '', 'fibonacci'), 1)

        self.assertEqual(self.cmp.sim('Niall', 'Niall'), 1)
        self.assertEqual(self.cmp.sim('Niall', 'Niall', None), 1)
        self.assertEqual(self.cmp.sim('Niall', 'Niall', 'fibonacci'), 1)

        self.assertAlmostEqual(self.cmp.sim('Niall', 'Neil'), 0.99901961)
        self.assertAlmostEqual(self.cmp.sim('Niall', 'Neil', None), 0.88888889)
        self.assertAlmostEqual(
            self.cmp.sim('Niall', 'Neil', 'fibonacci'), 0.99712644
        )

        self.assertAlmostEqual(self.cmp.sim('Niall', 'Colin'), 0.74313725)
        self.assertAlmostEqual(self.cmp.sim('Niall', 'Colin', None), 0.83333333)
        self.assertAlmostEqual(
            self.cmp.sim('Niall', 'Colin', 'fibonacci'), 0.79022989
        )

        # Test wrapper
        self.assertAlmostEqual(
            sim_eudex('Niall', 'Neil', 'fibonacci'), 0.99712644
        )


if __name__ == '__main__':
    unittest.main()
