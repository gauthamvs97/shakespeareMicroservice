import json
import time

def clean_Word(word):  # function that takes a word and returns only the alphabets in it. Ex: day's -> days, python3 -> python
    only_alpha = ""
    for char in word:
        if ((ord(char) >= 65 and ord(char) <= 90) or ((ord(char) >= 97 and ord(char) <= 122))):
            only_alpha += char.lower()

    return only_alpha

def count_Shakespeare(inputFile):                   #function that is called in views.py

    start_Time = time.time()                        #start time is stored
    n = 0
    with open(inputFile) as f:                      #input file is read and stores in a list, line by line
        lines = [line.strip() for line in f]

    total_Length = len(lines)
    print(total_Length)
    chapters = []
    response = dict()
    processingResult = list()

    cur = 0
    for i in range(cur, total_Length - 1):                               #main content of the shakespeare file starts from line 36
        if (i > 35 and len(lines[i]) > 0 and not lines[i] in chapters):   #extracting and storing each chapter name from index
            chapters.append(lines[i])
        elif (lines[i] in chapters):
            break
        cur = cur + 1
                                                            #starting with the main processing
    for i in range(cur, total_Length - 1):
        if lines[i] in chapters:
            chapterName = lines[i]
            chapInfo = dict()
            print("The chapter is ", lines[i])
            c_UniqueWords = 0
            c_Lines = 0
            word_with_Letter = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0,
                                'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
                                'w': 0, 'x': 0, 'y': 0, 'z': 0}
            unique_Words = []
            for j in range(i + 1, total_Length - 1):
                if (len(lines[j]) < 2):                     #length of line
                    j = j + 1
                elif (lines[j] in chapters):                #next chapter
                    break
                else:
                    c_Lines += 1
                    cur_line = lines[j].split()
                    for cur_word in cur_line:
                        cur_word = clean_Word(cur_word)     # cleaned word with only alphabets
                        if (len(cur_word) < 1):             # if word after cleaning is null,
                            continue

                        c = cur_word[0]                     # for finding words that begin with same characters
                        word_with_Letter[c] += 1

                        if (cur_word not in unique_Words):  # finding unique words and counting
                            unique_Words.append(cur_word)
                            c_UniqueWords += 1
                j += 1

            chapInfo["chapterName "] = chapterName                  #storing info for each entry
            chapInfo["noOfLines"] = c_Lines
            chapInfo["noOfUniqueWords"] = c_UniqueWords
            chapInfo["wordsByCharacter"] = word_with_Letter

            processingResult.append(chapInfo)                       #each entry is added to a list

    end_Time = time.time()
    processingTime = end_Time - start_Time
    print(processingTime)

    response["finalResults"] = processingResult
    response["totalTime"] = processingTime
    print(json.dumps(response))
    return response


