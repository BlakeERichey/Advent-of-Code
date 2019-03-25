def read_file():
    with open('input.txt') as my_file:
        read_data = my_file.read()
        return read_data.splitlines() #split by line

def main():
    content = read_file()
    numDouble = 0
    numTriple = 0
    for word in content:
        letters = [0 for index in range(0, 26)] #array of letters found in word
        for letter in word:
            letters[ord(letter) - 97] += 1
        if( letters.count(2) > 0 ):
            numDouble += 1
        if( letters.count(3) > 0 ):
            numTriple += 1
    print(numDouble,  numTriple)
    print(numDouble * numTriple) #checksum

main()