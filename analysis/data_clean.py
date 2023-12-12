import pandas as pd

class DataCleaner:
    def __init__(self, dataframe):
        """
        Initialize the DataCleaner with a pandas DataFrame.
        :param dataframe: DataFrame to be cleaned.
        """
        self.df = dataframe

    def remove_duplicates(self):
        """
        Removes duplicate rows from the DataFrame.
        """
        self.df.drop_duplicates(inplace=True)
        return self.df

    def handle_missing_values(self, strategy='mean', specific_column=None, custom_fill_value=None):
        """
        Handles missing values in the DataFrame.
        :param strategy: Strategy to handle missing values ('mean', 'median', 'drop', 'custom', etc.)
        :param specific_column: Specifies a column to apply the missing value strategy. If None, applies to all columns.
        :param custom_fill_value: Custom value to fill missing data if strategy is 'custom'.
        """
        columns = [specific_column] if specific_column else self.df.columns

        for col in columns:
            if self.df[col].dtype.kind in 'biufc' and strategy in ['mean', 'median']:  # Numerical columns
                if strategy == 'mean':
                    self.df[col].fillna(self.df[col].mean(), inplace=True)
                elif strategy == 'median':
                    self.df[col].fillna(self.df[col].median(), inplace=True)
            elif strategy == 'drop':
                self.df.dropna(subset=[col], inplace=True)
            elif strategy == 'custom':
                self.df[col].fillna(custom_fill_value, inplace=True)

        return self.df

    def convert_data_types(self, column, new_type):
        """
        Converts the data type of a specified column.
        :param column: Column name whose data type is to be converted.
        :param new_type: The new data type (e.g., 'float', 'int', 'str').
        """
        self.df[column] = self.df[column].astype(new_type)
        return self.df

    def check_for_outliers(self, column):
        """
        Identifies outliers in a specified column.
        :param column: Column to be checked for outliers.
        :return: DataFrame with identified outliers.
        """
        q1 = self.df[column].quantile(0.25)
        q3 = self.df[column].quantile(0.75)
        iqr = q3 - q1
        outlier_condition = (self.df[column] < (q1 - 1.5 * iqr)) | (self.df[column] > (q3 + 1.5 * iqr))
        return self.df[outlier_condition]

    def standardize_categorical(self, column):
        """
        Standardizes categorical data by converting to lowercase.
        :param column: Column containing categorical data.
        """
        if self.df[column].dtype == 'object':
            self.df[column] = self.df[column].str.lower()
        return self.df

    def encode_categorical(self, column, method='onehot'):
        """
        Encodes categorical data.
        :param column: Column containing categorical data.
        :param method: Encoding method ('onehot' or 'label').
        """
        if method == 'onehot':
            dummies = pd.get_dummies(self.df[column], prefix=column)
            self.df = pd.concat([self.df, dummies], axis=1)
        elif method == 'label':
            self.df[column] = self.df[column].astype('category').cat.codes
        return self.df