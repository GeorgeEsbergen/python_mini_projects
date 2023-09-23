# Word Replacement Program 


def word_replacement():
    str ="This string is to replace any word "
    print(str)

    selectWord = input("Enter the Word you want to replace")
    newWord = input("Enter the New Word")
    
    print(str.replace(selectWord,newWord))  


word_replacement()
