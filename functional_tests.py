from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_lits_and_retrieve_it_later(self):
        # Edith heard about a cool new online to-do app. She goes to check
        # out its homepage
        self.browser.get('http://localhost:8001')

        # She is invited to enter a todo item straight away
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)

        # When she hits enter, the page updates ,and now the page lists
        # "1: Buy Peacock feathers to make a fly" (Edith is ery methodical)

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remmeber her list. Then she sees
        # that the site has generated a unique URL for her -- ther is some explanatory
        # text to that effect. 

        # She visits that URL - her to-do list is still there. 

        # Satisfied, she goes back to sleep. 

if __name__ == '__main__':
    unittest.main(warnings='ignore')
