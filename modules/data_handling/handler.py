import os
from typing import Dict, List, Any

import pandas as pd


class DataHandler:

    def __init__(self, columns: List[str]) -> None:
        self.output_path = "./output"
        directory = os.path.dirname(self.output_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.storage = {col: [] for col in columns}

    def update_storage(self, values: List[Dict]):

        for row_dict in values:
            row_dict['published'] = row_dict['published']
            for key, value in row_dict.items():
                self.storage[key].append(value)

    def export_to_excel(self, file_name: str) -> None:
        df = pd.DataFrame(data=self.storage)
        df = df.drop_duplicates()
        df.to_excel(excel_writer=file_name, sheet_name="articles")

