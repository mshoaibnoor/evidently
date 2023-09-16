#pandas 2.0.1 is required to run deepchecks successfully
from deepchecks.tabular.suites import data_integrity
from deepchecks.tabular import Dataset
import pandas as pd
import os
from datetime import datetime

def data_integrity_check():
    data_df = pd.read_csv('app/data/adult-education-dataset.csv')
    dataset = Dataset(data_df, label='class', cat_features=[])
    suite_result = data_integrity().run(dataset)
    dt = datetime.now()
    dt = str(dt)
    dt = dt.replace(' ','-')
    file_name = 'app/output/dataintegritycheck/data_validation-' + dt + '.html'
    print(file_name)
    suite_result.save_as_html(file_name)


if __name__ == "__main__":
    # cwd = os.getcwd()
    # print(cwd)
    # os.chdir('app/')
    # cwd = os.getcwd()
    # print(cwd)
    data_integrity_check()
