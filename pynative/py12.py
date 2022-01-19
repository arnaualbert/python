def get_fibonacci():
  n = int(input("Fibonacci: "))
  a = 0
  b = 1
  sum = 0
  count = 1
  print("Fibonacci: ", end = " ")
  while(count <= n):
    print(sum, end = " ")
    count += 1
    a = b
    b = sum
    sum = a + b
get_fibonacci()