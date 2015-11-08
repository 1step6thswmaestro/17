from functional_tests.base import FunctionalTest


class SearchTest(FunctionalTest):
    fixtures = ['users.json', 'team_data.json', 'message_data.json', 'team_list.json']

    def timeout(self, time_to_sleep):
        import time
        time.sleep(time_to_sleep)

    def test_search(self):
        self.login()
        self.create_issues()
        self.browser.find_element_by_id('id_content').send_keys('test contents')
        self.browser.find_element_by_id('btn_search').click()
        search_1 = self.browser.find_element_by_id('Test-Issue-01')
        search_2 = self.browser.find_element_by_id('Test-Issue-02')
        self.assertEqual(search_1.text, 'Test-Issue-01')
        self.assertEqual(search_2.text, 'Test-Issue-02')

        self.browser.find_element_by_id('Test-Issue-01').click()

        div = self.browser.find_element_by_class_name('sorted_issues')
        issue_channels = div.find_elements_by_tag_name('a')
        issue_1 = issue_channels[0]
        url_regex_str = '/issue/.+'

        self.assertRegex(issue_1.get_attribute('href'), url_regex_str)

        self.timeout(2)