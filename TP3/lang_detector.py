def compute_score(reference, target):
    score = 0
    for key,value in target.items():
        if key in reference:
            score += abs(reference[key]- value)
    return score

def detect_lang(references, target):
    dict = {}
    for key,value in references.items():
        dict[key] = compute_score(value,target)
    
    mini = ''
    for key,value in dict.items():
        if  mini == '' or value < dict[mini]:
            mini = key

    return [mini,dict]