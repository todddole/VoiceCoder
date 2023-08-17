class Code_Edit():
    def process_text_for_code(self):
        statement=""
        code=""
        words=self.__code.split()
        for i in range(len(words)):
            if (statement=="" and words[i] in ["if", "for", "def", "class", "while"]):
                statement=words[i]
                code=words[i] + " "
                if words[i] in ["if", "while"]:
                    code=code+"("

            elif (len(words[i])==1 and words[i].isalpha()):
                code=code+words[i]
            else :
                code=code+" "+words[i]

            if words[i] in ["equals", "equal", "is"]:
                pass

        if statement in ["if", "while"]:
            code=code+"):"

        code+="\n"
        self.__code=code


    def __init__(self, txt):
        self.__txt = txt.lower()
        self.__code=""
        if ("add " in self.__txt[0:4]):
            self.__command = "add"
            self.__code= self.__txt.replace("add ", "")
            self.process_text_for_code()
            print(self.__command + " " + self.__code)

    def get_text(self):
        return self.__txt

    def get_code(self):
        return self.__code




