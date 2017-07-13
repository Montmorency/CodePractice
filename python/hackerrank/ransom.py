def ransom_note(magazine, ransom):
    enough_words = True
    if len(ransom) > len(magazine):
      return False
    for word in ransom:
      enough_words = magazine.count(word) >= ransom.count(word) and enough_words
    return enough_words

#m, n = map(int, raw_input().strip().split(' '))
#magazine = raw_input().strip().split(' ')
#ransom = raw_input().strip().split(' ')
magazine = 'give me one grand today night'
ransom = 'give one grand today'
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
