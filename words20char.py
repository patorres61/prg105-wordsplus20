# This program will read a text file of words and print out any words that have over 20 characters not including white space

# Define variables
length = 0
Less20Cnt = 0
word20 = 0
totalWords = 0

# Define input file
fin = open('words.txt')

print ('Words Greater Than 20 characters Omitting Blank Spaces\n')
# Read file, check character count in each line
for line in fin:
    word = line.strip()     # line.strip will strip out any blank spaces
    totalWords += 1         # increment count for total words in file
    length = len(word)      # get length of word
    if length > 20:
        print word
        word20 += 1
    else:
        Less20Cnt += 1

print ('\nTotal number of words in file: ' + str(totalWords))
print ('\nTotal words in file greater than 20 characters omitting blank spaces: ' + str(word20))
print ('\nTotal words in file less than or equal to 20 characters omitting blank spaces: ' + str(Less20Cnt))
