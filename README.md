# Overview

## NER
- Named Entity Recognition (NER) is a subfield of Natural Language Processing (NLP) that identifies and extracts entities such as people, organizations, and locations from unstructured text. 
- Semantic search is a search technique that uses machine learning algorithms to understand the meaning of words in a query and the context in which they are used. 
- NER semantic search combines these two techniques to enable more accurate and relevant search results by identifying and extracting named entities from the query and using them to filter and search only through records containing these named entities
    - its inputs are:
        - query: the end user's query
    - its outputs are:
        - relevant documents: documents that match the end user's query based upon Named Entity Recognition matches between the input query and stored documents


# NER Semantic Search Lab

## Files to Modify
The code you should modify, as well as the instructions for completing the lab, are in ```src/main/lab.py```. The lab module contains a main section you may use to manually test your code. You should not modify ```src/test/lab_test.py```. You must pass all test cases provided in tests/lab_test.py to pass the lab.

## Notes and Resources
This lab uses a locally downloaded LLM, so the first time you run your tests or manually execute the lab module there may be down time while the model is downloaded.