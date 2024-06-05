inputWord = input("Please enter a word to check if it is a palindrome word or not: ")



def split(word):
    lst = []
    for letter in word:
        lst.append(letter)
    reverseLst = []

    for i in range(len(lst)-1,-1,-1):
        print(i)
        reverseLst.append(lst[i])
    
    
    print(lst)
    print(reverseLst)
    lst= ''.join(lst)
    reverseLst = ''.join(reverseLst)
    print(lst)
    print(reverseLst)
    if(lst == reverseLst):
       print("PALINDROME")
    else:
        print("SORRY, IT IS NOT")


split(inputWord.lower())

#faster way
#reverseWord = inputWord[::-1]

#if(inputWord==reverseWord):
#   print("PALINDROME")
#else:
#   print("SORRY, IT IS NOT")