
# -*- coding: UTF-8 -*-

import matplotlib.pyplot
import argparse

def avg(results):
    return float(sum(results))/len(results)

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_name')
parser.add_argument('y_axis')
parser.add_argument('title')
parser.add_argument('baseline')

args = parser.parse_args()

f = open(args.input_file, "r")
line = f.readline()
results = {}
while line != '':
    i, t, r = line.split(',')
    i = int(i.strip('id: '))
    t = float(t.strip(' time: '))
    r = int(r.strip(' res: '))
    if i not in results.keys():
        results[i] = []
    results[i].append(r)
    line = f.readline()
    
#print results.keys()
baseline = int(args.baseline)

y = []
y2 = []

for k in results.keys():
    y.append(avg(results[k]))
    y2.append(int(baseline))
    
matplotlib.pyplot.title(args.title)
matplotlib.pyplot.xlabel("Iteracao")
matplotlib.pyplot.ylabel(args.y_axis)
matplotlib.pyplot.plot(y)
#baseline
matplotlib.pyplot.plot(y2)
matplotlib.pyplot.savefig(args.output_name+".png")

matplotlib.pyplot.clf()

for k in range(1, len(y)):
    if y[k-1] > y[k]:
        y[k] = y[k-1]

matplotlib.pyplot.title(args.title + " - Maximo")
matplotlib.pyplot.xlabel("Iteracao")
matplotlib.pyplot.ylabel(args.y_axis+" Maximo")
matplotlib.pyplot.plot(y)
#baseline
matplotlib.pyplot.plot(y2)
matplotlib.pyplot.savefig(args.output_name+"-best.png")

###

    
