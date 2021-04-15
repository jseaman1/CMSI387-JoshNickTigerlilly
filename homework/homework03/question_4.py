import mmap

def check_for_x(filename):
  with open(filename, mode="r", encoding="utf8") as file_obj:
    with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
      text = mmap_obj.read()
      print(text)
      for byte in text:
        # lower case x = 120
        # upper case X = 88
        if byte == 120 or byte == 88:
          print("success you found x!")
          return
      print("failure no x found!")

check_for_x("success_test.txt")
check_for_x("failure_test.txt")
