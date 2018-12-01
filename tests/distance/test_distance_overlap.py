# -*- coding: utf-8 -*-

# Copyright 2014-2018 by Christopher C. Little.
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

"""abydos.tests.distance.test_distance_overlap.

This module contains unit tests for abydos.distance.Overlap
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import unittest

from abydos.distance import Overlap, dist_overlap, sim_overlap
from abydos.tokenizer import QGrams

from .. import NONQ_FROM, NONQ_TO


class OverlapTestCases(unittest.TestCase):
    """Test overlap functions.

    abydos.distance.Overlap
    """

    cmp = Overlap()
    cmp_q2 = Overlap(tokenizer=QGrams(2))

    def test_overlap_sim(self):
        """Test abydos.distance.Overlap.sim."""
        self.assertEqual(self.cmp.sim('', ''), 1)
        self.assertEqual(self.cmp.sim('nelson', ''), 0)
        self.assertEqual(self.cmp.sim('', 'neilsen'), 0)
        self.assertAlmostEqual(self.cmp.sim('nelson', 'neilsen'), 4 / 7)

        self.assertEqual(self.cmp_q2.sim('', ''), 1)
        self.assertEqual(self.cmp_q2.sim('nelson', ''), 0)
        self.assertEqual(self.cmp_q2.sim('', 'neilsen'), 0)
        self.assertAlmostEqual(self.cmp_q2.sim('nelson', 'neilsen'), 4 / 7)

        # supplied q-gram tests
        self.assertEqual(
            self.cmp.sim(
                QGrams().tokenize('').get_counter(),
                QGrams().tokenize('').get_counter(),
            ),
            1,
        )
        self.assertEqual(
            self.cmp.sim(
                QGrams().tokenize('nelson').get_counter(),
                QGrams().tokenize('').get_counter(),
            ),
            0,
        )
        self.assertEqual(
            self.cmp.sim(
                QGrams().tokenize('').get_counter(),
                QGrams().tokenize('neilsen').get_counter(),
            ),
            0,
        )
        self.assertAlmostEqual(
            self.cmp.sim(
                QGrams().tokenize('nelson').get_counter(),
                QGrams().tokenize('neilsen').get_counter(),
            ),
            4 / 7,
        )

        # # non-q-gram tests
        # self.assertEqual(self.cmp.sim('', '', 0), 1)
        # self.assertEqual(self.cmp.sim('the quick', '', 0), 0)
        # self.assertEqual(self.cmp.sim('', 'the quick', 0), 0)
        # self.assertAlmostEqual(self.cmp.sim(NONQ_FROM, NONQ_TO, 0), 4 / 7)
        # self.assertAlmostEqual(self.cmp.sim(NONQ_TO, NONQ_FROM, 0), 4 / 7)

        # Test wrapper
        self.assertAlmostEqual(sim_overlap('nelson', 'neilsen'), 4 / 7)

    def test_overlap_dist(self):
        """Test abydos.distance.Overlap.dist."""
        self.assertEqual(self.cmp.dist('', ''), 0)
        self.assertEqual(self.cmp.dist('nelson', ''), 1)
        self.assertEqual(self.cmp.dist('', 'neilsen'), 1)
        self.assertAlmostEqual(self.cmp.dist('nelson', 'neilsen'), 3 / 7)

        self.assertEqual(self.cmp_q2.dist('', ''), 0)
        self.assertEqual(self.cmp_q2.dist('nelson', ''), 1)
        self.assertEqual(self.cmp_q2.dist('', 'neilsen'), 1)
        self.assertAlmostEqual(self.cmp_q2.dist('nelson', 'neilsen'), 3 / 7)

        # supplied q-gram tests
        self.assertEqual(
            self.cmp.dist(
                QGrams().tokenize('').get_counter(),
                QGrams().tokenize('').get_counter(),
            ),
            0,
        )
        self.assertEqual(
            self.cmp.dist(
                QGrams().tokenize('nelson').get_counter(),
                QGrams().tokenize('').get_counter(),
            ),
            1,
        )
        self.assertEqual(
            self.cmp.dist(
                QGrams().tokenize('').get_counter(),
                QGrams().tokenize('neilsen').get_counter(),
            ),
            1,
        )
        self.assertAlmostEqual(
            self.cmp.dist(
                QGrams().tokenize('nelson').get_counter(),
                QGrams().tokenize('neilsen').get_counter(),
            ),
            3 / 7,
        )

        # # non-q-gram tests
        # self.assertEqual(self.cmp.dist('', '', 0), 0)
        # self.assertEqual(self.cmp.dist('the quick', '', 0), 1)
        # self.assertEqual(self.cmp.dist('', 'the quick', 0), 1)
        # self.assertAlmostEqual(self.cmp.dist(NONQ_FROM, NONQ_TO, 0), 3 / 7)
        # self.assertAlmostEqual(self.cmp.dist(NONQ_TO, NONQ_FROM, 0), 3 / 7)

        # Test wrapper
        self.assertAlmostEqual(dist_overlap('nelson', 'neilsen'), 3 / 7)


if __name__ == '__main__':
    unittest.main()
