# 빙고
# 문제 설명
# 빙고는 NxN 크기의 게임 보드 칸에 1부터 NxN까지의 자연수를 중복 없이 하나씩 적은 후 숫자를 하나씩 지워나가는 게임입니다.
# 이때, 가로, 세로, 대각선 방향으로 한 줄에 적힌 숫자를 모두 지울 경우 빙고를 1개 만들었다고 합니다.
# 다음은 4X4 크기의 게임 보드를 이용해 게임을 진행한 예시입니다.

# image

# 위와 같이 각 칸에 숫자가 적혀 있을 때, 위 게임 보드에서 순서대로 지운 숫자가 [14,3,2,4,13,1,16,11,5,15]인 경우 아래와 같이 빙고 3개가 만들어집니다.

# image

# 빙고 게임 보드에 적힌 숫자가 담겨있는 배열 board, 게임 보드에서 순서대로 지운 숫자가 들어있는 배열 nums가 매개변수로 주어질 때,
# board에서 nums에 들어있는 숫자를 모두 지우면 몇 개의 빙고가 만들어지는지 return하도록 solution함수를 완성해주세요.

# 제한사항
# board는 게임 보드 칸에 적힌 숫자를 뜻하는 NxN크기의 2차원 배열이며, N은 2 이상 500이하의 자연수입니다.
# board의 각 칸에는 1 이상 NxN이하의 자연수가 중복 없이 하나씩 들어있습니다.
# nums는 board에서 지울 숫자가 들어있는 배열이며, 길이는 1 이상 NxN이하입니다.
# nums에 들어있는 숫자는 1 이상 NxN이하의 자연수이며, 중복된 수가 들어있지 않습니다.


# 입출력 예
# board	nums	result
# [[11,13,15,16],[12,1,4,3],[10,2,7,8],[5,14,6,9]]	[14,3,2,4,13,1,16,11,5,15]	3
# [[6,15,17,14,23],[5,12,16,13,25],[21,4,2,1,22],[10,20,3,18,8],[11,9,19,24,7]]	[15,7,2,25,9,16,12,18,5,4,10,13,20]	2
# 입출력 예 설명
# 입출력 예 #1
# 문제의 예시와 같습니다.

# 입출력 예 #2
# 다음 그림과 같이 2개의 빙고가 만들어집니다.
# image


import unittest
import collections


def solution(board, nums):
    bingo = 0

    lines = dict()
    lines["rows"] = collections.defaultdict(int)
    lines["cols"] = collections.defaultdict(int)
    lines["diags"] = collections.defaultdict(int)

    for row_idx, row in enumerate(board):
        for col_idx, element in enumerate(row):
            if element in nums:
                lines["rows"][row_idx] += 1
                lines["cols"][row_idx] += 1
                if row_idx == col_idx:
                    lines["diags"][0] += 1
                if row_idx == len(board) - col_idx - 1:
                    lines["diags"][1] += 1

    for line in lines.values():
        for l in line.values():
            if len(board) == l:
                bingo += 1

    return bingo


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(
            solution([[11, 13, 15, 16], [12, 1, 4, 3], [10, 2, 7, 8], [5, 14, 6, 9]], [14, 3, 2, 4, 13, 1, 16, 11, 5, 15]), 3)
        self.assertEqual(
            solution([[6,15,17,14,23],[5,12,16,13,25],[21,4,2,1,22],[10,20,3,18,8],[11,9,19,24,7]], [15,7,2,25,9,16,12,18,5,4,10,13,20]), 2)


unittest.main()
