#  File: DNA.py

#  Description: opens a text file  and outputs the longest common sequence of the text in the lines

#  Student Name: Arturo Reyes Munoz

#  Student UT EID: ar48836

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 03/24

#  Date Last Modified: 03/27

# MODIFIED SUBSTRING FUNCTION TO OUTPUT A LIST WITH THE STRINGS

def substr (st):
  wnd = len (st)
  pair_seq = []
  while (wnd > 0):
    start_idx = 0
    while ((start_idx + wnd) <= len(st)):
      piece = st[start_idx : start_idx + wnd]
      pair_seq.append(piece)
      start_idx += 1
    wnd = wnd - 1
  return pair_seq




  
def main():

  print("Longest Common Sequences")
  print(' ')

  file = open('dna.txt','r')

  dna = []

  # PUT THE TEXT LINES IN A LIST

  for line in file:

    dna.append(line)

  n = int(dna[0])

  pairs=1

  it = 1
 
 # MAIN LOOP

  while pairs <= n:

    seq = substr(dna[it]) + substr(dna[it+1])

    commonseq = []

    longestseq = []

    max_length = 2

    # CREATE LIST WITH REPEATED SEQUENCES

    for i in seq:

      if seq.count(i) > 1 and len(i) > 1:

        commonseq.append(i)

    commonseq = set(commonseq)

    # CREATE LIST WITH ONLY GREATEST LENGTH SEQUENCES


    for i in commonseq:

      if len(i) > max_length:

        longestseq=[i]

        max_length += 1

      elif len(i) == max_length:

        longestseq.append(i)

    # CREATE LIST WITH ONLY GREATEST SEQUENCES PRESENT IN BOTH DNA STRINGS

    longestseq_final = []

    for i in longestseq:

      for j in substr(dna[it]):

        if i == j:

          for k in substr(dna[it+1]):

            if j == k:

              longestseq_final.append(i)

    if len(longestseq_final) == 0:

      print('Pair ' + str(pairs) + ':  No Common Sequence Found')
      print(' ')

    else:

      print('Pair ' + str(pairs) + ':  ' + str(longestseq_final[0]).upper())

      if len(longestseq_final) > 1:

        for i in longestseq_final[1:]:

          print('         ' + str(i).upper())

      print(' ')

    it +=2
    pairs +=1

main()




      

    










  

      
    
