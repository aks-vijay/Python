import matplotlib.pyplot as plt
%matplotlib inline

blood_sugar_m = [130,100,82,115,86,72,142,92,178,145,71]
blood_sugar_f = [115,122,134,77,89,86,128,172,281,120,112]

plt.xlabel ('sugar range')
plt.ylabel ('total number of patients')
plt.title ('blood sugar analysis')

plt.hist([blood_sugar_m, blood_sugar_f], 
         bins = [80,100,125,150], 
         rwidth = 0.95, 
         color = ['green','orange'],
         label = ['men', 'women'],
         alpha = 0.6, 
         orientation='horizontal')

plt.legend()
