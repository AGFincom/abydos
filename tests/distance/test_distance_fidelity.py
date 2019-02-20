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

"""abydos.tests.distance.test_distance_fidelity.

This module contains unit tests for abydos.distance.Fidelity
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

from abydos.distance import Fidelity


class FidelityTestCases(unittest.TestCase):
    """Test Fidelity functions.

    abydos.distance.Fidelity
    """

    cmp = Fidelity()

    def test_fidelity_sim(self):
        """Test abydos.distance.Fidelity.sim."""
        # Base cases
        self.assertEqual(self.cmp.sim('', ''), 0)
        self.assertEqual(self.cmp.sim('a', ''), 0.0)
        self.assertEqual(self.cmp.sim('', 'a'), 0.0)
        self.assertEqual(self.cmp.sim('abc', ''), 0.0)
        self.assertEqual(self.cmp.sim('', 'abc'), 0.0)
        self.assertEqual(self.cmp.sim('abc', 'abc'), 4.0)
        self.assertEqual(self.cmp.sim('abcd', 'efgh'), 0.0)

        self.assertAlmostEqual(self.cmp.sim('Nigel', 'Niall'), 3.0)
        self.assertAlmostEqual(self.cmp.sim('Niall', 'Nigel'), 3.0)
        self.assertAlmostEqual(self.cmp.sim('Colin', 'Coiln'), 3.0)
        self.assertAlmostEqual(self.cmp.sim('Coiln', 'Colin'), 3.0)
        self.assertAlmostEqual(self.cmp.sim('ATCAACGAGT', 'AACGATTAG'), 7.0)

    def test_fidelity_dist(self):
        """Test abydos.distance.Fidelity.dist."""
        # Base cases
        self.assertEqual(self.cmp.dist('', ''), 1.0)
        self.assertEqual(self.cmp.dist('a', ''), 1.0)
        self.assertEqual(self.cmp.dist('', 'a'), 1.0)
        self.assertEqual(self.cmp.dist('abc', ''), 1.0)
        self.assertEqual(self.cmp.dist('', 'abc'), 1.0)
        self.assertEqual(self.cmp.dist('abc', 'abc'), -3.0)
        self.assertEqual(self.cmp.dist('abcd', 'efgh'), 1.0)

        self.assertAlmostEqual(self.cmp.dist('Nigel', 'Niall'), -2.0)
        self.assertAlmostEqual(self.cmp.dist('Niall', 'Nigel'), -2.0)
        self.assertAlmostEqual(self.cmp.dist('Colin', 'Coiln'), -2.0)
        self.assertAlmostEqual(self.cmp.dist('Coiln', 'Colin'), -2.0)
        self.assertAlmostEqual(self.cmp.dist('ATCAACGAGT', 'AACGATTAG'), -6.0)


if __name__ == '__main__':
    unittest.main()
