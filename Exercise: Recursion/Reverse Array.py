def reverse_array(idx, numbers):
    if idx == len(numbers) // 2:
        return
    swap_idx = len(numbers) - idx - 1
    numbers[idx], numbers[swap_idx] = numbers[swap_idx], numbers[idx]
    reverse_array(idx + 1, numbers)


numbers = input().split()
reverse_array(0, numbers)
print(*numbers)
