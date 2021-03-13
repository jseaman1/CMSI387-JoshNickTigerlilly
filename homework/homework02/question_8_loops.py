import time

# arrSizes = [17341530, 39018442, 58527663, 87791495, 131687243, 197530864, 296296296, 444444444, 666666667, 1000000000]
arrSizes = [7629, 15258, 30517, 61035, 122070, 244140, 488281, 976563, 1953125, 3906250, 7812500, 15625000, 31250000, 62500000, 125000000, 250000000, 500000000, 1000000000]
loopCount = 10
accessed = bytes
for size in arrSizes:
  t = time.time()
  arr = bytearray(size)
  timesAccessed = 0
  for i in range(0, loopCount):
    x = 4096
    while (x < len(arr)):
      accessed = arr[x]
      timesAccessed += 1
      x += 4096
  finalTime = time.time() - t
  print("\nSize: {}".format(size))
  # print("times accessed: \t{}".format(timesAccessed))
  print("avg time: \t{}".format(finalTime / timesAccessed))

    