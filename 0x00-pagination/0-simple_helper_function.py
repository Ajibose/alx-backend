#!/usr/bin/env python3
"""Write a funtion that calculate the starting and end index for pagination"""
from typing import Sequence


def index_range(page: int, page_size: int) -> Sequence:
    """Pagination index generator"""
    start_index = (page - 1) * page_size
    end_index = page_size * page
    return (start_index, end_index)
