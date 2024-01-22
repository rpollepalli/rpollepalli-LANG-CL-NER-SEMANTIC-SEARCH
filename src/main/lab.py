"""
    In this lab you will be using a Named Entity Recognition (NER) model to classify entities in a query and 
    using the detected classificaitons to augument your semantic query to a Chroma database.  NER is a subtask of 
    natural language processing that aims to identify and classify named entities in text into predefined categories 
    such as:
    - person names 
    - organizations
    - locations
    - etc.
    
    NER semantic searches bring the power of a regular semantic search and further refines the results of any
    queries by making use of the detected entities to better determine what data is relevant to the query.
"""

"""
    below is the Chroma collection you will use for this lab: note some of the "documents" already have named 
    entities associated with them
"""
import chromadb
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="lab_collection")
collection.add(
    documents=[
        "Apple has just announced a new product: smart shoes!",
        "I was told an apple a day keeps the doctor away when I was a kid: experience taught me this is not true.",
        "Bass Pro Shop has a new offering: weather resistant sneakers!",
        "When it comes to catching bass I am a pro! I sell them in my shop.",
        "I took George to Washington so we could have dinner at his favorite resturant.",
        "According to my research, George Washington and Napoleon Bonaparte never met"
        
    ],
    metadatas=[
        {
            "id":1,
            'word': 'Apple', 
        },
        {
            "id":2,
        },
        {
            "id":3,
            "organization": "Bass Pro Shop"
        },
        {
            "id":4
        },
        {
            "id":5,
            "person": "George",
            "location": "Washington"
        },
        {
            "id":6,
            "George Washington": True,
            "Napoleon Bonaparte": True
        }
    ],
    ids=["1", "2", "3", "4", "5", "6"]
)


"""
    The first two documents in the collection both reference "apple", but one is clearly a reference to the fruit, and
    the other the company.  The NER model is able to detect the company as a named entity, but a regular semantic
    search runs the risk of grabbing both documents with a query. Take the following example:
"""

query = "Is Apple a good brand?"

"""
    The question is about Apple the company, but query it to the Chroma database and see what happens
"""
results = collection.query(query_texts=[query], n_results=2)
docs_retrieved = results["documents"]
number_of_docs = len(docs_retrieved[0])
# print(number_of_docs)

"""
    The query returns both the fruit and company documents, the former of which is not relevant to the query.
    To help guide the search we can use a NER trained model to provide more detailed entity information to
    our query in order to refine the search results. First thing we need to do is load the NER model
"""
from transformers import AutoTokenizer, AutoModelForTokenClassification
ner_model_id = 'dslim/bert-base-NER'
tokenizer = AutoTokenizer.from_pretrained(ner_model_id)
ner_model = AutoModelForTokenClassification.from_pretrained(ner_model_id)

"""
    Once the model is loaded you need to create a pipeline to tokenize and then make entity predictions from
    the tokens. the bert model is able to handle both of these tasks
"""
from transformers import pipeline
ner_pipeline = pipeline("ner", model=ner_model, tokenizer=tokenizer)

"""
    Now you can pass your query into the NER pipeline and get a list of entities within your query. Save the
    results to a variable and you can check the entity data retrieved from the pipeline (note: it can take some
    time for the pipeline to complete its job). You can ignore the weights warning that triggers before printing
    the results of the pipeline operation
"""

entities = ner_pipeline(query)

# print(entities)

"""
    In this case, one entity was detected in the query and its data saved to a dictionary. We now have all the
    pieces we need to augment the query to the Chroma database
"""

results = collection.query(query_texts=[query], n_results=2, where={"word": entities[0]["word"]})
docs_retrieved = results["documents"]
number_of_docs = len(docs_retrieved[0])
# print(number_of_docs, docs_retrieved[0])

"""
    The results of the query have now been filtered to only include the Apple company document.
    
    Use what you have learned from the code above to implement the incomplete functions below. Make use of the 
    Chroma collection above to complete the lab
"""

def create_ner_pipeline():
    """
        Create an NER pipeline that can be used to extract entities from a query. You will use this method to
        initialize your NER pipeline for the rest of the lab
    """
    # TODO: implement the NER pipeline and return it from the function
    raise RuntimeError("create_ner_pipeline() is not implemented")

def get_Bass_Pro_Shop_company_document() -> list[str]:
    """
        Use the NER pipeline to extract the Bass Pro Shop company name from the query. You will need to
        extract the company name from the query, make sure it is formatted correctly, then filter your
        query to the collection using the correctly formatted company name
        
        The method should return the id of the document and the document itself in a list.
    """
    # TODO: implement the get_Bass_Pro_Shop_company_document() function within the try block. Make sure to
    #       use the create_ner_pipeline() function to create the NER pipeline
    try:
        query = "Does Bass Pro Shop sell anything new?"
        ner_pipe = create_ner_pipeline()
        raise RuntimeError("get_Bass_Pro_Shop_company_document() is not implemented correctly")

    except RuntimeError as e:
        return e
    
def get_George_going_to_dinner_document() -> list[str]:
    """
        Use the NER pipeline to extract the George going to dinner person from the query. You have a choice of
        using the name of the person or the location. Make sure it is formatted correctly, then filter your
        query to the collection using the correctly formatted person or location (you may use both if you wish)

        The method should return the id of the document and the document itself in a list
    """
    # TODO: implement the get_George_going_to_dinner_document() function within the try block. Make sure to
    #       use the create_ner_pipeline() function to create the NER pipeline
    try:
        query = "why do you take George to Washington?"
        ner_pipe = create_ner_pipeline()
        raise RuntimeError("get_George_going_to_dinner_document() is not implemented correctly")
    
    except RuntimeError as e:
        return e

def get_George_Washington_Document() -> list[str]:
    """
        Use the NER pipeline to extract the George Washington document from the query. You will need to
        be careful with formatting your extracted data for filtering the query to the collection. You may
        use one or both names associated with the George Washington document to filter the query.
        
        The method should return the id of the document and the document itself in a list
    """
    # TODO: implement the get_George_Washington_Document() function within the try block. Make sure to
    #       use the create_ner_pipeline() function to create the NER pipeline
    try:
        query = "Did George Washington and Napoleon Bonaparte ever meet?"
        ner_pipe = create_ner_pipeline()
        raise RuntimeError("get_George_Washington_Document() is not implemented correctly")
    
    except RuntimeError as e:
        return e

if __name__ == "__main__":
    # Use this space to test your code
    pass