def sum_to(num):
  return sum(range(num + 1))  
print(sum_to(6))
print(sum_to(10))


def largest(number): 
  return max(number)
print(largest([1, 2, 3, 4, 15, 0]) )

def occurances(string, substr):
  return string.count(substr)
print(occurances('fleep floop', 'e'))

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product


print(product(2, 5, 5))
