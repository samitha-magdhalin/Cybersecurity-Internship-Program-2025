from confusable_homoglyphs import confusables

def generate_homograph(domain: str):
    homograph = ""
    for char in domain:
        matches = confusables.is_confusable(char, greedy=True)
        if matches and 'homoglyphs' in matches[0] and len(matches[0]['homoglyphs']) > 0:
            # Extract the actual homoglyph character (it’s inside a dict)
            homoglyph_char = matches[0]['homoglyphs'][0].get('c', char)
            homograph += homoglyph_char
        else:
            homograph += char
    return homograph
