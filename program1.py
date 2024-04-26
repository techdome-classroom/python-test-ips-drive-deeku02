def smallest_missing_positive_integer(numbers):
    smallest_missing = 1
    for num in numbers:
        if num > 0 and num <= smallest_missing:
            smallest_missing = num + 1
    return smallest_missing



    



  

