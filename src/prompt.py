import nltk
from nltk import word_tokenize, pos_tag, ne_chunk, sent_tokenize

#can we not load the models up here, as i think everytime the function is called it will download the models - should verify
# nltk.download('punkt') #tokenize the given para into sentences
# nltk.download('averaged_perceptron_tagger') #adds tags to each word in a sentence, for ex ['NLP', 'noun']
# nltk.download('maxent_ne_chunker') #ner of the tags or words in the given sentence
# nltk.download('words') #contains the english word corpus, which we can load here, as of our need
# nltk.download('punkt_tab')
# nltk.download('averaged_perceptron_tagger_eng')
# nltk.download('maxent_ne_chunker_tab')
def classify_prompt_complexity(prompt):
    #nltk.download('punkt') #tokenize the given para into sentences
    #nltk.download('averaged_perceptron_tagger') #adds tags to each word in a sentence, for ex ['NLP', 'noun']
    #nltk.download('maxent_ne_chunker') #ner of the tags or words in the given sentence
    #nltk.download('words') #contains the english word corpus, which we can load here, as of our need
    #nltk.download('punkt_tab')
    #nltk.download('averaged_perceptron_tagger_eng')
    #nltk.download('maxent_ne_chunker_tab')
    # Length Classification
    length = len(prompt.split())
    if length <= 5:
        length_complexity = "Low"
    elif 6 <= length <= 10:
        length_complexity = "Mid"
    else:
        length_complexity = "High"

    # NER Classification using NLTK
    tokens = word_tokenize(prompt)
    pos_tags = pos_tag(tokens)
    ner_tree = ne_chunk(pos_tags)

    # Count named entities (chunked as proper nouns or specific entities)
    entity_count = sum(1 for chunk in ner_tree if hasattr(chunk, 'label'))

    if entity_count == 0:
        ner_complexity = "Low"
    elif entity_count <= 3:
        ner_complexity = "Mid"
    else:
        ner_complexity = "High"

    # Syntactic Complexity Calculation
    conj_count = sum(1 for word, tag in pos_tags if tag in {'CC'})  # Conjunctions
    sub_clause_count = sum(1 for word, tag in pos_tags if tag in {'IN', 'TO'})  # Subordinate clauses

    sentences = sent_tokenize(prompt)
    num_sentences = len(sentences)
    avg_sentence_length = len(tokens) / num_sentences if num_sentences > 0 else 0

    # Calculating the complexity score
    complexity_score = (
        conj_count + sub_clause_count + (1 if avg_sentence_length > 12 else 0)
    )

    if complexity_score == 0:
        syntax_complexity = "Low"
    elif 1 <= complexity_score <= 2:
        syntax_complexity = "Mid"
    else:
        syntax_complexity = "High"

    # Weighted Majority Logic
    weights = {
        "Low": 0,
        "Mid": 2,
        "High": 4
    }

    # Giving higher weight to NER and Syntax
    total_score = (
        weights[length_complexity] * 1 +
        weights[ner_complexity] * 2 +
        weights[syntax_complexity] * 3
    )

    # Final Complexity Classification
    if total_score <= 4:
        majority_complexity = "Low"
    elif 5 <= total_score <= 8:
        majority_complexity = "Mid"
    else:
        majority_complexity = "High"

    #print(f"Prompt : {prompt}")
    print(f"Length: {length_complexity} | NER: {ner_complexity} | Syntactic: {syntax_complexity}")
    #print(f"NER_TREE: {ner_tree}\n")
    #print(f"POS_TAG: {pos_tags}\n")
    print(f"Majority Complexity: {majority_complexity}\n")
    
    return majority_complexity
    #understood
