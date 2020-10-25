import random

def p_print(list):
    for i in range(0, len(list)):
        print(list[i], end="")
    print()



word_list = ["banana", "apple", "orange"]

set_word = random.randint(0,len(word_list) - 1)

player = []

for i in range(0, len(word_list[set_word])):
        player.append("_ ")

p_print(player)

max_count = 7
count = 0

running = True

while running:
    temp_c = input("알파벳 입력 ")
    if word_list[set_word].count(temp_c) != 0:
        print("correct")
        print()
        for i in range(0, len(word_list[set_word])):
            if temp_c == word_list[set_word][i]:
                player.insert(i, "{0} ".format(temp_c))
                del player[i + 1]
        
    if word_list[set_word].count(temp_c) == 0:
        print("Wrong")
        print("남은 횟수", max_count- count - 1)
        count += 1

    if player.count("_ ") == 0:
        print("Success")
        running = False

    if count == max_count:
        print("횟수없음")
        running = False
    
    p_print(player)
    print()

