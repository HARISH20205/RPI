import nltk
from nltk import word_tokenize, pos_tag, ne_chunk, sent_tokenize

#took from perplexity, if anyone can just comment each meaning, and say how its different from our previous thing
def calculate_ttr(prompt):
    tokens = word_tokenize(prompt.lower())
    unique_tokens = set(tokens)
    return len(unique_tokens) / len(tokens)

def advanced_tokenization(prompt):
    word_tokens = word_tokenize(prompt)
    pos_tags = pos_tag(word_tokens)
    
    noun_count = sum(1 for _, tag in pos_tags if tag.startswith('NN'))
    verb_complexity = sum(1 for _, tag in pos_tags if tag.startswith('VB'))
    
    return noun_count, verb_complexity

def enhanced_syntax_complexity(prompt):
    tokens = word_tokenize(prompt)
    pos_tags = pos_tag(tokens)
    
    subordinate_clauses = sum(1 for _, tag in pos_tags if tag in {'IN', 'WDT', 'WRB'})
    complex_noun_phrases = sum(1 for _, tag in pos_tags if tag in {'NNP', 'NNPS'})
    
    return subordinate_clauses + complex_noun_phrases

def classify_prompt_complexity(prompt):
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

    # Count named entities
    entity_count = sum(1 for chunk in ner_tree if hasattr(chunk, 'label'))

    if entity_count == 0:
        ner_complexity = "Low"
    elif entity_count <= 3:
        ner_complexity = "Mid"
    else:
        ner_complexity = "High"

    # Syntactic Complexity Calculation
    conj_count = sum(1 for word, tag in pos_tags if tag in {'CC'})
    sub_clause_count = sum(1 for word, tag in pos_tags if tag in {'IN', 'TO'})

    sentences = sent_tokenize(prompt)
    num_sentences = len(sentences)
    avg_sentence_length = len(tokens) / num_sentences if num_sentences > 0 else 0

    complexity_score = (
        conj_count + sub_clause_count + (1 if avg_sentence_length > 12 else 0)
    )

    if complexity_score == 0:
        syntax_complexity = "Low"
    elif 1 <= complexity_score <= 2:
        syntax_complexity = "Mid"
    else:
        syntax_complexity = "High"

    # New Metrics
    ttr = calculate_ttr(prompt)
    noun_count, verb_complexity = advanced_tokenization(prompt)
    syntax_score = enhanced_syntax_complexity(prompt)

    # Weighted Majority Logic
    weights = {
        "Low": 0,
        "Mid": 2,
        "High": 4
    }

    total_score = (
        weights[length_complexity] * 1 +
        weights[ner_complexity] * 2 +
        weights[syntax_complexity] * 3
    )

    # Incorporate new metrics
    if ttr > 0.7:
        total_score += 2
    if noun_count > 5:
        total_score += 1
    if syntax_score > 3:
        total_score += 2

    # Final Complexity Classification
    if total_score <= 4:
        majority_complexity = "Low"
    elif 5 <= total_score <= 8:
        majority_complexity = "Mid"
    else:
        majority_complexity = "High"

    print(f"Length: {length_complexity} | NER: {ner_complexity} | Syntactic: {syntax_complexity}")
    print(f"Type-Token Ratio: {ttr:.2f} | Noun Count: {noun_count} | Syntax Score: {syntax_score}")
    print(f"Majority Complexity: {majority_complexity}\n")
    
    return majority_complexity