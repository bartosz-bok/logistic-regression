import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = np.loadtxt("data/points.csv",delimiter=',')
X = data[:,0:1]
y = data[:,2]

#plot logistic regression curve with black points and red line
sns.regplot(x=X, y=y, data=data, logistic=True, ci=None, scatter_kws={'color': 'black'}, line_kws={'color': 'red'})

plt.title('Logistic Regression')
plt.savefig('images/logistic.png')

plt.show()
