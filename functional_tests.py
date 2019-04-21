from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_lits_and_retrieve_it_later(self):
        # Edith heard about a cool new online to-do app. She goes to check
        # out its homepage
        self.browser.get('http://localhost:8002')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a todo item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_atttribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates ,and now the page lists
        # "1: Buy Peacock feathers to make a fly" as an item in the to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # There is still a text box inbitin her to add antoher item. She
        # enters "Use peacock feathers to make a fly" (Edith is ery methodical)
        self.fail('Finish the test!')

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remmeber her list. Then she sees
        # that the site has generated a unique URL for her -- ther is some explanatory
        # text to that effect. 

        # She visits that URL - her to-do list is still there. 

        # Satisfied, she goes back to sleep. 

if __name__ == '__main__':
    unittest.main(warnings='ignore')
