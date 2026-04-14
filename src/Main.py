import os
from DataSorter import DataSorter
class Main:
    def __init__(self):
        self.data_url_array = []
    def get_data_url_array(self):
        # get all the files in the data folder and add them to the data_url_array
        for file in os.listdir('data'):
            self.data_url_array.append(os.path.join('data', file))
        return self.data_url_array
    def main(self):
        self.get_data_url_array()
        data_sorter = DataSorter(self.data_url_array)
        data_sorted = data_sorter.sort()
        if data_sorted:
            print('Data sorted successfully and saved to sorted_data.json')
        else:
            print('No data to sort')
if __name__ == '__main__':    
    main = Main()
    main.main()