import pandas as pd
import numpy as np

from sklearn import datasets

from evidently.report import Report
from evidently.metric_preset import DataDriftPreset,DataQualityPreset,TargetDriftPreset, RegressionPreset, ClassificationPreset


bcancer_data = datasets.load_breast_cancer(as_frame=True)
bcancer = bcancer_data.frame

bcancer_ref = bcancer.sample(n=300, replace=False)
bcancer_cur = bcancer.sample(n=200, replace=False)

# data drift report
data_drift_report = Report(
    metrics=[
        DataDriftPreset()
        ]
)

data_drift_report.run(reference_data=bcancer_ref, current_data=bcancer_cur)


data_drift_report.save_html('/scikit_learn_data/workspace/data_drift_report.html')

# data drift report

# data quality report
data_quality_report = Report(
    metrics=[
        DataQualityPreset()
    ]
)
data_quality_report.run(reference_data=bcancer_ref, current_data=bcancer_cur)
data_quality_report.save_html('/scikit_learn_data/workspace/data_quality_report.html')

# data quality report


# target drift report
target_drift_report = Report(
    metrics=[
        TargetDriftPreset()
    ]
)
target_drift_report.run(reference_data=bcancer_ref, current_data=bcancer_cur)
target_drift_report.save_html('/scikit_learn_data/workspace/target_drift_report.html')

# target drift report

# regression performance report
regression_performance_report = Report(
    metrics=[
        RegressionPreset()
    ]
)
regression_performance_report.run(reference_data=bcancer_ref, current_data=bcancer_cur)
regression_performance_report.save_html('/scikit_learn_data/workspace/regresion_performance_report.html')
# regression performance report

# classification performance report
classification_performance_report = Report(
    metrics=[
        ClassificationPreset(probas_threshold=0.7)
    ]
)

classification_performance_report.run(reference_data=bcancer_ref, current_data=bcancer_cur)
classification_performance_report.save_html('/scikit_learn_data/workspace/classification_performance_report.html')
# classification performance report