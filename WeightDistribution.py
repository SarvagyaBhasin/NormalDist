import pandas as pd
import csv 
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics

df=pd.read_csv("HeightWeight.csv")
weightlist=df["Weight"].tolist()
meanweight=statistics.mean(weightlist)
modeweight=statistics.mode(weightlist)
medianweight=statistics.median(weightlist)
stdevweight=statistics.stdev(weightlist)
print("Mean: ", meanweight)
print("Mode: ", modeweight)
print("Median: ", medianweight)
print("Standard Deviation: ", stdevweight)
stdev1start, stdev1end=meanweight-stdevweight, meanweight+stdevweight
stdev2start, stdev2end=meanweight-2*stdevweight, meanweight+2*stdevweight
stdev3start, stdev3end=meanweight-3*stdevweight, meanweight+3*stdevweight
datawithin1std=[result for result in weightlist if result>stdev1start and result<stdev1end]
datawithin2std=[result for result in weightlist if result>stdev2start and result<stdev2end]
datawithin3std=[result for result in weightlist if result>stdev3start and result<stdev3end]
print("percentage of data within 1st standard deviation: ", (len(datawithin1std)*100/ len(weightlist)))
print("percentage of data within 2nd standard deviation: ", (len(datawithin2std)*100/ len(weightlist)))
print("percentage of data within 3rd standard deviation: ", (len(datawithin3std)*100/ len(weightlist)))
graph=ff.create_distplot([df["Weight"].tolist()], ["Weightdistribution"], show_hist=False)
graph.add_trace(go.Scatter(x=[meanweight, meanweight], y=[0, 0.035], mode="lines", name="mean"))
graph.add_trace(go.Scatter(x=[stdev1start, stdev1start], y=[0, 0.035], mode="lines", name="mean"))
graph.add_trace(go.Scatter(x=[stdev1end, stdev1end], y=[0, 0.035], mode="lines", name="mean"))
graph.add_trace(go.Scatter(x=[stdev2start, stdev2start], y=[0, 0.035], mode="lines", name="mean"))
graph.add_trace(go.Scatter(x=[stdev2end, stdev2end], y=[0, 0.035], mode="lines", name="mean"))
graph.add_trace(go.Scatter(x=[stdev3start, stdev3start], y=[0, 0.035], mode="lines", name="mean"))
graph.add_trace(go.Scatter(x=[stdev3end, stdev3end], y=[0, 0.035], mode="lines", name="mean"))
graph.show()