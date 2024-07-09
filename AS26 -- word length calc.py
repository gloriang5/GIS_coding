text = str(input("Enter some text to check the average word length:\n"))
text_list = text.split()
length_sum = 0
number_of_words = 0

for i in text_list:
    length = len(i)
    length_sum += length
    number_of_words += 1

average_word_length = length_sum/number_of_words
print(f"The average word length of this text is {average_word_length} letters per word")