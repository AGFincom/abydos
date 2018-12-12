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

"""abydos.distance._lcprefix.

Longest common prefix
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from os.path import commonprefix

from ._distance import _Distance

__all__ = ['LCPrefix']


class LCPrefix(_Distance):
    """Longest common prefix.

    .. versionadded:: 0.4.0
    """

    def lcprefix(self, strings):
        """Return the longest common prefix of a list of strings.

        Longest common prefix (LCPrefix).

        Parameters
        ----------
        strings : list of strings
            Strings for comparison

        Returns
        -------
        str
            The longest common prefix

        Examples
        --------
        >>> pfx = LCPrefix()
        >>> pfx.lcprefix('cat', 'hat')
        'at'
        >>> pfx.lcprefix('Niall', 'Neil')
        'N'
        >>> pfx.lcprefix('aluminum', 'Catalan')
        'al'
        >>> pfx.lcprefix('ATCG', 'TAGC')
        'A'

        .. versionadded:: 0.4.0

        """
        return commonprefix(strings)

    def dist_abs(self, src, tar, *args):
        """Return the length of the longest common prefix of the strings.

        Parameters
        ----------
        src : str
            Source string for comparison
        tar : str
            Target string for comparison
        *args : strs
            Additional strings for comparison

        Raises
        ------
        ValueError
            All arguments must be of type str

        Returns
        -------
        int
            The length of the longest common prefix

        Examples
        --------
        >>> pfx = LCPrefix()
        >>> pfx.dist_abs('cat', 'hat')
        0
        >>> pfx.dist_abs('Niall', 'Neil')
        1
        >>> pfx.dist_abs('aluminum', 'Catalan')
        0
        >>> pfx.dist_abs('ATCG', 'TAGC')
        0

        .. versionadded:: 0.4.0

        """
        strings = [src, tar]
        for arg in args:
            if isinstance(arg, str):
                strings.append(arg)
            else:
                raise ValueError('All arguments must be of type str')

        return len(self.lcprefix(strings))

    def sim(self, src, tar, *args):
        r"""Return the longest common prefix similarity of two or more strings.

        Longest common prefix similarity (:math:`sim_{LCPrefix}`).

        This employs the LCPrefix function to derive a similarity metric:
        :math:`sim_{LCPrefix}(s,t) = \frac{|LCPrefix(s,t)|}{max(|s|, |t|)}`

        Parameters
        ----------
        src : str
            Source string for comparison
        tar : str
            Target string for comparison
        *args : strs
            Additional strings for comparison

        Returns
        -------
        float
            LCPrefix similarity

        Examples
        --------
        >>> pfx = LCPrefix()
        >>> pfx.sim('cat', 'hat')
        0.6666666666666666
        >>> pfx.sim('Niall', 'Neil')
        0.2
        >>> pfx.sim('aluminum', 'Catalan')
        0.25
        >>> pfx.sim('ATCG', 'TAGC')
        0.25

        """
        dist = self.dist_abs(src, tar, *args)
        maxlen = max(len(src), len(tar), *[len(arg) for arg in args])
        return dist/maxlen

    def dist(self, src, tar, *args):
        r"""Return the longest common prefix distance of two or more strings.

        Parameters
        ----------
        src : str
            Source string for comparison
        tar : str
            Target string for comparison
        *args : strs
            Additional strings for comparison

        Returns
        -------
        float
            LCPrefix distance

        Examples
        --------
        >>> pfx = LCPrefix()
        >>> pfx.dist('cat', 'hat')
        0.6666666666666666
        >>> pfx.dist('Niall', 'Neil')
        0.2
        >>> pfx.dist('aluminum', 'Catalan')
        0.25
        >>> pfx.dist('ATCG', 'TAGC')
        0.25

        """
        return 1.0 - self.sim(src, tar, *args)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
