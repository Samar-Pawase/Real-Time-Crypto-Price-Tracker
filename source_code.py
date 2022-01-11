'''
********************TRACK TOP 20 CRYPTOCURRENCIES IN REAL TIME********************

This program will help you to visualize real time price fluctuations of top 20 Cryptocurrencies by plotting the PRICE vs TIME graph using matplotlib in python.

NOTE:
1. Before running the code copy paste this command in the terminal to automatically install all the required dependencies. command: pip install -r requirements.txt
2. The default time interval is set to 1 second. You can change the time interval in line number 85
'''


# Importing modules
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import cryptocompare
from datetime import datetime
from pandas import *

# Declaring list to store user input from choice function
output = []

# Dictionary to store currencies and their codes
currency_code = {'INR': "Indian Rupee",
                 'USD': 'US Dollar', 'EUR': 'European Dollar'}

# Fetching data for crypto names and their codes from an excel
xls = ExcelFile('Currency_crypto_codes.xlsx')
data = xls.parse(xls.sheet_names[0])
excel_to_dict = data.to_dict()
crypto_names_dict = excel_to_dict['Name']
crypto_codes_dict = excel_to_dict['Code']


# Function to take input of the cryto to track, and currency
def choice():
    print("\n\n", excel_to_dict['Name'])
    code_input = int(input("\nEnter number to track crypto: "))
    output.append(crypto_codes_dict[code_input])
    print("\n\n", currency_code)
    currency_input = input("\nEnter currency code (Eg - INR): ")
    output.append(currency_input)
    output.append(code_input)
    return output


# Function to get price of specified crypto in given currency from cryptocompare API
def get_crypto_price(cryptocurrency, curr):
    return cryptocompare.get_price(cryptocurrency, currency=curr)[cryptocurrency][curr]


# Function to get the full name of cryptocurrency from cryptocompare API
def get_crypto_name(cryptocurrency):
    return cryptocompare.get_coin_list()[cryptocurrency]['FullName']


# Calling choice function to take user input for crypto to track, and currency in which it will be tracked
choice()


# Function to animate the plotting of price vs time graph
def animate(i):
    x_vals.append(datetime.now())
    y_vals.append(get_crypto_price(output[0], output[1]))
    plt.cla()
    plt.title(get_crypto_name(output[0]) + ' Price Plotting')
    plt.gcf().canvas.set_window_title('Cryptocurrency Price Tracking')
    plt.xlabel('Time')
    plt.ylabel(f'Price in {currency_code[output[1]]}')
    plt.plot_date(x_vals, y_vals, linestyle="solid", ms=0)
    plt.tight_layout()


# Plot style is seaborn
plt.style.use('seaborn')

# Prices will get appended in the y_vals list after specified interval
y_vals = []

# Time will get appended in the x_vals list after specified interval
x_vals = []

# Time interval in seconds. Feel free to change it.
# ( Default - 1 sec )
interval = 1 

# Animating the plot in the interval of time 
ani = FuncAnimation(plt.gcf(), animate, interval*1000)

print(
    f"Plot for {crypto_names_dict[output[2]]} ({output[0]}) in {currency_code[output[1]]} will be displayed\n"
    )

# Displaying the plot
plt.show()
