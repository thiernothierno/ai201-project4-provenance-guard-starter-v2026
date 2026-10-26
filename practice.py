
import statistics


# text = 'hello hello hello word a b b a b a a a  c @ & ( ) thierno barry tom * & ! '
text = 'a '

new_text = text.split(' ')
# print(new_text)
# total_t = len(text)
# all_p = ['!', '\"', '#', '$', '%', '&', '\\', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\\\', ']', '^', '_', '`', '{', '|', '}', '~']

def example(text):

    new_text = text.split(' ')
    if len(new_text) <= 1:
        return 0
    
    my_dict = {}
    words_frequency = []
    for word in new_text:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1

    # print(my_dict)
    for val in my_dict.values():
        words_frequency.append(val)

   

    mean = statistics.mean(words_frequency)
    std_dev = statistics.stdev(words_frequency)
    return round((std_dev/mean), 3)

print(example(text))
# total_p = 0
# for char in text:
#     if char in all_p:
#         total_p += 1
# print(total_p)
# print(round((total_p /total_t),2))

# unique = {}
# for w in text:
#     if w  in unique:
#         unique[w] += 1
#     else:
#         unique[w] = 1

# solo_words = []
# for a, b in unique.items():
#     if b == 1:
#         solo_words.append(a)

# print(solo_words)
# total_unique_words = len(solo_words)
# total_words = len(text)
# unique_word_over_total = round((total_unique_words / total_words), 2)
# print(unique_word_over_total)
    