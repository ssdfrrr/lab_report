import statsmodels.api as sm
import matplotlib.pyplot as plt

data = sm.datasets.copper.load_pandas().data


data['YEAR'] = data['YEAR'].astype(int)
filtered_data = data[(data['YEAR'] >= 1961) & (data['YEAR'] <= 1970)]


plt.figure(figsize=(12, 6))

plt.plot(filtered_data['YEAR'], filtered_data['WORLDCONSUMPTION'],
         label='World Consumption', marker='o')

plt.plot(filtered_data['YEAR'], filtered_data['COPPERPRICE'],
         label='Copper Price', marker='s')

plt.plot(filtered_data['YEAR'], filtered_data['ALUMPRICE'],
         label='Aluminium Price', marker='^')

plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Copper and Aluminium Market Dynamics (1961-1970)')
plt.legend()
plt.grid(True)
plt.show()