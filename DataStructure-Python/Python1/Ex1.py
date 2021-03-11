print('*** Reading E-Book ***')
text,highlight = input('Text , Highlight : ').split(',')
highlighted_text = ''
for i in text:
    if i == highlight:
        highlighted_text += f'[{i}]'
    else :
        highlighted_text += i 
else : print(highlighted_text)