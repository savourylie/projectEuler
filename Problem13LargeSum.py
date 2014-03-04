sum = 0

largeSum_filename = '/Volumes/Lexar128/Dropbox/ProjectEuler/Problem13LargeSum.txt'
largeSum_file = open(largeSum_filename, 'r')
line = largeSum_file.readline()
while line != '':
    sum = sum + int(line)
    line = largeSum_file.readline()
