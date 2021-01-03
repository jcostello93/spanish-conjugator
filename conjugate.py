import json

with open('./verbs.json') as f:
  data = json.load(f)

ORDER = [
    ['Indicative', 'Subjunctive', 'Imperative Affirmative', 'Imperative Negative', None],
    ['Present', 'Future', 'Conditional', 'Imperfect', 'Preterite', 'Gerund', 'Pastparticiple'],
    ['yo', 'tú', 'él/ella/usted', 'nosotros/nosotras', 'ellos/ellas/ustedes', None]
]

verb = input("What verb would you like to conjugate?: ")
print(f"https://en.wiktionary.org/wiki/{verb}#Spanish")
mode = input("\n1. Sorted\n2. Random\nPick a mode: ")

def get_conjugations(data):
    result = []
    for word, entry in data.items():
            for e in entry:
                if e.get('infinitive') == verb or e.get('verb') == verb:
                    result.append({
                        'conjugated_form': word,
                        'subject': e.get('performer'),
                        'mood': e.get('mood'),
                        'translation': e.get('translation'),
                        'tense': e.get('tense'),
                    })
    return result

def is_skippable(c):
    return (c['subject'] == 'vosotros/vosotras') or (c['mood'] == 'Subjunctive' and c['tense'] == 'Future')
    
def print_random(conjugations):
    for c in conjugations:
        if not is_skippable(c):
            print(f"\nMood: {c['mood']}\nTense: {c['tense']}\nSubject: {c['subject']}")
            input("...")
            print(f"{c['conjugated_form']}\n")

def find_verb(mood, tense, subject, conjugations):
    for c in conjugations:
        if c.get('mood') == mood and c.get('tense') == tense and c.get('subject') == subject:
            return c

def remove_extra_d(conjugations):
    for c in conjugations:
        if (c['mood'] == 'Imperative Affirmative' or c['mood'] == 'Imperative Negative') and c['conjugated_form'][-1] == 'd':
            c['conjugated_form'] = c['conjugated_form'][:-1]

def print_sorted(conjugations):
    for i in range(0, len(ORDER[0])):
        for j in range(0, len(ORDER[1])):
            for k in range(0, len(ORDER[2])):
                    c = find_verb(ORDER[0][i], ORDER[1][j], ORDER[2][k], conjugations)
                    if c and not is_skippable(c):
                        print(f"\nMood: {c['mood']}\nTense: {c['tense']}\nSubject: {c['subject']}")
                        input("...")
                        print(f"{c['conjugated_form']}\n")

conjugations = get_conjugations(data)
remove_extra_d(conjugations)

if mode == '1':
    print_sorted(conjugations)
else:
    print_random(conjugations)

