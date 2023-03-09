import pandas as pd

import csv
from io import StringIO
from typing import BinaryIO, TypeVar


PandasDataFrame = TypeVar('pandas.core.frame.DataFrame')


class FilesService:
    @staticmethod
    def upload(file: BinaryIO) -> PandasDataFrame:
        reader = csv.DictReader((line.decode() for line in file))
        ds = []
        for row in reader:
            ds.append(row)
        return pd.DataFrame(ds)


    @staticmethod
    def download(data: PandasDataFrame):
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=list(data))
        writer.writeheader()
        for i in range(len(data)):
            writer.writerow(dict(data.iloc[i]))
        output.seek(0)
        return output
