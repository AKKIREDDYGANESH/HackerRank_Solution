def word_change(a):
    word_to_digit = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero':'0',
    }
    
    return word_to_digit[a]


def full_string(input1):
    words = input1.split()
    result = ""
    i = 0
    while i< len(words):
        word = words[i]
        if word == "double":
            next_number = words[i+1]
            number = word_change(next_number)
            #result.append(number*2)
            result += number*2
            i +=2
        elif word == "triple":
            next_number = words[i+1]
            number = word_change(next_number)
            #result.append(number*3)
            result += number*3
            i +=2
            
        else:
            #result.append(word_change(word))
            result += word_change(word)
            i +=1
        
    return result






input1 = " two double five nine triple six eight two triple three triple three"

output = full_string(input1)

print(output)
print(type(output))