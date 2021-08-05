import pandas as pd
import numpy as np
import pickle

CRASHES_DROP = [
    'RD_NO',
    'CRASH_DATE_EST_I',
    'LANE_CNT',
    'REPORT_TYPE',
    'NOT_RIGHT_OF_WAY_I',
    'DATE_POLICE_NOTIFIED',
    'SEC_CONTRIBUTORY_CAUSE',
    'STREET_NO',
    'STREET_DIRECTION',
    'STREET_NAME',
    'BEAT_OF_OCCURRENCE',
    'PHOTOS_TAKEN_I',
    'STATEMENTS_TAKEN_I',
    'DOORING_I',
    'WORK_ZONE_TYPE',
    'WORKERS_PRESENT_I',
    'INJURIES_UNKNOWN',
    'INJURIES_INCAPACITATING',
    'INJURIES_NON_INCAPACITATING',
    'INJURIES_REPORTED_NOT_EVIDENT',
    'INJURIES_NO_INDICATION',
    'LOCATION'
]

NA_VALUES = [
    'UNKNOWN',
    'OTHER',
    'NOT APPLICABLE',
    'UNABLE TO DETERMINE',
    'NOT REPORTED',
]


def main():
    crashes = pd.read_csv('chicago_crashes.csv',
                          na_values=NA_VALUES,
                          true_values=['Y'],
                          false_values=['N']
                          ).drop(columns=CRASHES_DROP)

    # Save only samples that have a clear primary contributory cause and coordinates
    crashes.dropna(subset=['PRIM_CONTRIBUTORY_CAUSE', 'LATITUDE', 'LONGITUDE'], axis=0, inplace=True)

    # Change CRASH_DATE to CRASH_YEAR
    crashes['CRASH_DATE'] = crashes['CRASH_DATE'].map(lambda x: pd.to_datetime(x).year)
    crashes.rename({'CRASH_DATE': 'CRASH_YEAR'}, axis=1, inplace=True)

    crashes_injuries = crashes[crashes.MOST_SEVERE_INJURY.isin([
        'NONINCAPACITATING INJURY',
        'INCAPACITATING INJURY',
        'FATAL'
    ])]

    with open('crashes.pkl', 'wb') as c:
        pd.to_pickle(crashes, c)

    with open('crashes_injuries.pkl', 'wb') as ci:
        pd.to_pickle(crashes_injuries, ci)

if __name__ == '__main__':
    main()