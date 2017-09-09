"""Files tests simple file read related operations"""
import os
import csv

class SimpleFile(object):
    """SimpleFile tests using file read api to do some simple math"""
    def __init__(self, file_path):
        self.numbers = []
        selfparse = csv.reader(os.path.abspath(file_path),delimiter='/')
        for row in self reader:
            self.append(row)
        return self
        """
        TODO: reads the file by path and parse content into two
        dimension array (numbers)
        """

    def get_mean(self, line_number):
        """
        get_mean retrieves the mean value of the list by line_number (starts
        with zero)
        """
        return sum(self[0:line_number])/(len(self[0:line_number]))

    def get_max(self, line_number):
        """
        get_max retrieves the maximum value of the list by line_number (starts
        with zero)
        """
        return max(self[0:line_number])

    def get_min(self, line_number):
        """
        get_min retrieves the minimum value of the list by line_number (starts
        with zero)
        """
        return min(self[0:line_number])

    def get_sum(self, line_number):
        """
        get_sum retrieves the sumation of the list by line_number (starts with
        zero)
        """
        return sum(self[0:line_number])
