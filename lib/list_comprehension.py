def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]

num_list = [0, 1, 3, 5, 7, 8, 9]
sentence_list = ["I like computers", "I require coffee", "Live long and prosper"]

# using the above dummy data for illustration
print(return_evens(num_list))
print(make_exclamation(sentence_list))