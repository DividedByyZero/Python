words = []
with open('input.txt','r') as file:
    para = file.read()
total_line = para.split('\n')
for x in total_line:
    for word in x.split(" "):
        words.append(word)
search_word=["Python", "C", "OOP", "Hello", "Java"]
for s_word in search_word:
    count_word = 0
    for f_word in words:
        if s_word.upper()==f_word.upper():
            count_word+=1
    ans = str(count_word)
    print(s_word+" -> " + ans)