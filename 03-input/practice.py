where = input('경기장은 어디입니까?')
win = input('이긴 팀은 어디입니까?')
lose = input('진 팀은 어디입니까?')
score = input('스코어는 몇대몇 입니까?')
print('''오늘 %s에서 야구경기가 열렸습니다
%s와(과) %s의 치열한 공방전이 펼쳐졌습니다
결국 %s은 %s를 %s으로 이겼습니다''' %(where, win, lose, win, lose, score))
print(f'''오늘 {where}에서 야구경기가 열렸습니다
{win}와(과) {lose}의 치열한 공방전이 펼쳐졌습니다
결국 {win}은 {lose}를 {score}으로 이겼습니다''')