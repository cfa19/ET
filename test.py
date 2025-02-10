import unittest
import os
import pandas as pd
import csv
from ET import evaluate
import openai

class TestEvaluateFunction(unittest.TestCase):
    def setUp(self):
        self.test_input = 'tickets.csv'
        self.test_output = 'tickets_evaluated.csv'
        self.test_data = [
            {'ticket': 'How to install Python?', 'reply': 'You can download Python from the official website.'},
            {'ticket': 'What is OpenAI?', 'reply': 'OpenAI is a research company focused on AI.'}
        ]
        
        with open(self.test_input, 'w', newline='') as file:
            fieldnames = ['ticket', 'reply']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.test_data)


    def test_evaluate_function(self):
        tickets_df = pd.read_csv(self.test_input)
        self.assertEqual(len(tickets_df), 2)

        tickets_df['content_score'], tickets_df['content_explanation'], tickets_df['format_score'], tickets_df['format_explanation'] = zip(*tickets_df.apply(
            lambda row: evaluate(row['ticket'], row['reply']), axis=1))

        tickets_df.to_csv(self.test_output, index=False)

        output_df = pd.read_csv(self.test_output)
        self.assertEqual(len(output_df), 2)
        self.assertIn('content_score', output_df.columns)
        self.assertIn('format_score', output_df.columns)

    def tearDown(self):
        if os.path.exists(self.test_input):
            os.remove(self.test_input)
        if os.path.exists(self.test_output):
            os.remove(self.test_output)

if __name__ == '__main__':
    unittest.main()