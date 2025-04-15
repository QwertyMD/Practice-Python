import matplotlib.pyplot as plt
# plot a line, implicitly creating a subplot(111)
x=[1,2,3]
y=[4,5,6]
#plt.subplot(nRows,nColumns,index)
# nrows/nColumns number of rows/columns of graphs in the output section
#index position of the graph
plt.subplot(2,2,1)
#subplot(2,2,1) means there will be 2 graphs in row and 2 in columns and index 1 means this graph will be at the first position
plt.plot(x,y, marker='*', color='red')
plt.subplot(2,2,2)
plt.plot(x,y, marker='x', color='green')
plt.subplot(2,2,3)
plt.plot(x,y, marker='^', color='blue')
plt.subplot(2,2,4)
plt.plot(x,y, marker='+', color = 'yellow')
plt.show()