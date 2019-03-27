def read_file():
    with open('./Day 2/input.txt') as my_file:
        read_data = my_file.read()
        return read_data.splitlines() #split by line

#finds number of letters different between 2 words
def numDifferences(word1, word2):
  numDif = 0
  for i, letter in enumerate(word1):
    if word2[i] != letter:
      numDif += 1
  return numDif

#finds similar letters between 2 words
def simLetters(word1, word2):
  letters = ""
  for letter in word1:
    if letter in word2:
      letters += letter
  return letters

def main():
  words = read_file()
  for i, word in enumerate(words):
    for index in range(i + 1, len(words)):
      if numDifferences(word, words[index]) == 1:
        print("Similar letters:", simLetters(word, words[index]))

main()