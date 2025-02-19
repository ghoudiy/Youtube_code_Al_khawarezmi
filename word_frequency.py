ponct = [".", "?", "!", "..."]

# First question

def readTextfile(f):
  file = open(f, 'r')
  lines = file.readlines()
  file.close()
  return lines

# Second question
def Wordfrequency():
  freq = {}
  lines = readTextfile("test.txt")
  for l in lines:
    l = l.lower()
    for p in ponct:
      l = l.replace(p, "")
    words = l.split()
    for w in words:
      # if w in freq.keys():
      #   freq[w] += 1
      # else:
      #   freq[w] = 1
      freq[w] = 1 + freq.get(w, 0)
      print(w)
  return freq


# Third question
def phrases():
  lines = readTextfile("test.txt")
  ph = {}
  i = 1
  for l in lines:
    ph[i] = 0
    for p in ponct:
      ph[i] += l.count(p)
    i += 1
  return ph
