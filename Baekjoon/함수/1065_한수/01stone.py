# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 
# 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 
# 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, 
# N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

'''
입력 : 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
출력 : 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
'''

num = int(input())

hansu = 0
for n in range(1, num+1):
    num_list = list(map(int, str(n)))
    if n < 100: 
        hansu += 1  # 100보다 작으면 무조건 한수
    elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
        hansu += 1  # 100보다 크면 자리수 차이가 같으면 한수
print(hansu)