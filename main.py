def check_expression(expr, ans):
    nums = []
    oper = []
    cur = ''
    for i, s in enumerate(expr):
        if s.isdigit():
            cur += s
        else:
            cur = int(cur)
            nums.append(cur)
            cur = ''
            oper.append(s)
        
        if i == len(expr) - 1:
            cur = int(cur)
            nums.append(cur)
    
    s = 0
    for i, num in enumerate(nums):
        if i == 0:
            s += num
        elif i > 0 and oper[i-1] == '+':
            s += num
        else:
            s -= num
    
    if s == 200:
        ans.append(expr)
    

def rec(cur, expr, digits, ans, oper):
    if cur == len(digits) - 1:
        expr += str(digits[cur])
        check_expression(expr, ans)
        return
    expr += str(digits[cur])
    rec(cur+1, expr + oper[0], digits, ans, oper)
    rec(cur+1, expr + oper[1], digits, ans, oper)
    rec(cur+1, expr + oper[2], digits, ans, oper)
        


def get_list() -> list:
    ans = []

    oper = ['+', '-', '']
    digits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    rec(0, '', digits, ans, oper)

    return ans

if __name__ == '__main__':
    ans = get_list()
    print("ans", ans)
