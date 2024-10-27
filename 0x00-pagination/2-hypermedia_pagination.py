#!/usr/bin/env python3
"""A module to paginate a file"""

import csv
import math
from typing import Tuple, List, Dict, Union, Sized


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """A function to paginate a page"""

    end_page: int = page_size * page
    return end_page - page_size, end_page


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
        """A function to get a data page"""

        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        page_range = index_range(page, page_size)
        data = self.dataset()

        if len(data) < page_range[0]:
            return []
        elif len(data) < page_range[1]:
            return data[page_range[0]:]
        else:
            return data[page_range[0]: page_range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """A function to get the hyper contents of a dataset"""

        hyper_dict: Dict[str, Union[int, List, Sized, None]] = {
            'page_size': 0, 'page': page, 'data': None,
            'next_page': None, 'prev_page': None, 'total_pages': None
        }
        data: List = self.dataset()

        hyper_dict['data'] = self.get_page(page, page_size)
        hyper_dict['total_pages'] = int(len(data) / page_size)
        hyper_dict['page_size'] = len(hyper_dict['data'])
        if hyper_dict['total_pages'] > page:
            hyper_dict['next_page'] = page + 1
        if page > 1:
            hyper_dict['prev_page'] = page - 1

        return hyper_dict
