import csv
import sys
import matplotlib.pyplot as plt

def main():
    with open('bottlescsv.csv') as csv_file:
        x = []
        y = []
        pair = []
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            pair.append(list(line[i] for i in range(2)))
        print(pair)
        for i in pair:
            x.append(i[0])
            y.append(i[1])
        print(x)
        print(y)
        plt.plot()

if __name__ == '__main__':
    print('Running main program')
    main()