import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import parallel_coordinates
from math import pi
from scipy import stats
from scipy.stats import shapiro

class ExploratoryDataAnalysis:
    def __init__(self, dataframe):
        """
        Initialize the ExploratoryDataAnalysis with a pandas DataFrame.
        :param dataframe: DataFrame for analysis.
        """
        self.df = dataframe

    def basic_summary(self):
        """
        Prints basic summary information of the DataFrame.
        """
        print("Basic Summary:")
        print(self.df.describe())
        print("\nFirst Few Rows:")
        print(self.df.head())

    def plot_distribution(self, column, plot_type='histogram'):
        """
        Plots the distribution of a specified column.
        :param column: The column to plot.
        :param plot_type: Type of plot ('histogram' or 'boxplot').
        """
        if plot_type == 'histogram':
            plt.hist(self.df[column].dropna(), bins=30, edgecolor='black')
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.show()
        elif plot_type == 'boxplot':
            sns.boxplot(x=self.df[column])
            plt.title(f'Boxplot of {column}')
            plt.show()

    def plot_correlation_matrix(self):
        """
        Plots the correlation matrix of the DataFrame.
        """
        plt.figure(figsize=(10, 8))
        sns.heatmap(self.df.corr(), annot=True, fmt=".2f", cmap='viridis')
        plt.title('Correlation Matrix')
        plt.show()

    def countplot_categorical(self, column):
        """
        Creates a count plot for a categorical column.
        :param column: The column to create a count plot for.
        """
        sns.countplot(x=self.df[column])
        plt.title(f'Count Plot of {column}')
        plt.xticks(rotation=45)
        plt.show()

    def scatterplot_relationship(self, column1, column2):
        """
        Creates a scatter plot to show the relationship between two numerical columns.
        :param column1: First numerical column.
        :param column2: Second numerical column.
        """
        sns.scatterplot(x=self.df[column1], y=self.df[column2])
        plt.title(f'Scatter Plot between {column1} and {column2}')
        plt.show()

    def time_series_plot(self, date_column, target_column):
        """
        Creates a time series plot for a target column.
        :param date_column: The column representing date.
        :param target_column: The target column to plot over time.
        """
        self.df[date_column] = pd.to_datetime(self.df[date_column])
        self.df.set_index(date_column, inplace=True)
        self.df[target_column].plot()
        plt.title(f'Time Series Plot of {target_column}')
        plt.ylabel(target_column)
        plt.show()

    def pairplot_relationships(self, columns, hue=None):
        """
        Plots pairwise relationships for a set of specified columns.
        :param columns: List of columns to include in the plot.
        :param hue: Variable in `data` to map plot aspects to different colors.
        """
        sns.pairplot(self.df[columns], hue=hue)
        plt.show()

    def barplot_categorical_vs_numerical(self, categorical_column, numerical_column):
        """
        Creates a bar plot to compare a numerical column across different categories.
        :param categorical_column: The categorical column.
        :param numerical_column: The numerical column to compare.
        """
        sns.barplot(x=self.df[categorical_column], y=self.df[numerical_column])
        plt.xticks(rotation=45)
        plt.show()

    # New Methods
    def plot_stacked_bar_chart(self, category_column, value_column):
        """
        Creates a stacked bar chart for a categorical column and a value column.
        :param category_column: The categorical column.
        :param value_column: The value column for stacking.
        """
        pivot_data = self.df.pivot_table(index=category_column, columns=value_column, aggfunc='size', fill_value=0)
        pivot_data.plot(kind='bar', stacked=True)
        plt.title(f'Stacked Bar Chart of {category_column} by {value_column}')
        plt.xlabel(category_column)
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.show()

    def plot_density_curve(self, column):
        """
        Plots the density curve of a numerical column.
        :param column: The numerical column to plot.
        """
        sns.kdeplot(self.df[column], shade=True)
        plt.title(f'Density Curve of {column}')
        plt.xlabel(column)
        plt.show()

    def cumulative_frequency_plot(self, column):
        """
        Creates a cumulative frequency plot for a numerical column.
        :param column: The numerical column for the cumulative frequency plot.
        """
        self.df[column].sort_values().cumsum().plot()
        plt.title(f'Cumulative Frequency of {column}')
        plt.xlabel(column)
        plt.ylabel('Cumulative Frequency')
        plt.show()

    def plot_parallel_coordinates(self, columns, class_column):
        """
        Plots parallel coordinates for a set of columns.
        :param columns: List of columns to include in the plot.
        :param class_column: The column to use for coloring.
        """
        parallel_coordinates(self.df[columns + [class_column]], class_column)
        plt.xticks(rotation=45)
        plt.title('Parallel Coordinates Plot')
        plt.show()

    def plot_radial_chart(self, category_column, value_column):
        """
        Plots a radial chart for a categorical column.
        :param category_column: The categorical column.
        :param value_column: The numerical column to plot.
        """
        categories = list(self.df[category_column].unique())
        N = len(categories)

        values = self.df.groupby(category_column)[value_column].mean().tolist()
        values += values[:1]

        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        ax = plt.subplot(111, polar=True)
        plt.xticks(angles[:-1], categories, color='grey', size=12)

        ax.plot(angles, values)
        ax.fill(angles, values, 'teal', alpha=0.1)
        plt.show()





