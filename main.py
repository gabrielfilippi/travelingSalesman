from algorithms import randomAlgorithm, greedyAlgorithm, semiGreedyAlgorithm

#excutando as funções por 30 vezes.
i = 0
while i < 30:
  randomAlgorithm(i)
  i += 1

i = 0
while i < 30:
  greedyAlgorithm(i)
  i += 1

i = 0
while i < 30:
  semiGreedyAlgorithm(i)
  i += 1