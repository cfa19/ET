import os
import pandas as pd
import csv
import pytest
from ET import evaluate

@pytest.fixture
def create_test_files():
    test_input = 'tickets.csv'
    test_output = 'tickets_evaluated.csv'
    test_data = [
        {'ticket': 'How to install Python?', 'reply': 'You can download Python from the official website.'},
        {'ticket': 'What is OpenAI?', 'reply': 'OpenAI is a research company focused on AI.'}
    ]

    with open(test_input, 'w', newline='') as file:
        fieldnames = ['ticket', 'reply']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(test_data)

    yield test_input, test_output

    if os.path.exists(test_input):
        os.remove(test_input)
    if os.path.exists(test_output):
        os.remove(test_output)

def test_evaluate_function(create_test_files):
    test_input, test_output = create_test_files
    tickets_df = pd.read_csv(test_input)
    assert len(tickets_df) == 2

    tickets_df['content_score'], tickets_df['content_explanation'], tickets_df['format_score'], tickets_df['format_explanation'] = zip(*tickets_df.apply(
        lambda row: evaluate(row['ticket'], row['reply']), axis=1))

    tickets_df.to_csv(test_output, index=False)

    output_df = pd.read_csv(test_output)
    assert len(output_df) == 2
    assert 'content_score' in output_df.columns
    assert 'format_score' in output_df.columns
