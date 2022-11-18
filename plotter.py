import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# read Book1.csv
df = pd.read_csv('Book1.csv')
# print(df)

# data has 4 col
# window size on x axis
# throughput 5ms, throughput 50ms, throughput 150ms on y axis
# plot all on a single graph

# plot throughput 5ms
plt.plot(df['Window Size'], df['Throughput 5ms'], label = "Throughput 5ms")
# plot throughput 50ms
plt.plot(df['Window Size'], df['Throughput 50ms'], label = "Throughput 50ms")
# plot throughput 150ms
plt.plot(df['Window Size'], df['Throughput 150ms'], label = "Throughput 150ms")

# naming the x axis
plt.xlabel('Window Size')
# add x axis ticks as string
plt.xticks(df['Window Size'])
# naming the y axis
plt.ylabel('Throughput')
# giving a title to my graph
plt.title('Throughput vs Window Size')
# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()

