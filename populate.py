import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')

import django
django.setup()
chapters = [
    [1 , 'SENTENCE CONSTRUQTIONS'],
    [2 , 'PARTS OF SPEECH'],
    [3 , 'KINDS OF NOUNS'],
    [4 , 'COUNTABLE AND UNCOUNTABLE NOUNS'],
    [5 , 'THE NOUN - NUMBER'],
    [6 , 'THE NOUN - GENDER '],
    [7 , 'THE NOUN - CASE'],
    [8 , 'MORE ABOUT PRONOUNS'],
    [9 , 'MORE ABOUT ADJECTIVES'],
    [10 , 'MORE ABOUT VERBS AND MODALS'],
    [11 , 'SYNTAX - SUBJECT-VERB AGREEMENT'],
    [12 , 'CONJUGATION OF VERBS'],
    [13 , 'TIME AND TENSE WITH MOOD'],
    [14 , 'VERBAL NOUN, GERUND AND PARTICIPLE'],
    [15 , 'MORE ABOUT ADVERBS AND ADVERBIALS'],
    [16 , 'MORE ABOUT PREPOSITIONS'],
    [17 , 'APPROPRIATE PREPOSITIONS'],
    [18 , 'MORE ABOUT CONJUNCTIONS'],
    [19 , 'ARTICLES AND DETERMINERS'],
    [20 , 'MODIFIERS'],
    [21 , 'STRUCTURAL AND NON-STRUCTURAL WORDS'],
    [22 , 'NARRATION/REPORTING'],
    [23 , 'VOICE CHANGE/DESCRIBING A PROCESS'],
    [24 , 'PHRASES'],
    [25 , 'SENTENCES AND ITS CLAUSES/JOINING/SPLITTING'],
    [26 , 'TRANSFORMATION OF SENTENCES'],
    [27 , 'WH-QUESTIONS'],
    [28 , 'FORMATION OF WORDS/ANTONYMS '],
    [29 , 'WORD FAMILY/ONE PART OF SPEECH TO OTHERS'],
    [30 , 'SAME WORD USED AS DIFFERENT'],
    [31 , 'WORDS COMMONLY CONFUSED'],
    [32 , 'GROUP VERBS/PHRASAL VERBS'],
    [33 , 'IDIOMS '],
    [34 , 'NOMINAL COMPOUNDS'],
    [35 , 'PUNCTUATION AND CAPITALIZATION'],
]
from english_grammar.models import Chapter

def populate():
    for slno, title in chapters:
        Chapter.objects.create(title = title, slno=slno, total_pages=100)


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate()
    print('Populating Complete')
