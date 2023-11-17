import pandas as pd
import openpyxl

import settings


def read_channels():
    df = pd.read_excel(settings.EXCEL_FILE_NAME)
    first_column_array = df.iloc[:, 0].values
    return first_column_array


# ONLY FOR DEV RUN
def write_channels_hardcode(*args):
    df = pd.DataFrame(args, columns=["chat_link"])
    df.to_excel(settings.EXCEL_FILE_NAME, index=False)
