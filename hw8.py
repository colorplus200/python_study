def buy(shopping_bag):
    item = input('상품명? ')
    if item == '':
        return False
    n = int(input('수량? '))
    shopping_bag[item] = n
    print(f'장바구니에 {item} {n}개가 담겼습니다.')
    return True

def show(shopping_bag):
    print('\n>>> 장바구니 보기:')
    for item, n in shopping_bag.items():
        print(f'{item}: {n}개')

def find(shopping_bag):
    print('\n[검색]')
    key = input('장바구니에서 확인하고자 하는 상품은? ')
    if key in shopping_bag:
        print(f'{key}은(는) {shopping_bag[key]}개 담겨 있습니다.')
    else:
        print(f'{key}는 장바구니에 없습니다.')

# 주 프로그램부
shopping_bag = {}
print('[구입]')
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)