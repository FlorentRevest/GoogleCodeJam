#!/usr/bin/python3
# This function takes a prefix and remainder in the form of "a" & "b(cd)ef" and
# it returns the number of *existing* words that could come from the expanded string

def makeTrie(words):
    root = dict()
    for word in words:
        currentDict = root
        for letter in word:
            currentDict = currentDict.setdefault(letter, {})
    return root

def prefixInTrie(trie, word):
    currentDict = trie
    for letter in word:
        if letter in currentDict:
            currentDict = currentDict[letter]
        else:
            return False
    else:
        return True

def expand (prefix, remainder, existingWords, rootNode):
    found = prefixInTrie(rootNode, prefix)

    if found:
        if len(remainder) == 0:
            return 1
        else:
            i=0
            # Appends 'normal' characters of the begining of the string to the prefix
            # e.g: "b" in "b(cd)ef"
            while i < len(remainder) and remainder[i] != "(" :
                prefix += remainder[i]
                i += 1

            # Creates a list of all elements in a parenthesis
            # e.g: ["c", "d"] in "b(cd)ef"
            i += 1 # Ignores the parenthesis
            lettersToExpand = []
            while i < len(remainder) and remainder[i] != ")" :
                lettersToExpand.append(remainder[i])
                i += 1

            # For each element inside of the parenthesis recursively calls expand
            # e.g: expand("abc", "ef") & expand("abd", "ef") for the previous ex.
            possibilities = 0
            for letter in lettersToExpand:
                possibilities += expand(prefix + letter, remainder[i+1:], existingWords, rootNode)
            if len(lettersToExpand) == 0:
                possibilities += expand(prefix, "", existingWords, rootNode)

            return possibilities
    else:
        return 0

# Get global variables
firstLine = [int(n) for n in input().split()]
wordsLength     = firstLine[0]
existingWordsNb = firstLine[1]
wordsNb         = firstLine[2]

# Populates the existing words tree
existingWords=[]
for index in range(0, existingWordsNb):
    existingWords.append(input())

root = makeTrie(existingWords)

# Print the number of possibilities for every word
for index in range(0, wordsNb):
    print("Case #" + str(index+1) + ": " + str(expand("", input(), existingWords, root)))
