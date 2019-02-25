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

"""abydos.tests.distance.test_distance_pattern.

This module contains unit tests for abydos.distance.Pattern
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

from abydos.distance import Pattern


class PatternTestCases(unittest.TestCase):
    """Test Pattern functions.

    abydos.distance.Pattern
    """

    cmp = Pattern()
    cmp_no_d = Pattern(alphabet=0)

    def test_pattern_sim(self):
        """Test abydos.distance.Pattern.sim."""
        # Base cases
        self.assertEqual(self.cmp.sim('', ''), 0.0)
        self.assertEqual(self.cmp.sim('a', ''), 0.0)
        self.assertEqual(self.cmp.sim('', 'a'), 0.0)
        self.assertEqual(self.cmp.sim('abc', ''), 0.0)
        self.assertEqual(self.cmp.sim('', 'abc'), 0.0)
        self.assertEqual(self.cmp.sim('abc', 'abc'), 0.0)
        self.assertEqual(self.cmp.sim('abcd', 'efgh'), 0.0001626926280716368)

        self.assertAlmostEqual(self.cmp.sim('Nigel', 'Niall'), 5.85693e-05)
        self.assertAlmostEqual(self.cmp.sim('Niall', 'Nigel'), 5.85693e-05)
        self.assertAlmostEqual(self.cmp.sim('Colin', 'Coiln'), 5.85693e-05)
        self.assertAlmostEqual(self.cmp.sim('Coiln', 'Colin'), 5.85693e-05)
        self.assertAlmostEqual(
            self.cmp.sim('ATCAACGAGT', 'AACGATTAG'), 7.80925e-05
        )

    def test_pattern_dist(self):
        """Test abydos.distance.Pattern.dist."""
        # Base cases
        self.assertEqual(self.cmp.dist('', ''), 1.0)
        self.assertEqual(self.cmp.dist('a', ''), 1.0)
        self.assertEqual(self.cmp.dist('', 'a'), 1.0)
        self.assertEqual(self.cmp.dist('abc', ''), 1.0)
        self.assertEqual(self.cmp.dist('', 'abc'), 1.0)
        self.assertEqual(self.cmp.dist('abc', 'abc'), 1.0)
        self.assertEqual(self.cmp.dist('abcd', 'efgh'), 0.9998373073719283)

        self.assertAlmostEqual(self.cmp.dist('Nigel', 'Niall'), 0.9999414307)
        self.assertAlmostEqual(self.cmp.dist('Niall', 'Nigel'), 0.9999414307)
        self.assertAlmostEqual(self.cmp.dist('Colin', 'Coiln'), 0.9999414307)
        self.assertAlmostEqual(self.cmp.dist('Coiln', 'Colin'), 0.9999414307)
        self.assertAlmostEqual(
            self.cmp.dist('ATCAACGAGT', 'AACGATTAG'), 0.9999219075
        )


if __name__ == '__main__':
    unittest.main()
