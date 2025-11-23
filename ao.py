def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    orange_count = 0

    # Count apples
    for d in apples:
        if d > 0:
            if s <= a + d :
                apple_count += 1

    # Count oranges
    for d in oranges:
        if d < 0:
             if s <= b + d:
                orange_count += 1

    print(apple_count)
    print(orange_count)


# Example usage
s = 7
t = 10
a = 4
b = 12
apples = [2, 3, -4]
oranges = [3, -2, -4]

countApplesAndOranges(s, t, a, b, apples, oranges)
