import csv
import sys
import matplotlib.pyplot as plt
import datetime

def main():
    with open('bottlescsv.csv') as csv_file:
        x = []
        y = []
        pair = []
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            pair.append(list(line[i] for i in range(2)))
        for i in pair:
            x.append(i[0])
            y.append(i[1])
        x = [datetime.datetime.strptime(d, "%d/%m/%Y").date() for d in x]
        print(x[0])
        print(y)
        plt.plot_date(x,y, linestyle = 'solid', marker = 'x', linewidth = 1)

if __name__ == '__main__':
    print('Running main program')
    main()