dead_words = [
    ["you", 0],
    ["a lot", 0],
    ["lots", 0],
    ["also", 0],
    ["awesome", 0],
    ["cool", 0],
    ["rad", 0],
    ["awful", 0],
    ["but", 0],
    ["fun", 0],
    ["funny", 0],
    ["got", 0],
    ["get", 0],
    ["good", 0],
    ["great", 0],
    ["guy", 0],
    ["have to", 0],
    ["kid", 0],
    ["like", 0],
    ["mad", 0],
    ["nice", 0],
    ["pretty", 0],
    ["scared", 0],
    ["so", 0],
    ["then", 0],
    ["very", 0],
    ["I", 0],
    ["me", 0],
    ["I believe", 0],
    ["I think", 0],
    ["I feel", 0],
    ["kind of", 0],
    ["sort of", 0],
    ["like", 0],
    ["just", 0],
    ["thru", 0],
    ["tons", 0],
    ["stuff", 0],
    ["thing", 0],
    ["things", 0],
    ["wonderful", 0],
    ["neat", 0],
    ["bad", 0],
    ["okay", 0],
    ["ok", 0],
    ["k", 0],
    ["sad", 0],
    ["cause", 0],
    ["big", 0],
    ["small", 0],
    ["little", 0],
    ["gonna", 0],
    ["really", 0],
    ["kinda", 0],
    ["wanna", 0],
    ["hafta", 0],
    ["cuz", 0],
    ["wuz", 0],
    ["shoulda", 0],
    ["coulda", 0],
    ["woulda", 0],
    ["outta", 0],
    ["should of", 0],
    ["would of", 0],
    ["could of", 0],
    ["prolly", 0],
    ["probly", 0],
    ["many", 0],
]
punctuation = ["!", ".", ":", ";", "-", "?"]

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    print("Importing pip. . .")
    import pip
    print("Importing subprocess. . .")
    import subprocess
    print("Importing sys. . . ")
    import sys
    print("Installing colorama. . .")
    install("colorama")
    print("Importing colorama. . .")
    from colorama import Fore, Back, Style, init
    print("Initializing colorama. . .")
    init()
    print("Importing time. . .")
    import time
    print("Importing os. . .")
    import os
    print("Clearing terminal. . .")
    time.sleep(1.5)
    cls()

while True:
    in_quotation, found_dead_word = False, False
    
    print(f"{Style.BRIGHT}Text here:")
    sys.stdout.write(f"{Style.RESET_ALL}")
    user_input = input("\n")
    user_input = user_input.split()
    
    cls()

    for i in range(len(user_input)):
        try:
            word, word_minus_one, next_word, next_word_minus_one = user_input[i], "".join(list(user_input[i])[:len(user_input[i])-1]), user_input[i+1], "".join(list(user_input[i+1])[:len(user_input[i+1])-1])
        except:
            continue
        if '"' in word:
            if in_quotation == True:
                in_quotation = False
            else:
                in_quotation = True
        for dword in dead_words:
            try:
                if dword[0].lower() == word.lower() and in_quotation == False:
                    user_input[i], dword[1] = f"{Back.RED}{word}{Style.RESET_ALL}", dword[1]+1
                elif dword[0].lower() == word.lower()+" "+user_input[i+1].lower() and in_quotation == False:
                    user_input[i], dword[1] = f"{Back.RED}{word} {next_word}{Style.RESET_ALL}", dword[1]+1
                    user_input.remove(next_word)
                elif dword[0].lower() == word_minus_one.lower() and list(word)[-1] in str(punctuation) and in_quotation == False:
                    user_input[i], dword[1] = f"{Back.RED}{word}{Style.RESET_ALL}", dword[1]+1
                elif dword[0].lower() == word.lower()+" "+next_word_minus_one.lower() and list(next_word)[-1] in str(punctuation)  and in_quotation == False:
                    user_input[i], dword[1] = f"{Back.RED}{word} {next_word}{Style.RESET_ALL}", dword[1]+1
                    user_input.remove(next_word)
            except:
                if dword[0].lower() == word.lower() and in_quotation == False:
                    user_input[i], dword[1] = f"{Back.RED}{word}{Style.RESET_ALL}", dword[1]+1
                if dword[0].lower() == word_minus_one.lower() and in_quotation == False:
                    user_input[i], dword[1] = f"{Back.RED}{word}{Style.RESET_ALL}", dword[1]+1
    time.sleep(0.5)
    print(f"{' '.join(user_input)}\n")
    for dword in dead_words:
        if dword[1] != 0:
            print(f"{dword[0].capitalize()}: {dword[1]}")
            found_dead_word = True
            time.sleep(0.1)
    if found_dead_word == False:
        print("No dead words found.\n")
    print(" ")
    qreset = input("(y/n) Reset?    ")
    if "y" in qreset:
        for word in dead_words:
            word[1] = 0
        cls()
        continue
    break
