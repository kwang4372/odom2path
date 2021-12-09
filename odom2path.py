import glob
import os
import csv
import matplotlib.pyplot as plt


class odom2path:
    def __init__(self):       
        self.directory = r'C:\Users\kwang\Git\odom2path'
        self.filename = r'C:\Users\kwang\Git\odom2path\data.txt'
        self.seperator = '\t'
        
        self.output = []

    def convertFile(self, filename):
        data = []
                
        with open(filename, 'r') as f:
            csvreader = csv.reader(f, delimiter=self.seperator, quoting=csv.QUOTE_NONNUMERIC)
            for row in csvreader:
                data.append(row)
        
        return data
    
    def convertFolder(self, directory):
        dataset = []
        for filename in os.listdir(directory):
            dataset.append(self.convertFile(directory+'/'+filename))
        
        return dataset
            
    
    def visualize(self, data, save):
        fig = plt.figure()
        fig.set_facecolor('white')
                
        x = []
        y = []
        for row in data:
            x.append(row[0])
            y.append(row[1])
        plt.plot(x, y)
        plt.show()
            
    def visualize_multi(self, dataset, save):
        fig = plt.figure()
        fig.set_facecolor('white')        
        
        x = []
        y = []
        for data in dataset:
            for row in data:
                x.append(row[0])
                y.append(row[1])
            plt.plot(x, y)
            x.clear()
            y.clear()
        
        plt.show()
    
    def convertFolderGroup(self, directory):
        dataset = dict()
        for foldername in os.listdir(directory):            
            data = self.convertFolder(directory+'/'+foldername)       
            dataset[foldername] = data
            
        
        return dataset
    
    def visualize_group(self, dataset, save):
        fig = plt.figure()
        fig.set_facecolor('white')
        plt.xlabel('x[mm]')
        plt.ylabel('y[mm]')        
                
        x = []
        y = []
        for key, datas in dataset.items():
            for data in datas:
                for row in data:
                    x.append(row[0])
                    y.append(row[1])
            plt.plot(x, y, label=key)
            x.clear()
            y.clear()
        
        plt.legend(loc='upper left')
        plt.show()
                
        

converter = odom2path()
# data = converter.convertFile(r'C:\Users\kwang\Git\odom2path\data/1.txt')
# converter.visualize(data, save=False)

# dataset = converter.convertFolder(r'C:\Users\kwang\Git\odom2path\data')
# converter.visualize_multi(dataset, save=False)

dataset = converter.convertFolderGroup(r'C:\Users\kwang\Git\odom2path\data')
converter.visualize_group(dataset, save=False)
