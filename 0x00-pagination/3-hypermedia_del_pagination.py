#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """A function to get a delete resilent hyper page"""

        hyper_dict: Dict[str, Union[List, int, None]] = {
            'index': index, 'page_size': None,
            'next_index': None, 'data': None
        }
        data_list: List = []
        data_set = self.indexed_dataset()
        # assert index is less than dataset range
        assert index < len(list(data_set))
        # iterate over the dataset from index position using page_size as range
        for _ in range(page_size):
            index_data = data_set.get(index)
            if index_data:
                data_list.append(index_data)
            index += 1
        # using the current data_list fill hyper_dict
        hyper_dict['page_size'] = len(data_list)
        hyper_dict['data'] = data_list
        hyper_dict['next_index'] = index

        return hyper_dict
