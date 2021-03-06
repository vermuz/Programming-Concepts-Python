# From Stanford easy way to generate subsets
# 2^N calls
def getSubSets(soFar, rest):
    if len(rest) == 0:
        print soFar
        return

    getSubSets(soFar + rest[0], rest[1:]) # Either choose the character and recurse
    getSubSets(soFar, rest[1:])           # Or dont choose the character and recurse

getSubSets("","abc")


# Second method, instead of creating new arrays pass around the indice
def sub(word, word_idx, soFar, soFar_idx):
  if word_idx == len(soFar):
    print(soFar[:soFar_idx])
    return

  sub(word, word_idx+1, soFar, soFar_idx)
  soFar[soFar_idx] = word[word_idx]
  sub(word, word_idx+1, soFar, soFar_idx+1)

word = 'abc'
soFar = [0] * len(word)
print sub(word, 0, soFar, 0)

# Third method use bit array
def sub_bitarray(word, word_idx, soFar):
  if word_idx == len(soFar):
    res = []
    for i in range(len(soFar)):
       if soFar[i] == 1:
         res.append(word[i])
    print res
    return
  soFar[word_idx] = 0
  sub_bitarray(word, word_idx+1, soFar)
  soFar[word_idx] = 1
  sub_bitarray(word, word_idx+1, soFar)

word = 'abc'
soFar = [0] * len(word)
print sub_bitarray(word, 0, soFar)
