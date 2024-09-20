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
#   Daniel Izquierdo Cortazar <dizquierdo@bitergia.com>
#


import pandas

import numpy as np


class Format(object):
    """ Library that allows to format dataframes to be later enriched

    This class is the first step in the enrichment process of data.
    Although this can be used alone for other purposes, its main
    goal consists of providing well formated [missing fields,
    string dates, removal of not needed fields] for the following
    steps of the enrichment process.

    This data format and cleaning process is done due to
    inconsistencies and missing fields that may appear when reading
    information.
    """

    def fill_missing_fields(self, data, columns):
        """ This  method fills with 0's missing fields

        :param data: original Pandas dataframe
        :param columns: list of columns to be filled in the DataFrame
        :type data: pandas.DataFrame
        :type columns: list of strings

        :returns: Pandas dataframe with missing fields filled with 0's
        :rtype: pandas.DataFrame
        """

        for column in columns:
            if column not in data.columns:
                data[column] = np.zeros(len(data))

        return data

    def update_field_names(self, data, matching):
        """ This method updates the names of the fields according to matching

        :param data: original Pandas dataframe
        :param matching: dictionary of matchings between old and new values
        :type data: pandas.DataFrame
        :type matching: dictionary

        :returns: Pandas dataframe with updated names
        :rtype: pandas.DataFrame
        """

        for key in matching.keys():
            if key in data.columns:
                data.rename(columns={key: matching[key]})

        return data

    def format_dates(self, data, columns):
        """ This method translates columns values into datetime objects

        :param data: original Pandas dataframe
        :param columns: list of columns to cast the date to a datetime object
        :type data: pandas.DataFrame
        :type columns: list of strings

        :returns: Pandas dataframe with updated 'columns' with datetime objects
        :rtype: pandas.DataFrame
        """

        for column in columns:
            if column in data.columns:
                data[column] = pandas.to_datetime(data[column])

        return data

    def remove_columns(self, data, columns):
        """ This method removes columns in data

        :param data: original Pandas dataframe
        :param columns: list of columns to remove
        :type data: pandas.DataFrame
        :type columns: list of strings

        :returns: Pandas dataframe with removed columns
        :rtype: pandas.DataFrame
        """

        for column in columns:
            if column in data.columns:
                data = data.drop(column, axis=1)

        return data
