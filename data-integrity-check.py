#pandas 2.0.1 is required to run deepchecks successfully
from deepchecks.tabular.suites import data_integrity
from deepchecks.tabular import Dataset
import pandas as pd
import os

def data_integrity_check():
    data_df = pd.read_csv('/app/data/adult-education-dataset.csv')
    dataset = Dataset(data_df, label='class', cat_features=[])
    suite_result = data_integrity().run(dataset)
    suite_result.save_as_html('/app/output/dataintegritycheck/data_validation.html')


if __name__ == "__main__":
    cwd = os.getcwd()
    print(cwd)
    os.chdir('/app/')
    cwd = os.getcwd()
    print(cwd)
    data_integrity_check()
