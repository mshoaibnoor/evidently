import pandas as pd
import numpy as np

from sklearn import datasets

from evidently.report import Report
from evidently.metric_preset import DataDriftPreset


bcancer_data = datasets.load_breast_cancer(as_frame=True)
bcancer = bcancer_data.frame

bcancer_ref = bcancer.sample(n=300, replace=False)
bcancer_cur = bcancer.sample(n=200, replace=False)


data_drift_report = Report(
    metrics=[DataDriftPreset()]
)

data_drift_report.run(reference_data=bcancer_ref, current_data=bcancer_cur)


data_drift_report.save_html('/scikit_learn_data/workspace/data_drift_report.html')