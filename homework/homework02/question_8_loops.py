import time


arrSizes = [6473, 16278, 31782, 62123, 123123, 243140, 976563, 7812500, 15938728, 692657839, 125937563, 269272864, 10000000000]
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

    
