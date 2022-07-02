import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df=pd.read_csv("data5.csv")

data=df["temp"].tolist()
mean=statistics.mean(data)
print("populationmean: ",mean)




def randomsetofmeans(counter):
  dataset=[]
  for i in range (0,counter):
    random_index= random.randint(0,len(data)-1) 
    value = data[random_index] 
    dataset.append(value)

  mean=statistics.mean(dataset)
  return mean

def showfig(meanlist):
  df=meanlist
  mean=statistics.mean(df)
  fig=ff.create_distplot([df],["means"],show_hist=False)
  fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines"))
  fig.show()

def setup():
  meanlist=[]
  for i in range (0,1000):
    setofmeans=randomsetofmeans(100)
    meanlist.append(setofmeans)
  samplemean=statistics.mean(meanlist)
  showfig(meanlist)
  print(samplemean)

setup()