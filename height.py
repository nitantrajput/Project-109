import pandas as pd 
import csv 
import plotly.figure_factory as ff

df = pd.read_csv('data.csv')
figure = ff.create_distplot([df['Height(Inches)'].tolist()],['height'])
#figure.show()
height_list = df['Height(Inches)'].tolist()
import statistics
import plotly.graph_objects as go 
mean = statistics.mean(height_list)
median = statistics.median(height_list)
mode = statistics.mode(height_list)
print('mean , median , mode is {} , {} , {}'.format(mean , median , mode))
stdev = statistics.stdev(height_list)
print('stdev = {}'.format(stdev))
fstart , fend = mean - stdev       , mean +      stdev 
sstart , send = mean - (2 * stdev) , mean + (2 * stdev)
tstart , tend = mean - (3 * stdev) , mean + (3 * stdev)
data_in_first_stdev =  [results for results in height_list if results > fstart and results < fend]
data_in_second_stdev = [results for results in height_list if results > sstart and results < send]
data_in_third_stdev =  [results for results in height_list if results > tstart and results < tend]
print('{}% of data lies within first standard deviation'.format(len(data_in_first_stdev) * 100.0 / len(height_list)))
print('{}% of data lies within second standard deviation'.format(len(data_in_second_stdev)*100.0 / len(height_list)))
print('{}% of data lies within third standard deviation'.format(len(data_in_third_stdev) * 100.0 / len(height_list)))
fig = ff.create_distplot([df['Height(Inches)'].tolist()],['height'] , show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[fstart, fstart], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[fend, fend], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[sstart, sstart], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[send, send], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[tstart, tstart], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[tend, tend], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()