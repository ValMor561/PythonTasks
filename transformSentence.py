"""
There is a sentence that consists of space-separated strings of upper and lower case English letters. 
Transform each string according to the given algorithm and return the new sentence.

Each string should be modified as follows:
- The first character of the string remains unchanged
- For each subsequent character, say x, consider a letter preceding it, say y:
    - If y precedes x in the English alphabet, transform x to uppercase
    - If x precedes y in the English alphabet, transform x to lowercase
    - If x and y are equal, the letter remains unchanged    
"""

def transformSentence(sentence):
    arr = sentence.split(" ")
    count = len(arr)
    for i in range(0, count):
        n = len(arr[i])
        arr[i] = list(arr[i])
        for j in range(1, n):
            if arr[i][j].lower() > arr[i][j - 1].lower():
                arr[i][j] = arr[i][j].upper()
            if arr[i][j].lower() < arr[i][j - 1].lower():
                arr[i][j] = arr[i][j].lower()
        arr[i] = ''.join(arr[i])
    sentence = " ".join(arr)
    return sentence

if __name__ == '__main__':
    sentence = input()

    result = transformSentence(sentence)
    print(result)
