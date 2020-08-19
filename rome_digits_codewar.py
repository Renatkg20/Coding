
# def solution(n):
#   dict1 = {1: "I", 2: "II", 3:"III", 4:"IV", 5:"V", 7:"VII", 8:"VIII", 9:"IX", 10:"X", 50: "L", 100:"C", 400: "CD", 500:"D", 1000:"M", 6:"VI", 40: "XL", 90:"XC", 900:"CM"}
#   i = 0
#   roman_num = ""
#   while n > 0:
#     for _ in range(n // dict1[i]):
#       roman_num += dict1.get[i]
#       n -= dict1[i]
#       i += 1
#   return roman_num


def int_to_Roman(num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

print(int_to_Roman(1989))



# print(solution(80))
# class Test():
#   def __init__(self):
#         pass

#   def assert_equals(actual, expected):
#         if actual == expected:
#             print(True)
#         else:
#             print(False, f"'{actual}' should equal '{expected}'")


# test.assert_equals(solution(1),'I', "solution(1),'I'")
# test.assert_equals(solution(4),'IV', "solution(4),'IV'")
# test.assert_equals(solution(6),'VI', "solution(6),'VI'")
# test.assert_equals(solution(14),'XIV', "solution(14),'XIV")
# test.assert_equals(solution(21),'XXI', "solution(21),'XXI'")
# test.assert_equals(solution(89),'LXXXIX', "solution(89),'LXXXIX'")
# test.assert_equals(solution(91),'XCI', "solution(91),'XCI'")
# test.assert_equals(solution(984),'CMLXXXIV', "solution(984),'CMLXXXIV'")
# test.assert_equals(solution(1000), 'M', 'solution(1000), M')
# test.assert_equals(solutiona(1889),'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
# test.assert_equals(solution(1989),'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")