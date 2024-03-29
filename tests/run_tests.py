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
#     Daniel Izquierdo <dizquierdo@bitergia.com>
#

import sys
import logging

import unittest


if __name__ == '__main__':
    test_suite = unittest.TestLoader().discover('.', pattern='test*.py')
    logging.warning("Test events ignored. Run them manually.")
    result = unittest.TextTestRunner(buffer=True).run(test_suite)
    sys.exit(not result.wasSuccessful())
