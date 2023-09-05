"""
This piece of code is meant to 
count the no. of words in a string/sentence.
It does this from the terminal.
It therefore requires the user to have some
basic idea about unix environments. 
It is a very basic application.
"""
import re
from bs4 import BeautifulSoup
class WordCounter:
    """
    This is the class whose instances shall
    count words in a string
    """
    def __init__(self):
        """
        This is the class constructor.
        All default attributes and methods
        are define here
        """
        pass

    def __repr__(self):
        """
        This is the class representation.
        What is the class all-about
        """
        return "<word counter>"
    
    def count_words(self, text):
        """
        Here, we implement word count by splitting and 
        calculating the length of the resulting list
        """
        text = BeautifulSoup(text, "html.parser").text
        if text == "":
            return 0
        if "," in text:
            text = re.sub(",", " ", text)
        
        splits = text.split(" ")
        splits = [i for i in splits if i!=""]

        return len(splits)



"""
Create a testing ground for the function
"""
if __name__ == "__main__":
    sentence = "Sumac Imbalance are now doing their final project"
    inst = WordCounter()
    print(inst.count_words(sentence))