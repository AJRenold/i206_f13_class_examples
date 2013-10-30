# ## Python Regex
#
# Important things to understand
# * `\b` versus `^` and `$` and don't forget `[^A-Z]`
# * Uses of `\w` `\d` `\s`
# * `*` versus `+` versus `{m,n}`
# * Uses of sets `[abc]`
# * Uses of optional character or groups with `?`
# * Greedy versus Non-Greedy `.*` and `.*?`
# * Using re.VERBOSE

import re

def stateZipsExample():
    """ Example from f09t2 """
    state_zip = ['CA 94720-4600','NV 10001','XY 99999-9991', 'CA 94720+4600', 'NY10001', 'XY, 99999']

    states_and_zip = re.compile(r'''
                            ^[A-Z]{2}   # Starts with two alpha
                            \           # single space (needs \ to escape)
                            \d{5}       # five digits
                            (?:-\d{4})?  # optional - and four digits
                            $           # ends after optional group (If you remove the $, 'CA 94720+4600' is matched 
                            '''
                         ,flags=re.VERBOSE)

    for state in state_zip:
        m = re.match(states_and_zip, state)
        if m:
            print 'matched: '+ m.group()
        else:
            print 'not mactched: '+state

def tenLetterWordsExample():

    def get_moby_dick():
        """ Helper function to read in Moby Dick """
        with open('pg2701.txt') as infile:
            words = infile.read().strip().split(' ')

        ## Adding Everything for Tim
        words.append('Everything')
        return words

    words = get_moby_dick()

    ## Pos Lookahead example from http://www.regular-expressions.info/lookaround.html
    ## Let's match ten letter words that start with a capital letter

    words_pattern = re.compile(r'''
                        (?=\b\w{10}\b)            # pos lookahead to check if a word has 10 characters
                        ([A-Z])([a-z]*y[a-z]*)    # matches Capital letter, any word containing y, returns 2 groups
                        '''
                     ,flags=re.VERBOSE)

    for word in words:
        m = re.match(words_pattern, word)
        if m:
            # If a match is found, print all of the groups
            print 'all groups:', m.group(), 'group1:', m.group(1), 'group2:', m.group(2)


def fileNameExample():

    ## Neg Lookahead example from http://docs.python.org/2/howto/regex.html
    file_names = ['document.doc', 'assignment.pdf', 'test.docx', 'homework.py', 'more_homework.txt', 'not a file', 'test. ', '.other', 'word']

    # What if we don't want .doc? Use a neg lookahead! (?!doc)
    # Be sure to include a $ to make sure the string ends with doc and there are no more characters.
    file_names_pattern = re.compile(r'''
                            \w+      # alphanumeric and _ one or more
                            \.       # period character
                            \w+      # ends with, alphhanumeric and _ one or more
                            '''
                         ,flags=re.VERBOSE)

    file_names_pattern_exclude_doc = re.compile(r'''
                            \w+      # alphanumeric and _ one or more
                            \.       # period character
                            (?!doc$) # negative lookahead to exclude doc, if the string ends with doc
                            \w+      # ends with, alphhanumeric and _ one or more
                            '''
                         ,flags=re.VERBOSE)

    for fname in file_names:
        ## also try re.match(file_names_pattern_exclude, fname)
        m = re.match(file_names_pattern, fname)
        if m:
            print 'matched: '+ m.group()
        else:
            print 'not matched: '+ fname

if __name__ == '__main__':

    print 'State Example'
    stateZipsExample()

    print '\nTen Letter Words Example'
    tenLetterWordsExample()

    print '\nFile Name Example'
    fileNameExample()
