#Question 1
def prime(n):
     if n<2:
          return False
     for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
     return True
def main():
    try:
          Day_so = input("Nhap vao 1 day so: ")
          Cac_so = [int(x) for x in Day_so.split()]
          if any(n<=0 for n in Cac_so):
            print('Vui long nhap so nguyen duong')
            return
          prime_number=[n for n in Cac_so if prime(n)]
          largest_prime_number=max(prime_number)
          print('Cac so nguyen to la:', prime_number)
          print('So nguyen to lon nhat la:', largest_prime_number)
    except ValueError:
         print('Error')
if __name__ == "__main__":
    main()