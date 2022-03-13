class StringCalculator():

    def Add(self, string: str):
        if not(string and string.strip()):
            return 0
        else:
            cleaned_string = string.split(",")
            return sum(int(character) for character in cleaned_string)
    
SC = StringCalculator()
print(SC.Add("1,102,5,90"))
