import pandas as pd

class DataTransformer:
    def __init__(self, dataframe):
        """
        Initialize the DataTransformer with a pandas DataFrame.
        :param dataframe: DataFrame to be transformed.
        """
        self.df = dataframe

    def extract_date_components(self, date_column, drop_original=True):
        """
        Extracts components from a date column (year, month, day).
        :param date_column: The name of the column containing date information.
        :param drop_original: Boolean, whether to drop the original date column after extraction.
        """
        self.df[date_column] = pd.to_datetime(self.df[date_column])
        self.df[date_column + '_year'] = self.df[date_column].dt.year
        self.df[date_column + '_month'] = self.df[date_column].dt.month
        self.df[date_column + '_day'] = self.df[date_column].dt.day

        # if drop_original:
        #     self.df.drop(columns=[date_column], inplace=True)
        return self.df
