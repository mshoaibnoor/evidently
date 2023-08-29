import datetime

from sklearn import datasets
import pandas as pd

adult_data = datasets.fetch_openml(name="adult", version=2, as_frame="auto")
adult = adult_data.frame

df = pd.DataFrame(adult)

df.to_csv('app/data/adult-education-dataset.csv')