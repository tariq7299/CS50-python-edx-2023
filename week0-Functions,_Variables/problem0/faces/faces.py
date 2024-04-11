import re



def main():

  userInput = input('Enter something here with a smily or frowning emoticons --> ')

  text = replace_emoticons_simpler(userInput)

  print(text)



# A simpler version
def replace_emoticons_simpler(text):
    emoDict = {
     ":)" :  "🙂",
     ":(" :  "🙁"
    }
    for emoticon, emoji in emoDict.items() :
        if emoticon in text :
            text = text.replace(emoticon, emoji)
    return text


# Another better way to solve the problem but more complicated that uses the "re" module
def replace_emoticons(text):

    # Define emoticon patterns
    smiley_pattern = re.compile('[:;=]-?[)D]')
    frowny_pattern = re.compile('[:;=]-?[\(\\\/]')

    # Replace smiley emoticons with slightly smiling emoji
    text = smiley_pattern.sub('🙂', text)

    # Replace frowny emoticons with slightly frowning emoji
    text = frowny_pattern.sub('🙁', text)

    return text


# The same previous way but with anther synatx, without using re.complie() method
# def replace_emoticons(text):

    # Define emoticon patterns
    # smiley_pattern = r'[:;=]-?[)D]'
    # frowny_pattern = r'[:;=]-?[\(\\\/]'

    # Replace smiley emoticons with slightly smiling emoji
    # text = re.sub(smiley_pattern, '🙂', text)

    # Replace frowny emoticons with slightly frowning emoji
    # text = re.sub(frowny_pattern, '🙁', text)
    

main()


