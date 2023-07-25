def convert_to_korean(input_string):
    korean_dict = {
        'q': 'ㅂ',
        'w': 'ㅈ',
        'e': 'ㄷ'
    }
    
    output_string = ''
    for char in input_string:
        if char.lower() in korean_dict:
            output_string += korean_dict[char.lower()]
        else:
            output_string += char
    
    return output_string

input_string = input("string:")
result = convert_to_korean(input_string)
print(result)
