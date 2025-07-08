#Joe Melia EET-107

def main():
    print("File Processor\n")
    name = input("Enter the name of the file you wish to process: ")
    try:
        file = open(name, "r")
        contents = file.read()
        file.close()
        result = count(contents, name)
        print(result)
    except FileNotFoundError:
        print("\nThe file is either unreachable or doesnt exist")

def count(contents, name,):
    words =len(contents.split())
    letters = 0
    for letter in contents:
        if letter.isupper():
            letters += 1
    result = f"The file {name} contains {words} words of which {letters} of them are capitalized."
    return result

main()
