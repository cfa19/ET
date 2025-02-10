import unittest
import os
import csv


def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]



def write_csv(file_path, data):
    with open(file_path, 'w', newline='') as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
        
        

class TestCSVFunctions(unittest.TestCase):
    def setUp(self):
        self.test_input = 'test_input.csv'
        self.test_output = 'test_output.csv'
        self.test_data = [
            {'ticket': 'How to install Python?', 'reply': 'You can download Python from the official website.'},
            {'ticket': 'What is OpenAI?', 'reply': 'OpenAI is a research company focused on AI.'}
        ]


        with open(self.test_input, 'w', newline='') as file:
            fieldnames = ['ticket', 'reply']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.test_data)


    def test_read_csv(self):
        data = read_csv(self.test_input)
        self.assertEqual(len(data), 2)  
        self.assertEqual(data[0]['ticket'], 'How to install Python?')  
        self.assertEqual(data[1]['reply'], 'OpenAI is a research company focused on AI.') 



    def test_write_csv(self):
        write_csv(self.test_output, self.test_data)
        with open(self.test_output, 'r') as file:
            reader = csv.DictReader(file)
            result_data = [row for row in reader]
        self.assertEqual(len(result_data), 2)  
        self.assertEqual(result_data[0]['ticket'], 'How to install Python?')  
        self.assertEqual(result_data[1]['reply'], 'OpenAI is a research company focused on AI.')  



    def tearDown(self):
        if os.path.exists(self.test_input):
            os.remove(self.test_input)
        if os.path.exists(self.test_output):
            os.remove(self.test_output)

if __name__ == '__main__':
    unittest.main()
