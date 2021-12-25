import pandas as pd
import csv 
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics

df=pd.read_csv("HeightWeight.csv")
heightlist=df["Height"].tolist()
meanheight=statistics.mean(heightlist)
modeheight=statistics.mode(heightlist)
medianheight=statistics.median(heightlist)
stdevheight=statistics.stdev(heightlist)
print("Mean: ", meanheight)
print("Mode: ", modeheight)
print("Median: ", medianheight)
print("Standard Deviation: ", stdevheight)
stdev1start, stdev1end=meanheight-stdevheight, meanheight+stdevheight
stdev2start, stdev2end=meanheight-2*stdevheight, meanheight+2*stdevheight
stdev3start, stdev3end=meanheight-3*stdevheight, meanheight+3*stdevheight
datawithin1std=[result for result in heightlist if result>stdev1start and result<stdev1end]
datawithin2std=[result for result in heightlist if result>stdev2start and result<stdev2end]
datawithin3std=[result for result in heightlist if result>stdev3start and result<stdev3end]
print("percentage of data within 1st standard deviation: ", (len(datawithin1std)*100/ len(heightlist)))
print("percentage of data within 2nd standard deviation: ", (len(datawithin2std)*100/ len(heightlist)))
print("percentage of data within 3rd standard deviation: ", (len(datawithin3std)*100/ len(heightlist)))
graph=ff.create_distplot([df["Height"].tolist()], ["Heightdistribution"], show_hist=False)
graph.add_trace(go.Scatter(x=[meanheight, meanheight], y=[0, 0.035], mode="lines", name="mean"))
graph.add_trace(go.Scatter(x=[stdev1start, stdev1start], y=[0, 0.035], mode="lines", name="mean"))
graph.add_trace(go.Scatter(x=[stdev1end, stdev1end], y=[0, 0.035], mode="lines", name="mean"))
graph.add_trace(go.Scatter(x=[stdev2start, stdev2start], y=[0, 0.035], mode="lines", name="mean"))
graph.add_trace(go.Scatter(x=[stdev2end, stdev2end], y=[0, 0.035], mode="lines", name="mean"))
graph.add_trace(go.Scatter(x=[stdev3start, stdev3start], y=[0, 0.035], mode="lines", name="mean"))
graph.add_trace(go.Scatter(x=[stdev3end, stdev3end], y=[0, 0.035], mode="lines", name="mean"))
graph.show()
