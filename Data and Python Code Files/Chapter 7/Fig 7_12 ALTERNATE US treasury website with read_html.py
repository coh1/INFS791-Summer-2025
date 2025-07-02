import pandas as pd

#brings in the ssl module, which provides functionalities for working with Secure Sockets Layer (SSL) and Transport Layer Security (TLS).
import ssl

#disables SSL/TLS certificate verification for all subsequent HTTPS connections made using the default ssl context.
ssl._create_default_https_context = ssl._create_unverified_context

# The following line assigns the URL of interest to a variable
cta_bus_routes_url = "https://en.wikipedia.org/wiki/List_of_Chicago_Transit_Authority_bus_routes"

##"https://www.treasury.gov/resource-center/data-chart-center" \
##                + "/interest-rates/pages/TextView.aspx?data=yieldYear&year=2018"


#  The following line uses the Pandas read_html function to read all
#   the HTML tables from the webpage and create a list of DataFrame objects.
tables = pd.read_html(cta_bus_routes_url)

former_routes_table = tables[1]
print(former_routes_table.columns)

print("The first 5 rows of data are:")
print(former_routes_table.head())

print("The last 5 rows of data are:")
print(former_routes_table.tail())
