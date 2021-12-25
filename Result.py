import pandas as pd
import csv 
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics

df=pd.read_csv("StudentsPerformance.csv")
readinglist=df["reading score"].tolist()
meanreading=statistics.mean(readinglist)
modereading=statistics.mode(readinglist)
medianreading=statistics.median(readinglist)
stdevreading=statistics.stdev(readinglist)
print("Mean: ", meanreading)
print("Mode: ", modereading)
print("Median: ", medianreading)
print("Standard Deviation: ", stdevreading)
stdev1start, stdev1end=meanreading-stdevreading, meanreading+stdevreading
stdev2start, stdev2end=meanreading-2*stdevreading, meanreading+2*stdevreading
stdev3start, stdev3end=meanreading-3*stdevreading, meanreading+3*stdevreading
datawithin1std=[result for result in readinglist if result>stdev1start and result<stdev1end]
datawithin2std=[result for result in readinglist if result>stdev2start and result<stdev2end]
datawithin3std=[result for result in readinglist if result>stdev3start and result<stdev3end]
print("percentage of data within 1st standard deviation: ", (len(datawithin1std)*100/ len(readinglist)))
print("percentage of data within 2nd standard deviation: ", (len(datawithin2std)*100/ len(readinglist)))
print("percentage of data within 3rd standard deviation: ", (len(datawithin3std)*100/ len(readinglist)))
graph=ff.create_distplot([df["reading score"].tolist()], ["readingdistribution"], show_hist=False)
graph.add_trace(go.Scatter(x=[meanreading, meanreading], y=[0, 0.025], mode="lines", name="mean"))
graph.add_trace(go.Scatter(x=[stdev1start, stdev1start], y=[0, 0.025], mode="lines", name="mean"))
graph.add_trace(go.Scatter(x=[stdev1end, stdev1end], y=[0, 0.025], mode="lines", name="mean"))
graph.add_trace(go.Scatter(x=[stdev2start, stdev2start], y=[0, 0.025], mode="lines", name="mean"))
graph.add_trace(go.Scatter(x=[stdev2end, stdev2end], y=[0, 0.025], mode="lines", name="mean"))
graph.add_trace(go.Scatter(x=[stdev3start, stdev3start], y=[0, 0.025], mode="lines", name="mean"))
graph.add_trace(go.Scatter(x=[stdev3end, stdev3end], y=[0, 0.025], mode="lines", name="mean"))
graph.show()
