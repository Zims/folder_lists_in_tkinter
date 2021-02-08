import os
from datetime import date
import pandas as pd


def folder_content(folder_name, folder_output_name):
    data_location = folder_name
    file_list = []
    for file in os.listdir(data_location):
        file_list.append(file)

    data = {'file_names': file_list}
    file_df = pd.DataFrame(data)

    new_file_dir = folder_output_name
    today = date.today()

    file_df.to_excel(new_file_dir + '/file_list-' + str(today) + '.xlsx')
    new_file_dir + '/book_list-' + str(today) + '.xlsx'
