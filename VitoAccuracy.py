import json
import os

import pandas as pd
from pandas.core.frame import DataFrame
from sklearn.metrics import accuracy_score

from vito_algorithms import nightsignal as ns


def add_blank_rows(df, no_rows):
    df_new = pd.DataFrame(columns=df.columns)
    for idx in range(len(df)):
        df_new = df_new.append(df.iloc[idx])
        for _ in range(no_rows):
            df_new = df_new.append(pd.Series(), ignore_index=True)
    return df_new



def processAll(folder_path="./sample_data/", type="Healthv6v2"):
        folder_path = folder_path + type
        filenames = os.listdir(folder_path)
        for file in filenames:
            if "csv" in file:

                try:
                    processData(os.path.join(folder_path, file))
                except:
                    print()
def processData(HRFile):

        df = pd.DataFrame()
        df = pd.read_csv(HRFile)
        df.to_csv(os.path.join("/tmp/tmp.csv"))
        count = df.shape[0]
        devices = []
        for i in range(count):
            devices.append("HK Apple Watch")
        df.insert(0, "Device", devices, True)

        dfSteps = DataFrame()
        steps = []
        start_time = []
        end_time = []
        start_date = []

        dfSteps.insert(0, "Steps", steps, True)
        dfSteps.insert(0, "Start_Date", start_date, True)
        dfSteps.insert(0, "Start_Time", start_time, True)
        dfSteps.insert(0, "End_Date", start_date, True)
        dfSteps.insert(0, "End_Time", end_time, True)
        dfSteps.to_csv(os.path.join("/tmp/tmp2.csv"))



        ns.getScore(os.path.join("/tmp/tmp.csv"), "/tmp/tmp2.csv")

        with open(os.path.join("/tmp/NS-signals.json"), "r") as f:

            data = json.load(f)
            os.system("rm " + os.path.join("/tmp/NS-signals.json"))
            os.system("rm " + os.path.join("/tmp/tmp.csv"))

        alerts = data["nightsignal"]
        if HRFile is not None:
            alertVals = []
            allAlertVals = []
            allDates = []
            for item in alerts:

                allAlertVals.append(item["val"])

                allDates.append(item["date"])
                if int(item["val"]) > 1:

                    alertVals.append(item["val"])

        print(accuracy_score(alertVals, pd.read_csv(HRFile)["risk"]))


processAll()