def main():
    wordDictionary={
        "C++": "Programming language",
        "Flutter":"Framework from Goolge",
        "JavaScript": "Programming Language from Meta",
    }
    while True:
        word=input("Enter The Word : \n")
        if word=="":
            break
        if word in wordDictionary :
            print(f"{word} : {wordDictionary[word]}")

main()