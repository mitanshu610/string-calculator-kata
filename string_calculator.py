class StringCalculator():

    def Add(self, string: str):
        if not(string and string.strip()):
            return 0
        else:
            cleaned_string = self.cleanup_the_string(string).split(",")
            try:
                result = sum(int(character) for character in cleaned_string)
            except ValueError:
                return "Character different from numbers detected! please insert numbers for the addition"
            return result
    
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
    