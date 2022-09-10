class Bin(object):
    """ Container for items that keeps a running sum """
    def __init__(self):
        self.items = []
        self.sum = 0

    def append(self, item):
        self.items.append(item)
        self.sum += item

    def __str__(self):
        """ Printable representation """
        return 'Bin(sum=%d, items=%s)' % (self.sum, str(self.items))

    def __eq__(self, other):
        return sum(self.items) == sum(other.items)

    def __lt__(self, other):
        return sum(self.items) < sum(other.items)

    def __gt__(self, other):
        return sum(self.items) > sum(other.items)



def pack(values, maxValue):
    values = sorted(values, reverse=True)
    bins = []

    for item in values:
        # Try to fit item into a bin
        for bin in bins:
            if bin.sum + item <= maxValue:
                #print 'Adding', item, 'to', bin
                bin.append(item)
                break
        else:
            # item didn't fit into any bin, start a new bin
            #print 'Making new bin for', item
            bin = Bin()
            bin.append(item)
            bins.append(bin)

    return bins

def packleastloaded(values, maxValue):
 values = sorted(values, reverse=True)
 #bins = []
 bins= []
 bins.append(Bin())
 while(True):
    for bin in bins:
        bin.items = []
        bin.sum=0
    for item in values:
        # Try to fit item into a bin
        bins = sorted(bins)

        for bin in bins:
            if bin.sum + item <= maxValue:
                #print 'Adding', item, 'to', bin
                bin.append(item)
                break
        else:
            # item didn't fit into any bin, start a new bin
            #print 'Making new bin for', item
            bin = Bin()
            bins.append(bin)
            break
    else:
        break

 return bins

if __name__ == '__main__':
    import random

    def packAndShow(aList, maxValue):
        """ Pack a list into bins and show the result """

        bins = pack(aList, maxValue)

        print('Solution using', len(bins), 'bins:')
        for bin in bins:
            print(bin)

        print()

    def packAndShowLeastLoaded(aList, maxValue):
            """ Pack a list into bins and show the result """

            bins = packleastloaded(aList, maxValue)

            print('Solution using', len(bins), 'bins:')
            for bin in bins:
                print(bin)

            print()

    aList = [70,40,30,20,30,20]
    packAndShow(aList, 100)
    packAndShowLeastLoaded(aList, 100)




    # aList = [ random.randint(1, 11) for i in range(100) ]
    # packAndShow(aList, 11)
