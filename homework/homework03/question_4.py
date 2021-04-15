import mmap
import time

def check_for_x(filename):
  t = time.time()
  with open(filename, mode="r", encoding="utf8") as file_obj:
    with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
      text = mmap_obj.read()
      for byte in text:
        # lower case x = 120
        # upper case X = 88
        if byte == 120 or byte == 88:
          print("success! you found x in: {} seconds".format(time.time() - t))
          return
      print("failure! you didn't find x in: {} seconds".format(time.time() - t))

check_for_x("q4_test/early_success.txt")
check_for_x("q4_test/late_success.txt")
check_for_x("q4_test/short_fail.txt")
check_for_x("q4_test/long_fail.txt")

