def main():
  nums = input("Escribe una linea de numeros enteros, sin espacios: ")
  result = 0

  for num in nums:
    num = int(num)
    result = result + num

  print(result)
  

if __name__== "__main__":
  main()