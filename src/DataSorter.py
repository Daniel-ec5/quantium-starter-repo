
import csv

class DataSorter:
    def __init__(self, data_url_array):
        self.data = data_url_array

    def sort(self):
        isSorted=False
        sorted_data = []
        c=0
        for item in self.data:
            with open(item, 'r') as f:
                reader = csv.reader(f)
                for line in reader:
                    # skip the first line of the csv file, it containes the column names
                    if c==0:
                        c+=1
                        continue
                    line_formatted={}
                    if 'pink morsel' in line:
                        print('Pink Morsel found in line: ', line)
                        try:
                            # remove the dollar sign from the price and convert it to a float
                            p=0.0
                            for x in line[1]:
                                if x.isdigit() or x=='.':
                                    p=line[1].replace('$','')
                                    p=float(p)
                            q=float(line[2])
                            line_formatted['sales'] = p * q
                            line_formatted['date'] = line[3]
                            line_formatted['region']=line[4]
                            sorted_data.append(line_formatted)
                            print('added to dict')
                        except (ValueError, IndexError):
                            print('Error processing line: ', line)
                            continue
                    else:
                        continue
        # if the sorted data array is not empty, write it to a csv file and return true, else return false
        if len(sorted_data) > 0:
            with open('sorted_data.csv', 'w', newline='') as f:
                headers = sorted_data[0].keys()
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader()
                writer.writerows(sorted_data)
            isSorted=True  
        return isSorted
    