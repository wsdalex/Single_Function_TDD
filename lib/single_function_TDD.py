import math
def calc_reading_time(text):
    word_count = len(text.split())
    time_to_read = math.ceil(word_count / 200)
    if time_to_read > 1:
        return f'It will take {time_to_read} minutes to read this text.'
    return 'It will take 1 minute to read this text.'

def grammar_check(text):
    sentence_enders = "!?."
    return text[0].isupper() and text[-1] in sentence_enders