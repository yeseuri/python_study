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

    #튜플 패킹
    tri_one = (12, 15)  # 밑변 길이 12와 높이 길이 15를 묶어 놓은 것
    # tri_one = 12, 15 이렇게 소괄호 생략할 수도 있다.
    tri_two = 12, 15
    print(tri_one)
    print(tri_two)

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

    # 파이썬 숫자와 문자열 기초
    # https://wikidocs.net/26718
    #a = 아이유가 부릅니다 "삐삐" 는 문법에러 입니다
    b = '아이유가 부릅니다 "삐삐"'
    c = "I'm a doy"
    print(b)
    print(c)

    #파이썬에서의 "숫자"는 천단위 구분기호 없이 오로지 숫자로만 구성된 데이터입니다.
    #a = 2025/03/31 는 문법에러 입니다
    #1000.0은 실수입니다

    #사칙연산에는 연산자 우선 순위가 적용되어 덧셈, 뺄셈 보다는 곱셈, 나눗셈이 우선합니다
    #연산자 우선순위가 헷갈린다면 괄호를 사용해서 가독성을 높일 수 있습니다
    a = 10 + (2 * 3)
    print(a)

    #파이썬 문자열은 덧셈과 곱셈을 지원합니다. 두개의 문자열을 더하면 문자열이 이어 붙어
    #하나의 새로운 문자열을 만듭니다
    a = "안녕" + "하세요"
    print(a)
    #곱셈은 곱한 숫자만큼 문자열을 반복해서 이어 붙입니다
    b = "안녕" * 3
    print(b)

    # 내장 함수
    # 함수이름() -> 함수 호출 방법
    # print(   100   +   3   ) -> 코드를 작성할때 코드 중간에 포함되는 공백은 결과에 아무런 영향을
    # 미치지 않습니다
    # print 함수 괄호안에 들어가는 값을 함수의 입력이라고 부르며, 다른 말로 파라미터라고 부릅니다
    print(   100   +   3   )
    # print 함수에 100+3 파라미터를 입력한 결과 103이라는 값이 출력되었다.
    # 명령 프롬프트에서 스파이더 콘솔을 불러올수 있는데 거기선 print 함수를 사용하지 않고
    # 출력할 수 있지만 그외 화면에 값을 출려기하는 FM적인 방법은 print 함수를 사용하는 것입니다

    # type() 함수는 값의 조아류를 판별합니다
    # len() 함수는 문자열의 길이를 구하는 함수입니다
    len("123456")
    print(len("123456"))

    # 형변환 함수
    # 숫자/문자열과 같은 데이터의 타입을 변경하는 것을 형변환이라고 합니다.
    # 다음과 같이 데이터 타입이 다른 값에 연산을 적용할 경우 파이썬 인터프리터는 이상하다고 판단하여
    # 에러를 발생합니다
    # a = "1000" + 500
    # 숫자간의 덧셈을 하고 싶으면 문자열을 숫자로 변경한 후에 덧셈 연산을 적용해야 합니다
    print(int("1000") + 500)
    # 실수를 정수로 변환하면 올림/반올림/버림 중에서 어떻게 될까요?
    print(int(10.7))
    # 실수를 정수로 형변환하면 소수점 이하는 버려지는 것을 확인할 수 있습니다.

    #앞에 770000 * 3 주식만 10% 상승으로 장을 마감할 경우 전체 평가 금액을 출력하여라
    # 내가 푼 것
    print(((770000 * 3 * int(0.1) + 292000 * 4 + 38350 * 4)))
    # 정답)
    print(770000 * 3 * 1.1 + 292000 * 4 + 38350 * 4)

    #032
    print("Hi" * 3)

    #033
    print("-" * 80)

    #034
    t1 = "python"
    t2 = "java"
    print( (t1 + " " + t2 + " ") * 4 )

    #035
    # "%s %s %s %d"%.format("이름:", "김민수", "나이:", 10) -> 내가 푼 거
    # "{1} {2} {3} {4}".format("이름:", "김민수", "나이:", 10) -> 내가 푼 거
    # 내가 푼 거
    name1 = "김민수"
    age1 = 10
    name2 = "이철희"
    age2 = 13
    print("이름: %s 나이: %d"%(name1, age1))
    print("이름: %s 나이: %d"%(name2, age2))

    #036
    print("이름: {} 나이: {}".format(name1, age1))
    print("이름: {0} 나이: {1}".format("김민수", 10))

    #037
    result = f'이름: {name1} 나이: {age1}'
    print(result)
    
    #038 컴마 제거 하기
    상장주식수 = "5,969,782,550"

    #내가 푼 거
    #def sum(*p) :
    #   return int(p)

    #print(sum(상장주식수))

    컴마제거 = 상장주식수.replace(",", "")
    타입변환 = int(컴마제거)
    print(타입변환, type(타입변환))

    #039
    분기 = "2020/03(E) (IFRS연결)"
    #print(분기[0:7]) -> 내가 푼 거
    print(분기[:7])

    #040 strip 메서드
    data = "    삼성전자    "
    print(data.strip())
