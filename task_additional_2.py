def digit_root(num):
    if not isinstance(num, int):
        print("Ошибка: число должно быть целым")
        return None
    
    if num < 1:
        print("Ошибка: число должно быть натуральным (1, 2, 3, ...)")
        return None
        
    if num > 10**7:
        print("Ошибка: число не должно превышать 10 000 000")
        return None

    while num >= 10:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        num = digit_sum
    
    print(digit_sum)

digit_root(4851)