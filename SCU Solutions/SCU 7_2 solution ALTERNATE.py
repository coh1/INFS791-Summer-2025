import pandas as pd

#brings in the ssl module, which provides functionalities for working with Secure Sockets Layer (SSL) and Transport Layer Security (TLS).
import ssl

#disables SSL/TLS certificate verification for all subsequent HTTPS connections made using the default ssl context.
ssl._create_default_https_context = ssl._create_unverified_context

# read the table at the following URL:
trips_update_url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2018"

# use the Pandas module to read the HTML of the page:
tables = pd.read_html(trips_update_url)

# The webpage has two tables. Read the first table into update_table object:
update_table = tables[0]

# The following prints out table information
print(update_table.columns)
print("The first five rows of data are:")
print(update_table.head())
print("The last five rows of data are:")
print(update_table.tail())
print("Summary statistics of the dataset are:")
print(update_table.describe())
