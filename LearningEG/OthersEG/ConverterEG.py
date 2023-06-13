'''
message = input('>')
words = message.split(' ') #anything with space inbetween will become single word
emojis = {
    ':)': '😊',
    ':(': '😥'
}
output = ''
for word in words:
    output += emojis.get(word, word) + ' ' #this first word is the keyword itself(emoji) and the second is all the other words, if never put the "word" it will just appear None
print(output)
'''
#Resuable functions eg. emoji_converter()
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
    ':)': '😊',
    ':(': '😥'
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return output

message = input('>')
print(emoji_converter(message))