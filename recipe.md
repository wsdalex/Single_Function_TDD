## 1. Describe the Problem
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature
def calc_reading_time(text):
Calculate reading time based on length of string
Parameters:
    text:A string containing the words being read
Returns:
    time: number of minutes to read the text
Side Effects:
    The function doesn't print or have any side effects

## 3. Create Examples as Tests
Given a text containing 200 words returns 1 minute
calc_reading_time('200 word text') == 'It will take 1 minute to read this text.'

Given a text containing 600 words return 3 minutes
calc_reading_time('600 word text') == 'It will take 3 minutes to read this text.'

Given a text containing 40 words returns 1 minute
calc_reading_time('40 word text') == 'It will take 1 minute to read this text.'

## 1. Describe the problem
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature
def grammar_check(text):
Check if sentence is grmatically correct.
parameters:
    text: a string to be evaluated
Returns: A boolean value that relates to testing the string
Side Effects:
    There are no side effects

## 3. Create Examples as Tests
Given a text with correct grammar, returns True
grammar_check('Hello, my name is Will!') == True

Given a text with no capital letter on the first word, returns False
grammar_check('hello, my name is Will!') == False

Given a text with no correct sentence ending punctuation, return False
grammar_check('Hello, my name is Will1') == False