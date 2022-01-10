# 작성자: red-Pen9uin
# Data structure: stack
# 4949: 균형잡힌 세상
# 수행 결과: 30860 KB / 96 ms
"""
세계는 균형이 잘 잡혀있어야 한다.
양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.

정민이의 임무는 어떤 문자열이 주어졌을 때,
괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.

문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고,
문자열이 균형을 이루는 조건은 아래와 같다.

모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.

"""
import sys


def is_balanced(word: str) ->None:
    stack = list()
    cnt = -1
    for i in word:
        if (i == '(') or (i == '['):
            stack.append(i)
            cnt+=1

        elif i == ')':
            if (cnt<0) or stack[cnt]!='(':
                print("no")
                return
            elif stack[cnt]=='(':
                del stack[cnt]
                cnt-=1
        
        elif i == ']':
            if (cnt<0) or stack[cnt]!='[':
                print("no")
                return
            elif stack[cnt]=='[':
                del stack[cnt]
                cnt-=1
    
    if cnt == -1:
        print("yes")
    else:
        print("no")
    return


if __name__ == "__main__":
    while True:
        word = sys.stdin.readline().rstrip('\n')
        if len(word)==1:
            if word[0] == '.':
                break
        is_balanced(word)