"""
This file is meant to be executed in the terminal while the Chicago Data Portal CSV file, Traffic Crashes - Crashes,
is present in the data/ directory. Otherwise, the script will fail. Due to its large file size, this CSV is not included
in the repository. However, the results of this script are stored in data/raw/, which will be included.
"""
import pandas as pd

# Define columns from original CSV to drop
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

# Define values to be considered as NaN
NA_VALUES = [
    'UNKNOWN',
    'OTHER',
    'NOT APPLICABLE',
    'UNABLE TO DETERMINE',
    'NOT REPORTED',
]

# Define values in the MOST_SEVERE_INJURIES that indicate injuries
INJURIES = ['NONINCAPACITATING INJURY', 'INCAPACITATING INJURY', 'FATAL']


def main():
    """Create four PKL files from the dataset using the original, large CSV file for Chicago crash data"""
    # Read CSV file
    crashes = pd.read_csv('data/chicago_crashes.csv',
                          na_values=NA_VALUES,
                          true_values=['Y'],
                          false_values=['N']
                          ).drop(columns=CRASHES_DROP)

    # Change CRASH_DATE to CRASH_YEAR
    crashes['CRASH_DATE'] = crashes['CRASH_DATE'].map(lambda x: pd.to_datetime(x).year)
    crashes.rename({'CRASH_DATE': 'CRASH_YEAR'}, axis=1, inplace=True)

    # Drop rows without coordinates
    crashes.dropna(subset=['LATITUDE', 'LONGITUDE'], axis=0, inplace=True)

    # Divide data into samples that have a clear PRIM_CONTRIBUTORY_CAUSE feature, and those that don't
    crashes_cause = crashes.dropna(subset=['PRIM_CONTRIBUTORY_CAUSE'], axis=0)
    crashes_no_cause = crashes.loc[crashes.PRIM_CONTRIBUTORY_CAUSE.isna(), :]

    # Segment data for only considering crashes resulting in injuries
    crashes_injuries_cause = crashes_cause[crashes_cause.MOST_SEVERE_INJURY.isin(INJURIES)]
    crashes_injuries_no_cause = crashes_no_cause[crashes_no_cause.MOST_SEVERE_INJURY.isin(INJURIES)]

    # Pickle each DataFrame
    pickle_df('data/raw/crashes.pkl', crashes_cause)  # With cause, with or without injuries
    pickle_df('data/raw/crashes_no_cause.pkl', crashes_no_cause)  # Without cause, with or without injuries
    pickle_df('data/raw/crashes_injuries.pkl', crashes_injuries_cause)  # With cause, with injuries
    pickle_df('data/raw/crashes_injuries_no_cause.pkl', crashes_injuries_no_cause)  # Without cause, with injuries


def pickle_df(filepath, df):
    """Pickle a Pandas DataFrame given the file path and DataFrame object"""
    with open(filepath, 'wb') as f:
        pd.to_pickle(df, f)


if __name__ == '__main__':
    main()
