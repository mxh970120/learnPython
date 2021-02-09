# -*- coding: utf-8 -*-

import os
from plyfile import PlyData
import pandas as pd
import numpy as np
from collections import OrderedDict
import colorsys
import open3d


path = 'data2'
file_name_dict = getFolderFileName(path)
print(file_name_dict)

writer = pd.ExcelWriter(path + '.xlsx', engine='openpyxl')
plyDataFrame = []
for foldername, filenames in file_name_dict.items():
    for i, filename in enumerate(filenames):
        """
        CODE
        """

        df = pd.DataFrame( .... )
        plyDataFrame.append(df)

result = pd.concat(plyDataFrame, ignore_index=True)
result.index = range(1, len(result) + 1)
print(result)
result.to_excel(writer, path)

workbook = writer.book
worksheets = writer.sheets
worksheet = worksheets[path]
for col in worksheet.columns:
    max_length = 0
    # Since Openpyxl 2.6, the column name is  ".column_letter" as .column became the column number (1-based)
    column = col[0].column_letter  # Get the column name
    print(column)
    for cell in col:
        try:  # Necessary to avoid error on empty cells
            if len(str(cell.value)) > max_length:
                max_length = len(cell.value)
        except:
            pass
    adjusted_width = (max_length + 2) * 1.2
    worksheet.column_dimensions[column].width = adjusted_width

writer.save()