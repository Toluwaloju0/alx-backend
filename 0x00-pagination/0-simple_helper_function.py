#!/usr/bin/env python3
"""A module to paginate a file"""

import csv
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """A function to paginate a page"""

    end_page = page_size * page
    return end_page - page_size, end_page
