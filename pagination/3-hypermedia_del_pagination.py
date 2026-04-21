#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any, Optional


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server instance."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return dataset indexed by position."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None, page_size: int = 10) -> Dict[str, Any]:
        """
        Return a deletion-resilient pagination dictionary.

        The method ensures that missing indices do not affect pagination.
        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed_dataset = self.indexed_dataset()
        assert index < len(indexed_dataset)

        data = []
        current_index = index

        while len(data) < page_size and current_index < len(indexed_dataset):
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
            current_index += 1

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': current_index
        }
