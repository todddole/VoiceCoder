from voiceout import print_say, speak_text
from voicein import voice_to_text
from codeedit import Code_Edit
from pynput.keyboard import Key, Controller
from word2number import w2n


def process_text_for_code(txt):
    txt = txt.replace("equals", "==")
    return txt

def process_typemode(keyboard, txt):
    print("In process_typemode, txt = "+txt)

    shifton=False

    txt = txt.replace("end parentheses", "endparentheses").lower()
    txt = txt.replace("end bracket", "endbracket")
    txt = txt.replace("end curly", "endcurly")
    txt = txt.replace("greater equals", "greaterequals")
    txt = txt.replace("less equals", "lessequals")
    txt = txt.replace("single quote", "singlequote")

    words = txt.split()

    #Check if the word "repeat" appears.  If so, parse the number after it, and repeat the word after that that many times
    #eg "repeat five down" becomes "down down down down down"
    if "repeat" in txt:

        for i in range(len(words)):
            if words[i]=="repeat":
                if words[i+1].isalpha():
                    #number of times to repeat is a word
                    try:
                        count = w2n.word_to_num(words[i+1])
                    except ValueError:
                        print("Repeat failed on word "+words[i+1])
                        raise ValueError
                elif words[i+1].isnumeric():
                    #number of times to repeat is a number
                    count = int(words[i+1])
                elif words[i+1].isalnum():
                    #text garbled such as "5A"
                    for k in range(len(words[i+1])):
                        if words[i+1][k].isalpha():
                            print("In isalpha block, k = "+str(k))
                            print("words[i+1][:k] = " + words[i+1][:k])
                            words[i+1] = words[i+1][:k] + " " + words[i+1][k:-1]
                            print("words[i+1] now = " + words[i+1])
                            tempwords = words[i+1].split()
                            words[i+1] = tempwords[0]
                            if (len(words)<i+2):
                                words.insert(i+2, tempwords[1])
                            else:
                                words.append(tempwords[1])
                            break
                else:
                    raise ValueError

                repeatword = words[i+2]
                for j in range(count-1):
                    words.insert(i+2, repeatword)
                del words[i+1]
                del words[i]
                break



    for word in words:

        if (len(word)==1):
            keyboard.type(word)
            print("Printing "+word)
        elif (word=="space"):
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif (word=="tab"):
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
        elif (word=="enter"):
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        elif (word=="backspace"):
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
        elif (word=="endparentheses"):
            keyboard.type(")")
        elif (word=="parentheses"):
            keyboard.type("(")
        elif (word=="bracket"):
            keyboard.type("[")
        elif (word=="endbracket"):
            keyboard.type("]")
        elif (word=="curly"):
            keyboard.type("{")
        elif (word=="endcurly"):
            keyboard.type("}")
        elif (word=="equals"):
            keyboard.type("=")
        elif (word=="plus"):
            keyboard.type("+")
        elif (word=="minus"):
            keyboard.type("-")
        elif (word=="multiply"):
            keyboard.type("*")
        elif (word=="divide"):
            keyboard.type("/")
        elif (word=="greater"):
            keyboard.type(">")
        elif (word=="less"):
            keyboard.type("<")
        elif (word=="greaterequals"):
            keyboard.type(">=")
        elif (word=="lessequals"):
            keyboard.type("<=")
        elif (word=="not"):
            keyboard.type("!")
        elif (word=="ampersand"):
            keyboard.type("&")
        elif (word=="pipe"):
            keyboard.type("|")
        elif (word=="colon"):
            keyboard.type(":")
        elif (word=="semicolon"):
            keyboard.type(";")
        elif (word=="comma"):
            keyboard.type(",")
        elif (word=="dot"):
            keyboard.type(".")
        elif (word=="singlequote"):
            keyboard.type("")
        elif (word=="left"):
            keyboard.press(Key.left)
            keyboard.release(Key.left)
        elif (word=="right"):
            keyboard.press(Key.right)
            keyboard.release(Key.right)
        elif (word=="up"):
            keyboard.press(Key.up)
            keyboard.release(Key.up)
        elif (word=="down"):
            keyboard.press(Key.down)
            keyboard.release(Key.down)
        elif (word=="pass"):
            pass
        elif (word=="shift"):
            if shifton:
                keyboard.release(Key.shift)
                shifton=False
            else:
                keyboard.press(Key.shift)
                shifton=True
        elif (word=="end"):
            keyboard.press(Key.end)
            keyboard.release(Key.end)
        elif (word=="home"):
            keyboard.press(Key.home)
            keyboard.release(Key.home)
        elif (word=="undo"):
            #use the editor's undo function
            keyboard.press(Key.ctrl)
            keyboard.press("z")
            keyboard.release(Key.ctrl)
            keyboard.release("z")
        else:
            keyboard.type(word)




command_list=[]
typemode = False
keyboard = Controller()

while True:
    print('Python is listening...')
    inp=voice_to_text()
    print(inp)
    if (typemode==False): command_list.append(Code_Edit(inp))



    if inp == "stop listening":
        print("Goodbye!")
        break

    elif inp == "type mode":
        typemode = True
        print("Type mode activated")

    elif inp == "end type mode" or inp == "command mode":
        typemode = False
        print("Type mode deactivated")

    else:
        if typemode == True:
            try:
                process_typemode(keyboard, inp)
            except:
                print("Failed to process "+inp)


        else:
            pass




for comd in command_list:
    print(comd.get_code())


#file = open("main.py","a")
#file.write("print('Hello World')\n")
#file.close()



