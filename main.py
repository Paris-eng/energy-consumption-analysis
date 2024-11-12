# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import matplotlib.pyplot as plt
import numpy as np

# Data for the top 5 energy consuming countries and their energy consumption breakdown by source
countries = ['China', 'United States', 'India', 'Russia', 'Japan']
sources = ['Coal', 'Oil', 'Natural Gas', 'Nuclear', 'Renewables']

# Energy consumption data in exajoules (EJ)
energy_consumption = {
    'China': [82.4, 15.3, 10.6, 2.9, 9.3],
    'United States': [11.3, 35.2, 31.8, 8.4, 7.5],
    'India': [17.5, 9.8, 6.2, 0.8, 3.1],
    'Russia': [4.2, 7.1, 22.4, 5.7, 0.2],
    'Japan': [1.2, 7.5, 4.5, 1.6, 3.8]
}

# Create a stacked bar chart
fig, ax = plt.subplots()

# Bottoms for stacking bars
bottoms = np.zeros(len(countries))

# Plot each energy source
for source in sources:
    values = [energy_consumption[country][sources.index(source)] for country in countries]
    ax.bar(countries, values, bottom=bottoms, label=source)
    bottoms += values

# Add labels and title
ax.set_ylabel('Energy Consumption (EJ)')
ax.set_title('Energy Consumption Breakdown by Source for Top 5 Energy Consuming Countries')
ax.legend()

# Save the plot as an image file
plt.savefig('energy_consumption_breakdown.png')

# Show the plot
plt.show()
