def word_or_number(words):
    words = words.replace(" ", "")
    print(words) 
    try:
        if int(words):
            return True
    except:
        if words.isalpha():
            return True
        else:
            return False
