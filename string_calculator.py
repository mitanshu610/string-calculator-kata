class StringCalculator():

    def Add(self, string: str):
        if not(string and string.strip()):
            return 0
        else:
            cleaned_string = self.cleanup_the_string(string).split(",")
            try:
                summation = 0
                negative_numbers = list()
                for character in cleaned_string:
                    if "-" in character:
                        negative_numbers.append(int(character))
                    else:
                        summation += int(character)
                if negative_numbers:
                    raise Exception("Negative numbers detected: {}".format(negative_numbers))

            except ValueError:
                raise Exception("Character different from numbers detected! please insert numbers for the addition")
            return summation
    
    def cleanup_the_string(self, string: str):
        clean_string = string
        if string.startswith("//"):
            clean_string = self.allow_custom_delimiter(clean_string)
        clean_string = clean_string.replace("\n", ",")
        return clean_string

    def allow_custom_delimiter(self, string: str):
        custom_delimeter, summation_string = string.split("\n", 1)
        temp_string = custom_delimeter[2:]
        custom_string = summation_string.replace(temp_string, ",")
        return custom_string
            
SC = StringCalculator()
print(SC.Add("-1,2,-7,-8,9"))
        