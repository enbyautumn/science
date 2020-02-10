import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 3 * np.pi, 2)
y = np.exp(np.sin(x))

plt.stem(x, y, use_line_collection=True)
plt.show()

#The first number controls the initial hieght of the graph, and the second number 
#after the comma controls the frquency of the graph. Finally, the third number after the np.pi, 
#controls the number of data points or lines.


markerline, stemlines, baseline = plt.stem(
    x, y, linefmt='grey', markerfmt='D', bottom=1.1, use_line_collection=True)
markerline.set_markerfacecolor('none')
plt.show()


#This controls the shape and color of the data point and it also creates a "baseline" that the graph can go above or below
