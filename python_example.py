from dataclasses import replace

if __name__=="__main__":

    # 초보자를 위한 파이썬 300제
    # 01. 파이썬 시작하기 001 ~ 010

    print("Hello world")
    print("Mary's cosmetics")
    # print("신씨가 소리질렀다. "도둑이야"")은 안돼
    print('신씨가 소리질렀다. "도둑이야"')
    print("신씨가 소리질렀다. '도둑이야'")
    print("C:\\windows")
    print("안녕하세요.\n만나서\t\t반갑습니다.")
    print("오늘은", "일요일")
    print("naver;kakao;sk;samsung")
    print("naver", "kakao", "sk", "samsung", sep=";")
    print("naver", "kakao", "sk", "samsung", sep="/")
    print("first", end="")
    print("second")
    print(5/3)

    # 초보자를 위한 파이썬 300제
    # 02. 파이썬 변수 011 ~ 020

    #011
    삼성전자 = 50000
    def sum(a) :
        return str(a * 10) + "원"

    print(sum(삼성전자))

    #012
    # 시가총액 = "298조"
    # 현재가 = "50,000원"
    # PER = 15.79

    # print(시가총액, 현재가, PER)

    시가총액 = 298000000000000
    현재가 = 50000
    PER = 15.79
    print(시가총액, type(시가총액))
    print(현재가, type(현재가))
    print(PER, type(PER))

    #013
    s = "hello"
    t = "python"
    print(s + "!", t)
    # 궁금한점 str은 문자열인데 왜 괄호안에 ""를 해줘야해? str()안에 함수는 ""없이 그냥 쓰잖아 함수일떄 쓰는게 str()이야?
    print(s + str("!"), t)
    print(s + str("b"), t)

    #014
    #곱하기가 우선
    print(2+2*3)

    #015
    a = 128
    print(type(a))
    b="132"
    print(type(b))

    #016
    num_str = 720
    print(type(num_str))

    num_int = float(num_str)
    print(num_int+1, type(num_int))

    #017
    num = 100
    num1 = str(num)
    num2 = "100"
    print(type(num1), type(num2))

    #018
    fl = float(15.79)
    data = "15.79"
    print(type(fl))
    print(data, type(data))

    #019
    #궁금한점 최근 3년이면 보통 밑으로 1,2,3 내려가는가.. 내가 생각을 깊게 못했나..
    year = "2020"
    year_int = int(year)
    print(year_int+1, year_int+2, year_int+3, type(year_int))
    print(int(year)-3)
    print(int(year)-2)
    print(int(year)-1)
    print(int(year)-1)
    print(int(year)-2)
    print(int(year)-3)

    #020
    월금액 = 48584
    무이자_개월수 = 36
    print(월금액 * 무이자_개월수)
    월 = 48584
    총금액 = 월 * 36
    print(총금액)

    #03. 파이썬 문자열 021 ~ 030
    #021
    #이건 첫번째 문자 세번째 문자를 출력하는 방법이 아니네...
    print("{0}월 {1}일 입니다. {2}월 {3}일 입니다. {4}월 {5}일 입니다".format(10,31,12,3,7,"안녕하세요"))

    print("| {0:<10} | {1:<5} |".format("왼쪽 10칸", "왼쪽 5칸"))
    print("| {0:>10} | {1:>5} |".format("오른쪽 10칸", "오른쪽 5칸"))
    print("| {0:^10} | {1:^5} |".format("가운데 10칸", "가운데 5칸"))

    print("| {0:-<10} | {1:o<5} |".format("왼쪽10칸", "왼쪽5칸"))
    print("| {0:+>10} | {1:0>5} |".format("오른쪽10칸", "오른쪽5칸"))
    print("| {0:.^10} | {1:@^5} |".format("가운데10칸", "가운데5칸"))

    letters = 'python'
    print(letters[0], letters[2])
    #022
    license_place = "24가 2210"
    print(license_place[4:8])
    #let result = "Hello world"
    #console.log(result.slice(2, -1))
    print(license_place[4],license_place[5],license_place[6],license_place[7])

    #023
    #파이썬 슬라이싱 a[start:end:step] step:보폭
    string = "홀짝홀짝홀짝"
    print(string[0], string[2], string[4], sep="")
    print(string[::2])
    print(string[::-1])
    print(string[::1])
    print(string[::3])

    #024
    #궁금한점 왜 string이라는 변수를 023번에서도 썼는데 또 쓸수 있어? 파이썬은 변수를 또 사용할수 있지만
    #나중에 유지보수가 힘들어지기 때문에 같은 변수는 사용하지 않는것이 좋다.
    string = "PYTHON"
    print(string[::-1])

    #025
    phone_number = "010-1111-2222"
    print(phone_number.replace('-',''))
    #뭐가 문제일까용
    phone_number = "010-1111-2222"
    phone_number1 = phone_number.replace("-", " ")
    print(phone_number1)

    #026
    phone_number = "010-1111-2222"
    phone_number1 = phone_number.replace("-", "")
    print(phone_number1)

    #027
    url = "http://sharebook.kr"
    print(url[-2::])

    #튜블의 패킹과 언패킹
    def sum(*nums) :  # 전달되는 모든 값들을 하나의 튜플로 묶어서 nums에 저장
        s = 0
        for i in nums:
            s += i
        return s, nums


    print(sum(1, 2, 3))
    print(sum(1, 2, 3, 4))
    print(sum(1, 2, 3, 4, 5))

    #패킹 :  묶기, 언패킹 : 풀기
    #튜플에 저장된 값을 꺼내는 행위를 "튜플 언패킹"이라한다
    tri_one = (12, 15)
    bt, ht = tri_one #튜플 언패킹
    print(bt, ht)

    #튜플을 언패킹 하더라도 *로 묶어서 푼 경우 리스트로 묶인 것을 확인할 수 있다
    nums = (1,2,3,4,5)
    n1,n2, *others = nums
    print(n1)
    print(n2)
    print(others)

    def show_man(name,age,height):
        print(name,age,height, sep=', 1')

    p = ('Yoon', 22, 180)
    show_man(*p)
    show_man('Yoon', 22, 180)

    p = ['park', 21, 177]
    show_man(*p)

    t = (1, 2,(3, 4))
    a,b,(c,d) = t
    print(a, b, c, d, sep=", ")

    p = 'Hong', (32, 178), '010-1234-5678', 'Korea'
    na, (ag,he), ph, ad = p
    print(na,he)

    name,(_, height),_,_= p
    print(name, height)

    # for문 예시 메모장에서 링크, for문 시작할때 보기 (25.03.30)
    # for (i = 0; i<rows.length; i++) {
    #     var obj = {
    #         patternId: Id,
    #         sortOrder: idx
    #    };
    #     rowOrderArr.push(obj);
    #
    # }

    #028
    #typeError: 문자열은 수정할 수 없다. 실행결과를 확인해보면 문자열이 할당 메서드를
    #지원하지 않음을 알 수 있다.
    # lang = 'python'
    # lang[0] = 'P'
    # print(lang)

    #029
    string = 'abcdfe2a354a32a'
    string_1 = string.replace('a', 'A')
    print(string_1)

    #030
    #aBcd가 출력되지않는 이유는 문자열을 변경할 수 없는 자료형이기 때문이다
    string = 'abcd'
    string.replace('b','B')
    print(string)

    # 초보자를 위한 파이썬 300제
    # 03. 파이썬 문자열 031 ~ 040
    #031
    # a = "3"
    # b = 4
    # c = a + b
    # print(c, type(c))

    a = "3"
    b = "4"
    print(a + b, type(a + b))

    # 정수 + 실수는 실수다 더 넒은 자료형으로 변환해준다
    # 문자열 + 실수는 더 넓은 자료형인 문자열로 바뀌는데 자바랑, 자바스크립트는
    # 문자열로 바뀌지만 파이썬은 다른 자료형은 더할수 없다(타입 에러가 뜬다)
    a = 5  # 정수
    b = 3.2  # 실수
    result = a + b
    print(result)










