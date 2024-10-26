#!/usr/bin/env python3
"""A module to paginate a file"""

import csv
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """A function to paginate a page"""

    count: int = 0

    with open("Popular_Baby_Names.csv", 'r') as csv_file:
        end_page = page_size * page
        csv_list = list(csv.DictReader(csv_file))
        return end_page - page_size, end_page
            