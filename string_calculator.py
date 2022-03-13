import re


class StringCalculator():
    """
    Contains functions to add numbers from 
    string (which may contain custom delimiters and new lines) by cleaning it up
    """

    def Add(self, string: str):
        """Add numbers from a given string of numbers and delimiter

        Args:
            string (str): string containing numbers and delimiter

        Raises:
            Exception: When negative numbers are detected
            Exception: When different character is detected for addition in place of numbers

        Returns:
            int: sum of the numbers in the string
        """
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
                    elif int(character) <= 1000:
                        summation += int(character)
                if negative_numbers:
                    raise Exception("Negative numbers detected: {}".format(negative_numbers))

            except ValueError:
                raise Exception("Character different from numbers detected! please insert numbers for the addition")
            return summation

    
    def cleanup_the_string(self, string: str):
        """clean up the string containing new lines and custom delimiter

        Args:
            string (str): string that may contain new lines and custom delimiters

        Returns:
            str: cleaned up string which contains only integers with default delimiter i.e. ','
        """
        clean_string = string
        if string.startswith("//"):
            clean_string = self.allow_custom_delimiter(clean_string)
        clean_string = clean_string.replace("\n", ",")
        return clean_string


    def allow_custom_delimiter(self, string: str):
        """Replaces custom delimiters with default delimiter i.e. ','

        Args:
            string (str): string containing custom delimiters

        Returns:
            str: string with replaced custom delimiters and no // in start index
        """
        custom_delimiter, summation_string = string.split("\n", 1)
        delimiters = re.findall(r'\[.*?\]', custom_delimiter[2:])
        if delimiters:
            for d in delimiters:
                delm = d.replace("[", "").replace("]","")
                summation_string = summation_string.replace(delm, ",")
        else:
            summation_string = summation_string.replace(custom_delimiter[2:], ",")
        return summation_string
