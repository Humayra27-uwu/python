def count_rare_items(items):
    rare_items = ['egg', 'bread', 'milk']
    count = 0
    for item in items:
        if item in rare_items:
            count += 1
    return count
print(count_rare_items(['oil']))