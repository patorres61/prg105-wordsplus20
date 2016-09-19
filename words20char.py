# This program will read a text file of words and print out any words that have over 20 characters not including white space

# Define variables
length = 0
count = 1
word20 = 0

# Define input file
fin = open('words.txt')

# Read input file
fin.readline()

print ('Words Greater Than 20 characters Omitting Blank Spaces\n')
# Read file, check character count in each line
for line in fin:
    word = line.strip()     # line.strip will strip out any blank spaces
    length = len(word)      # get length of word
    if length > 20:
        print word
        word20 += 1
    else:
        count += 1

print ('\nTotal number of words in file: ' + str(word20+count))
print ('\nTotal number of words in file greater than 20 characters omitting blank spaces: ' + str(word20))
print ('\nTotal number of words in file less than or equal to 20 characters omitting blank spaces: ' + str(count))
