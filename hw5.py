# 숫자 하나를 한글로 읽는 함수 (0~9)
def read_number(digit):
    korean_digits = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    return korean_digits[digit]

# 세 자리 수를 입력받아 한글로 읽는 문자열을 화면에 출력하는 함수
def read_single_digit(num):
    # 각 자리 추출
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10

    # 한글로 변환
    h_read = read_number(hundreds)
    t_read = read_number(tens)
    o_read = read_number(ones)

    # 결과 출력
    print(h_read, t_read, o_read)

# 주 프로그램부
num = int(input("세 자리 정수를 입력하세요: "))
if num < 100 or num > 999:
    print("세 자리 양의 정수를 입력해야 합니다.")
else:
    read_single_digit(num)