class ExploratoryDataAnalysisNICS:
    def __init__(self, dataframe):
        self.df = dataframe

    def basic_summary(self):
        print("Basic Summary:")
        print(self.df.describe())
        print("\nFirst Few Rows:")
        print(self.df.head())

    def plot_distribution(self, column, plot_type='histogram'):
        if plot_type == 'histogram':
            plt.hist(self.df[column].dropna(), bins=30, edgecolor='black')
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.show()
        elif plot_type == 'boxplot':
            sns.boxplot(x=self.df[column])
            plt.title(f'Boxplot of {column}')
            plt.show()

    def plot_correlation_matrix(self):
        plt.figure(figsize=(10, 8))
        sns.heatmap(self.df.corr(), annot=True, fmt=".2f", cmap='viridis')
        plt.title('Correlation Matrix')
        plt.show()

    def heatmap_for_year_and_state(self, column):
        self.df['year'] = pd.to_datetime(self.df['date_year'])
        heatmap_data = self.df.pivot_table(values=column, index='year', columns='state', aggfunc='sum')
        plt.figure(figsize=(20, 15))
        sns.heatmap(heatmap_data, annot=False, cmap='viridis')
        plt.title(f'Heatmap for Year and State Comparison of {column}')
        plt.show()

    def monthly_sum_comparison(self, columns):
        monthly_data = self.df.groupby(self.df['date_month'])[columns].sum()
        monthly_data.plot(kind='bar', stacked=False)
        plt.title('Monthly Sum Comparison')
        plt.xlabel('Month')
        plt.ylabel('Sum')
        plt.show()

    def cumulative_sum_plot(self, column):
        self.df[column].cumsum().plot()
        plt.title(f'Cumulative Sum of {column}')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Sum')
        plt.show()

    def boxplot_by_state(self, column):
        plt.figure(figsize=(15, 10))
        sns.boxplot(x='state', y=column, data=self.df)
        plt.title(f'Boxplot of {column} by State')
        plt.xticks(rotation=90)
        plt.show()

    def plot_statewise_trends(self, column):
        for state in self.df['state'].unique():
            state_data = self.df[self.df['state'] == state]
            state_data.set_index('date')[column].plot(label=state)
        plt.legend()
        plt.title(f'State-wise Trends of {column}')
        plt.ylabel(column)
        plt.show()

    def statistical_analysis(self, column):
        data = self.df[column].dropna()
        print(f"Statistical Analysis for {column}:")
        print("Mean:", np.mean(data))
        print("Median:", np.median(data))
        mode_result = stats.mode(data)
        # print("Mode:", mode_result.mode[0] if mode_result.count[0] > 0 else "No mode")
        print("Standard Deviation:", np.std(data))
        print("Variance:", np.var(data))

    def validate_data_normality(self, column):
        data = self.df[column].dropna()
        stat, p_value = shapiro(data)
        print(f"Normality Test for {column}:")
        print("Statistics:", stat)
        print("P-Value:", p_value)
        if p_value > 0.05:
            print("Data is likely normal.")
        else:
            print("Data is likely not normal.")

    def plot_regression(self, column1, column2):
        sns.regplot(x=column1, y=column2, data=self.df)
        plt.title(f'Regression Line between {column1} and {column2}')
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.show()