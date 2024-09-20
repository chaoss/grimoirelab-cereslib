# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2019 Bitergia
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#     Alberto Pérez García-Plaza <alpgarcia@bitergia.com>
#

import sys
import unittest

import pandas

if '..' not in sys.path:
    sys.path.insert(0, '..')

from cereslib.dfutils.filter import FilterRows


class TestFilter(unittest.TestCase):
    """ Unit tests for Filter class
    """

    def test_filter_rows(self):
        """ Test several cases for filtering rows by column value
        """

        # One column, values of different types
        df = pandas.DataFrame()
        filepaths = ['', None, '-', '/file/path', 1, True, pandas.NA, '-', [1, 2]]
        df["filepath"] = filepaths
        data_filtered = FilterRows(df)
        df = data_filtered.filter_(["filepath"], "-")

        self.assertEqual(len(df), 7)

        # One empty column
        df = pandas.DataFrame()
        df["filepath"] = []
        data_filtered = FilterRows(df)
        df = data_filtered.filter_(["filepath"], "-")

        self.assertEqual(len(df), 0)

        # Several columns and just one empty
        df = pandas.DataFrame()
        df["filepath"] = []
        df["name"] = ["name", "-", "other", "-"]
        df["dirname"] = ["dir", "-", "-", "-"]
        data_filtered = FilterRows(df)
        df = data_filtered.filter_(["filepath", "name", "dirname"], "-")

        self.assertEqual(len(df), 1)

    def test_column_not_exists(self):
        """ Test empty dataframe looking for the corresponding ValueError exception
        """
        df = pandas.DataFrame()
        data_filtered = FilterRows(df)
        with self.assertRaisesRegex(ValueError, "Column filepath not in DataFrame columns: \[\]") as context:
            data_filtered.filter_(["filepath"], "-")


if __name__ == '__main__':
    unittest.main()
