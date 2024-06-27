#!/usr/bin/env python3
"""Write a funtion that calculate the starting and end index for pagination"""
import csv
import math
from typing import List
from typing import Sequence


def index_range(page: int, page_size: int) -> Sequence:
    """Pagination index generator"""
    start_index = (page - 1) * page_size
    end_index = page_size * page
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert(type(page) == int)
        assert(type(page_size) == int)
        assert(page > 0)
        assert(page_size > 0)

        self.dataset()
        start, end = index_range(page, page_size)
        if start < 0 or end > len(self.__dataset):
            return []

        return self.__dataset[start:end]
