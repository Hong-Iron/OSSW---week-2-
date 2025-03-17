# 사칙연산 함수 정의
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    return a / b

if __name__ == "__main__":
    # 사용자 입력
    print("\n첫 번째 숫자를 입력하세요.")
    input1 = input("입력: ")

    print("\n어떤 연산을 하고 싶은지 기호를 선택하세요. (+, -, *, /)")
    act = input("기호 입력: ")

    print("\n두 번째 숫자를 입력하세요.")
    input2 = input("입력: ")

    if act == '+':
        result = plus(int(input1), int(input2))
    elif act == '-':
        result = minus(int(input1), int(input2))
    elif act == '*':
        result = mul(int(input1), int(input2))
    elif act == '/':
        result = divide(int(input1), int(input2))

    print(f"\n사용자의 결과는 {result}입니다.")
