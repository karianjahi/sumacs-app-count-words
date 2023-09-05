"""
- This is the testing ground for the 
application count-words.
- It serves like a documentation to our code
- It also ensures that any additional feature 
does not break the pre-existing code.
- Tests are the lifeline to any code. Any programmer
who wishes to interact with our application first looks
at the tests to get some idea on what the app is all about
- It is a fact that tests are built sequentially.
- If the code breaks, we know that it is because of the
current adjustment to the code and therefore it is easier 
to debug.
- We always aim to make sure 100% of the code is tested

===============
We use pytest from the terminal to make tests
install it using :
pip install pytest
We use `assert` to compare the result from code with expected result
=================
"""
from count_words import WordCounter
class TestWordCounter: # Test at the beginning very important
    def atest_empty_string(self):
        text = ""
        assert WordCounter().count_words(text) == 0
    
    def atest_one_word(self):
        text = "sumacs"
        assert WordCounter().count_words(text) == 1

    def atest_multiple_words(self):
        text = "testing multiple words"
        assert WordCounter().count_words(text) == 3
    
    def atest_mutiple_words_separated_by_commas(self):
        text = "testing,multiple words"
        assert WordCounter().count_words(text) == 3
    
    def atest_exaggerated_spaces(self):
        text = "testing           multiple     words"
        assert WordCounter().count_words(text) == 3
    
    def atest_html(self):
        text = "<h1> Testing html </h1>"
        assert WordCounter().count_words(text) == 2
    
    def test_html_with_attributes(self):
        text = "<h1 class='sumac'> Testing html </h1>"
        assert WordCounter().count_words(text) == 2
    






