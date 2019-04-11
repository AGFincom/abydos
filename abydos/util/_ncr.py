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

"""abydos.util._ncr.

The util._ncr module defines _ncr, which computes n Choose r.
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from math import factorial

__all__ = []


def _ncr(n, r):
    r"""Return n Choose r.

    Cf. https://en.wikipedia.org/wiki/Combination

    Parameters
    ----------
    n : numeric
        The number of elements in the set/multiset
    r : numeric
        The number of elements to choose

    Returns
    -------
    float
        n Choose r

    Examples
    --------
    >>> _ncr(4, 2)
    6.0
    >>> _ncr(10, 3)
    120.0

    .. versionadded:: 0.4.0

    """
    if not r:
        return 1.0
    if r > n:
        return 0.0
    return factorial(n) / (factorial(r) * factorial(n - r))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
