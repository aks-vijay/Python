import matplotlib.pyplot as plt
%matplotlib inline

exp_values = [1400,500,200,400,100]
exp_labels = ['Rent','Food','Phone and Internet bill','Car','Other utilities']

plt.axis('equal')
plt.pie(exp_values, 
        labels = exp_labels, 
        radius = 1.5, 
        autopct='%0.0f%%', 
        shadow = True, 
        explode = [0,0,0,0.5,0], 
        startangle=160)
plt.show()
