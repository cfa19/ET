
# Take-Home Assignment: LLM-Based Ticket Reply Evaluation

Objective
You are given a CSV fi le (tickets.csv) containing two columns:
1. ticket – A (fi ctional) customer support ticket message.
2. reply – A response generated by an AI system.
Your task is to use an OpenAI Large Language Model (LLM) (e.g., GPT-4o or o1) to evaluate each reply along two dimensions:
● Content (relevance, correctness, completeness)
● Format (clarity, structure, grammar/spelling)
You will then produce a new CSV containing four additional columns:
1. content_score
2. content_explanation
3. format_score
4. format_explanation
Please use the scoring scale 1-5 for the “_score” fi elds and provide a short textual explanation in each of the “_explanation” fi elds.




## Author

- [@cfa19](https://www.github.com/cfa19)


## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```
    
## Deployment


```bash
Create .env with OpenAI API key:
```


## Usage/Examples

```python
Run: python ET.py
```


## Common Errores
If you get error 429: 

This means you've exceeded your OpenAI API quota. 

