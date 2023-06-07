import que
# print(que.data["questions"][0])
count=0
for q in que.data["questions"]:
    print(q['question'])
    print(f"a:{q['options']['a']}")
    print(f"b:{q['options']['b']}")
    print(f"c:{q['options']['c']}")
    print(f"d:{q['options']['d']}\n")
    candidate = input('Answer: ')
    print('\n')
    if(candidate == q['correctOption']): count+=1

print(f'You got {count} marks out of {len(que.data["questions"])}')