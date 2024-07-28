a = ['abc', 'xyz', 'aba', '1221']

for i, word in enumerate(a):
  if word[0] == word[-1]:
    print("index",i,"element", word)
