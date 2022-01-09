def inputFileReader(file, array):
    for line in file:
        line = line.strip(" ")
        line = line.strip("ď»ż")
        line = line.strip(")")
        line = line.strip("(")
        values = line.split(",")
        for v in values:
            array.append(int(v))


randomArr = []
reversedArr = []
sortedArr = []

randomArr500K = []

inputFileReader(open("data_source/100kRandom-array.txt", "r"), randomArr)
inputFileReader(open("data_source/100kReversed-array.txt", "r"), reversedArr)
inputFileReader(open("data_source/100kSorted-array.txt", "r"), sortedArr)

inputFileReader(open("data_source/500kRandom-array.txt", "r"), randomArr500K)
