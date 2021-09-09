import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

days = [1,2,3,4,5,6,7]
max_t = [45,72,52,54,27,78,52]
min_t = [45,65,20,47,29,38,32]
avg_t = [25,62,18,42,22,32,31]

plt.xlabel('Weekdays')
plt.ylabel('Temperature')
plt.title('Weather')

plt.plot(days, max_t, label = 'Max')
plt.plot(days, min_t, label = 'Min')
plt.plot(days, avg_t, label = 'Average')

plt.legend(loc = 'best', shadow = True, fontsize = 'small')

plt.grid()

company = ['GOOGL', 'AMZN', 'MSFT', 'FB']
revenue = [90,136,89,27]
profit = [42, 9, 34, 12]

xpos = np.arange(len(company))

plt.xticks(ypos, company)
plt.ylabel("Revenue (bil)")
plt.xlabel("Company")
plt.title("US Tech Stocks")
plt.bar(xpos-0.2, revenue, color = 'orange', label = 'revenue', width = 0.4)
plt.bar(xpos+0.2, profit, label = 'profit', width = 0.4)
plt.legend()

plt.yticks(ypos, company)
plt.xlabel("Revenue (bil)")
plt.ylabel("Company")
plt.title("US Tech Stocks")
plt.barh(xpos-0.2, revenue, color = 'orange', label = 'revenue', height = 0.4)
plt.barh(xpos+0.2, profit, label = 'profit', height = 0.4)
plt.legend()
