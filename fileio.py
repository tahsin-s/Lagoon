import csv

def getlink(linktype,n):
    with open('links.csv','r') as csvfile:

        reader = csv.reader(csvfile)

        for row in reader:

            if row == []:
                continue

            if row[0] == linktype:
                if len(row) > n:
                    return row[n]
                else:
                    print('Entry',n,'not found in', linktype)
                    return '*Link unvailable*'


    print(linktype, 'not found')
    return '*Link unavailable*'

#test: output 'https://tenor.com/view/laboon-whale-one-piece-spinning-spin-gif-23005705'
#print(getlink('Images',1))