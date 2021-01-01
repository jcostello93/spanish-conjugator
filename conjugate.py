import json

with open('./verbs.json') as f:
  data = json.load(f)

verb = input("What verb would you like to conjugate?: ")

def get_conjugations(data):
    return [ {
        'conjugated_form': word,
        'subject': entry[0].get('performer'),
        'mood': entry[0].get('mood'),
        'translation': entry[0].get('translation'),
        'tense': entry[0].get('tense'),
    } for word, entry in data.items() if entry[0].get('infinitive') == verb]

def is_skippable(c):
    return (c['subject'] == 'vosotros/vosotras') or (c['mood'] == 'Subjunctive' and c['tense'] == 'Future')
    
def print_conjugations(conjugations):
    for c in conjugations:
        if not is_skippable(c):
            print(f"\nMood: {c['mood']}\nTense: {c['tense']}\nSubject: {c['subject']}")
            input("...")
            print(f"{c['conjugated_form']}\n")

conjugations = get_conjugations(data)
print_conjugations(conjugations)

