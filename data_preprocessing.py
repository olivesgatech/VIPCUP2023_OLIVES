import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import glob
from tqdm import tqdm
from PIL import Image
from collections import Counter
def combine_excel(csv_dir):
    filenames = glob.glob(csv_dir + "/*.xlsx")
    outputxlsx = pd.DataFrame()

    for file in filenames:
        df = pd.concat(pd.read_excel(file, sheet_name=None), ignore_index=True, sort=False)
        outputxlsx = outputxlsx.append(df, ignore_index=True)

    outputxlsx.to_csv('test_set_labels.csv',index=False)

def analyze_dataframe(csv_dir):
    pass

def process_images(csv_dir):
    df = pd.read_csv(csv_dir)

    for i in tqdm(range(0,len(df))):
        path = df.iloc[i,0]
        im = Image.open(path).convert('L')


def numpy_submission(sub_dir,np_dir):
    np_file  = np.load(np_dir)
    print(len(np_file))
    sub_dir = pd.read_csv(sub_dir)
    print(len(sub_dir))
    for i in range(0,len(sub_dir)):
        sub_dir.iloc[i,1] = np_file[i,0]
        sub_dir.iloc[i, 2] = np_file[i, 1]
        sub_dir.iloc[i, 3] = np_file[i, 2]
        sub_dir.iloc[i, 4] = np_file[i, 3]
        sub_dir.iloc[i, 5] = np_file[i, 4]
        sub_dir.iloc[i, 6] = np_file[i, 5]
    print(sub_dir.head())
    sub_dir.to_csv('baseline_result.csv',index=False)
def patient_count(csv_dir):
    df = pd.read_csv(csv_dir)
    patient_list = []
    for i in range(0,len(df)):
        file_name = df.iloc[i,0]
        patient_id = file_name.split('-')[1]
        patient_list.append(patient_id)
    print(len(Counter(patient_list).keys()))  # equals to list(set(words))
    print(len(Counter(patient_list).values()))  # counts the elements' frequency

if __name__ == '__main__':
    # Patient_Analysis
    #csv_dir = '/home/kiran/Desktop/Dev/VIPCUP2023_OLIVES/csv_dir/Phase2_Corrected.csv'
    #patient_count(csv_dir)
    # Generate Submission CSV

    csv_dir = '/home/kiran/Desktop/Dev/VIPCUP2023_OLIVES/csv_dir/Phase2_submission_template.csv'
    np_dir = '/home/kiran/Desktop/Dev/VIPCUP2023_OLIVES/output.npy'
    numpy_submission(csv_dir, np_dir)



    #process_images(csv_dir)