def calculate_word_frequency(input_sentence):
    word_freq = {}
    words = input_sentence.lower().split()
    
    for word in words:
        word = word.strip('.,?!') 
        if word:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    
    return word_freq

new_sentence = "We are learning python in moringa"
result = calculate_word_frequency(new_sentence)
print(result)