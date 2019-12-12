import pandas as pd
import matplotlib.pyplot as plt

file1 = pd.read_csv('co-emissions-per-capita.csv')
file2 = pd.read_csv('life-expectancy.csv')
combined = pd.merge(file1,file2,on=['Year','Entity','Code'])
combined.set_index('Year',inplace=True)
combined.columns = ['Country','Code','CO2 Emission','Life expectancy']
nepall = combined[combined.Country == 'Nepal']
nepal = nepall.loc['1962':]
co2 = nepal['CO2 Emission']
life = nepal['Life expectancy']

fig, ax = plt.subplots()
ax.plot(co2,color = 'blue',label='CO2 Emission')
ax.set_xlabel('Year')
ax.set_ylabel('CO2 Emissions (Tonnes per capita)')
ax.tick_params(axis='y', colors='blue')
ax.yaxis.label.set_color('blue')
plt.legend(loc='upper left')

ax2= ax.twinx()
ax2.plot(life,color = 'red',label='Life expectancy')
ax2.set_xlabel('Year')
ax2.set_ylabel('Life expectancy (years)')
ax2.tick_params(axis='y', colors='red')
ax2.yaxis.label.set_color('red')
plt.legend(loc='upper center')
'''
plt.plot(co2)
plt.twinx()
plt.plot(life)
plt.title('Nepal\'s CO2 emission and life expectancy',fontsize='15',color='Brown')
plt.legend(('CO2 Emission','Life expectancy'), loc='upper left')
'''
plt.savefig('New.png')
plt.show()