class StringCalculator():

    def Add(self, string: str):
        if not(string and string.strip()):
            return 0
        else:
            cleaned_string = self.replace_new_line(string).split(",")
            try:
                result = sum(int(character) for character in cleaned_string)
            except ValueError:
                return "Character different from numbers detected! please insert numbers for the addition"
            return result

    def replace_new_line(self, string: str):
        new_line_replaced_string = string.replace("\n", ",")
        return new_line_replaced_string
    
SC = StringCalculator()
print(SC.Add("a"))