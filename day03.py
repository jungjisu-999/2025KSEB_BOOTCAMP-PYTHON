# Assignment
# v2.3) 다음 코드에서 딕셔너리를 제거하고 리스트만 사용하여 동일하게 동작하도록 코드를 수정하시오.
import random
drinks = ["위스키", "와인", "소주", "고량주"]
snacks = ["초콜릿","치즈", "삼겹살","양꼬치"]
drinks.append("사케")
snacks.append("광어회")
snacks[0] = "낙곱새"
while True:
    menu = input(f'다음 술중에 고르세요.\n1) {drinks[0]}   2) {drinks[1]}   3) {drinks[2]}   4) {drinks[3]}   5) {drinks[4]}   6) 아무거나   7) 종료 : ')
    if menu == '1':
        print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')
    elif menu == '2':
        print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')
    elif menu == '3':
        print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')
    elif menu == '4':
        print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')
    elif menu == '5':
        print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')
    elif menu == '6':
        random_index = random.randint(0, len(drinks)-1)
        print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')

    
        random_drink = random.choice(drinks)
        print(f'{random_drink}에 어울리는 안주는 {drinks[random_drink]} 입니다')
    elif menu == '7':
        print(f'다음에 또 오세요')
        break

        # Assignment
        # v2.4) 메뉴 삭제 추가에 대응되는 코드를 추가하시오
        import random

        drinks = ["위스키", "와인", "소주", "고량주"]
        snacks = ["초콜릿", "치즈", "삼겹살", "양꼬치"]
        # drinks.append("사케")
        # snacks.append("광어회")
        snacks[0] = "낙곱새"
        # drinks.append("데킬라")
        # snacks.append("소금")

        menu_list = '다음 술중에 고르세요.\n'
        for i in range(len(drinks)):
            menu_list = menu_list + f'{i+1}) {drinks[i]}   '
        #print(menu_list)

        while True:
            menu = input(
                f'다음 술중에 고르세요.\n1) {drinks[0]}   2) {drinks[1]}   3) {drinks[2]}   4) {drinks[3]}   5) {drinks[4]}   6) 아무거나   7) 종료 : ')
            if menu == '1':
                print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')
            elif menu == '2':
                print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')
            elif menu == '3':
                print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')
            elif menu == '4':
                print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')
            elif menu == '5':
                print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')
            elif menu == '6':
                random_index = random.randint(0, len(drinks) - 1)
                print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')

                random_drink = random.choice(drinks)
                print(f'{random_drink}에 어울리는 안주는 {drinks[random_drink]} 입니다')
            elif menu == '7':
                print(f'다음에 또 오세요')
                break

# Assignment
# v2.5) while 안쪽의 하드코딩된 코드를 함수화하시오.
import random

drinks = ["위스키", "와인", "소주", "고량주"]
snacks = ["초콜릿", "치즈", "삼겹살", "양꼬치"]
drinks.append("사케")
snacks.append("광어회")
snacks[0] = "낙곱새"
while True:
    menu = input(
        f'다음 술중에 고르세요.\n1) {drinks[0]}   2) {drinks[1]}   3) {drinks[2]}   4) {drinks[3]}   5) {drinks[4]}   6) 아무거나   7) 종료 : ')
    if menu == '1':
        print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')
    elif menu == '2':
        print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')
    elif menu == '3':
        print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')
    elif menu == '4':
        print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')
    elif menu == '5':
        print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')
    elif menu == '6':
        random_index = random.randint(0, len(drinks) - 1)
        print(f'{drinks[0]}에 어울리는 안주는 {snacks[0]} 입니다')

        random_drink = random.choice(drinks)
        print(f'{random_drink}에 어울리는 안주는 {drinks[random_drink]} 입니다')
    elif menu == '7':
        print(f'다음에 또 오세요')
        break