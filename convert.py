import collections
import re

language = {
    "source": "English",
    "target": "Ladino"
}

translate_from = {
    "target": collections.defaultdict(list),
    "source":  collections.defaultdict(list),
}

filename="dictionary.txt"
with open(filename) as fh:
    for line in fh:
        line = line.rstrip()
        target, source = line.split('<=>')
        target = target.strip(" ")
        source = source.strip(" ")
        translate_from["target"][target].append(source)
        translate_from["source"][source].append(target)

data = """Skill:
  Name: Generated
  Id: 225
  Comment: This file is generated from the dictionary.txt. Do NOT edit this files!

New words: []
Phrases: []
Mini-dictionary:
"""

with open('course/words/skills/generated.yaml', 'w') as fh:
    fh.write(data)

    for origin in ["source", "target"]:
        fh.write(f"  {language[origin]}:\n")
        for word in sorted(translate_from[origin].keys()):
            cleaned_word = re.sub(r' *\(.*', '', word)
            fh.write(f"    - {cleaned_word}:\n")
            for translation in sorted(translate_from[origin][word]):
                fh.write(f"      - {translation}\n")

