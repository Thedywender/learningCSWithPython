ratings = [6, 8, 5, 9, 10]

new_notes = [rating * 10 for rating in ratings]
print(new_notes)

multiply_three = [rating for rating in ratings if rating % 3 == 0]
print(multiply_three)
