def is_prime_list(numbers):
    for num in numbers:            
        if num == 0 or num == 1:
            return False
        elif num < 0:
            return False  
        for n in range(2, num):
            if num % n == 0:
                return False
    return True

