# data_acquisition.py

import pandas as pd

class DataAcquisition:
    def __init__(self, gun_violence_path, nics_bgchecks_path):
        """
        Initializes the data acquisition class with file paths for both datasets.
        :param gun_violence_path: str, path to the gun violence data file.
        :param nics_bgchecks_path: str, path to the NICS background checks data file.
        """
        self.gun_violence_path = gun_violence_path
        self.nics_bgchecks_path = nics_bgchecks_path

    def load_gun_violence_data(self):
        """
        Loads the gun violence data from the CSV file.
        :return: DataFrame containing the gun violence data.
        """
        try:
            data = pd.read_csv(self.gun_violence_path)
            print("Gun Violence Data loaded successfully.")
            return data
        except Exception as e:
            print(f"Error loading Gun Violence Data: {e}")

    def load_nics_bgchecks_data(self):
        """
        Loads the NICS background checks data from the CSV file.
        :return: DataFrame containing the NICS background checks data.
        """
        try:
            data = pd.read_csv(self.nics_bgchecks_path)
            print("NICS Background Checks Data loaded successfully.")
            return data
        except Exception as e:
            print(f"Error loading NICS Background Checks Data: {e}")
