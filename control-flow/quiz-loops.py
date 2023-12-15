# Schreiben Sie eine for-Schleife, die die Namensliste durchläuft, um eine Benutzernamensliste zu erstellen. 

# Um für jeden Namen einen Benutzernamen zu erstellen, schreiben Sie alles in Kleinbuchstaben und ersetzen Sie Leerzeichen durch Unterstriche. 
# Führen Sie Ihre for-Schleife über die Liste aus:

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for username in names:
    print(username.lower().replace(" ", "_"))



usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
for index in range(len(usernames)):
    usernames[index] = usernames[index].lower().replace(" ", "_")


tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for token in tokens:
    if token[0] == "<" and token[-1] == ">":
        count += 1
print(count)




items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"
print(html_str)



