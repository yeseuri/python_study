# from dataclasses import replace
import requests
# import json  # import json module

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
    def function_sum(a) :
        return str(a * 10) + "원"

    print(function_sum(삼성전자))

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
    n = 5
    print(s + "!", t)
    # 근데 같은 문자열이 아닌 n을 적어도 나오네.. 아 +, *가 아니니까!
    print(s + "!", t, n)
    # 궁금한점 str은 문자열인데 왜 괄호안에 ""를 해줘야해? str()안에 함수는 ""없이 그냥 쓰잖아 함수일떄 쓰는게 str()이야?
    print(s + str("!"), t)
    print(s + str("b"), t)

    #014
    #곱하기가 우선
    print(2+2*3)

    #015
    print('-' * 30 + "015")
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
    #021 문자 인덱싱
    #이건 첫번째 문자 세번째 문자를 출력하는 방법이 아니네...
    print("{0}월 {1}일 입니다. {2}월 {3}일 입니다. {4}월 {5}일 입니다".format(10,31,12,3,7,"안녕하세요"))
    a = "{0}월 {1}일 입니다. {2}월 {3}일 입니다. {4}월 {5}일 입니다".format(10,31,12,3,7,"안녕하세요")
    print(a, type(a))
    print("| {0:<10} | {1:<5} |".format("왼쪽 10칸", "왼쪽 5칸"))
    print("| {0:>10} | {1:>5} |".format("오른쪽 10칸", "오른쪽 5칸"))
    print("| {0:^10} | {1:^5} |".format("가운데 10칸", "가운데 5칸"))

    print("| {0:-<10} | {1:o<5} |".format("왼쪽10칸", "왼쪽5칸"))
    print("| {0:+>10} | {1:0>5} |".format("오른쪽10칸", "오른쪽5칸"))
    print("| {0:.^10} | {1:@^5} |".format("가운데10칸", "가운데5칸"))

    letters = 'python'
    print(letters[0], letters[2])
    #022 문자열 슬라이싱
    license_place = "24가 2210"
    print(license_place[4:8])
    #let result = "Hello world"
    #console.log(result.slice(2, -1))
    print(license_place[4],license_place[5],license_place[6],license_place[7])

    #023 문자열 인덱싱
    #파이썬 슬라이싱 a[start:end:step] step:보폭
    string = "홀짝홀짝홀짝"
    print(string[0], string[2], string[4], sep="")
    print(string[::2])
    print(string[::-1])
    print(string[::-2])
    print(string[::-3])
    print(string[::1])
    print(string[::3])
    string = "가나다라마바"
    # 인덱스[0]부터함
    print(string[::3])
    print(string[0:5:3]) #0번 인덱스부터 5번 인덱스까지 3칸씩 건너뛰면서 추출

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
    print(url[-2::]) #-2번 인텍스부터 끝까지

    #튜플의 패킹과 언패킹
    def function_sum(*nums) :  # 전달되는 모든 값들을 하나의 튜플로 묶어서 nums에 저장
        s = 0
        for i in nums:
            s += i
        return s, nums


    print(function_sum(1, 2, 3))
    print(function_sum(1, 2, 3, 4))
    print(function_sum(1, 2, 3, 4, 5))

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
    #궁금한점 위에 sum함수에서는 *로 묶었는데 *nums가 튜플로나옴..
    nums = (1,2,3,4,5)
    n1,n2, *others = nums #튜플의 언패킹
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
    # show_man함수에 return이란 글씨가 없어도 print됨

    print("yoon", "22", "180", sep=', 1')

    t = (1, 2,(3, 4))
    a,b,(c,d) = t
    print(a, b, c, d, sep=", ")

    p = 'Hong', (32, 178), '010-1234-5678', 'Korea'
    na, (ag,he), ph, ad = p
    print(na,he)

    name,(_, height),_,_= p
    print(name, height)

    # name,( , height), , = p
    # print(name, height)
    #공백은 안되고 _를 사용해야한다

    # for문 예시 메모장에서 링크, for문 시작할때 보기 (25.03.30)
    #생략 나중에 for문 들어가서 고민하기
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
    print(string)

    #030
    #aBcd가 출력되지않는 이유는 문자열을 변경할 수 없는 자료형이기 때문이다
    string = 'abcd'
    string1 = string.replace('b','B')
    print(string1) #string1이라는 변수에 담아야지 변경할수 있다 원본이 유지됨
    print(string)


    # 초보자를 위한 파이썬 300제
    # 03. 파이썬 문자열 031 ~ 040
    #031
    # type Error가 뜸
    # a = "3"
    # b = 4
    # c = a + b
    # print(c, type(c))
    print('-' * 30 + "031")

    a = "3"
    b = "4"
    print(a + b, type(a + b))

    # 정수 + 실수는 실수다 더 넒은 자료형으로 변환해준다
    # 문자열 + 실수는 더 넓은 자료형인 문자열로 바뀌는데 자바랑, 자바스크립트는
    # 문자열로 바뀌지만 파이썬은 다른 자료형은 더할수 없다(타입 에러가 뜬다)
    a = 5  # 정수
    b = 3.2  # 실수
    result = a + b
    print(result, type(result))


    # a = "안녕"
    # b = 2.5
    # result = a + b
    # print(result) 타입에러가 뜬다 문자열과 실수는 연결할수 없다고 한다

    # 파이썬 숫자와 문자열 기초
    # https://wikidocs.net/26718
    #a = 아이유가 부릅니다 "삐삐" 는 문법에러 입니다
    b = '아이유가 부릅니다 "삐삐"'
    c = "I'm a doy"
    # 문법오류 SyntaxError
    # d = I'm a doy
    print(b)
    print(c)
    # print(d)

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
    # 출력할 수 있지만 그외 화면에 값을 출력하는 FM적인 방법은 print 함수를 사용하는 것입니다

    # type() 함수는 값의 종류를 판별합니다
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

    #035 문자열 출력
    # "%s %s %s %d"%.format("이름:", "김민수", "나이:", 10) -> 내가 푼 거

    # 내가 푼 거
    name1 = "김민수"
    age1 = 10
    name2 = "이철희"
    age2 = 13
    print("이름: %s 나이: %d"%(name1, age1))
    print("이름: %s 나이: %d"%(name2, age2))
    # 밑에꺼 타입 str
    a = "이름: %s 나이: %d"%(name2, age2)
    print(a, type(a))

    #036 문자열 출력
    #{} 중괄호가 비어도 되지만 {}숫자를 넣을때 꼭 0부터 넣어야함
    print("{0} {1} {2} {3}".format("이름:", "김민수", "나이:", 10))
    print("이름: {} 나이: {}".format(name1, age1))
    print("이름: {0} 나이: {1}".format("김민수", 10))
    # 밑에꺼 타입 str
    a = "이름: {0} 나이: {1}".format("김민수", 10)
    print(a, type(a))

    #037 문자열 출력 f-string을 사용해서 풀어보세요
    # f-string 은 파이썬 버전 3.6부터 할수있는 기능입니다
    # f-string은 f와 {}만 알면됩니다 문자열 맨앞에 f를 붙여주고 중괄호 안에
    # 직접 변수이름이나 출력 하고 싶은것을 바로 넣으면 됩니다
    # f'문자열 {변수} 문자열'
    # 밑에꺼 타입 str
    result = f'이름: {name1} 나이: {age1}'
    result1 = f'{name1}'
    result2 = f'123{name1}'''
    result3 = f'여어 {"안녕" + "하세요"} 하잇'
    print(result, type(result))
    print(result1, type(result1))
    print(result2, type(result2))
    print(result3, type(result3))
    print(name1, type(name1))
    
    #038 컴마 제거 하기
    상장주식수 = "5,969,782,550"

    #내가 푼 거
    # 궁금한점 뒤에 for문을 배우면 다시 해보자
    # def sum(*p) :
    #     for i in p:
    #         return int(i)
    #
    # print(sum(상장주식수))

    컴마제거 = 상장주식수.replace(",", "")
    타입변환 = int(컴마제거)
    print(타입변환, type(타입변환))

    #039 문자열 슬라이싱
    분기 = "2020/03(E) (IFRS연결)"
    #print(분기[0:7]) -> 내가 푼 거
    print(분기[:7])

    #040 strip 메서드
    data = "    삼성전자    "
    print(data.strip())
    # 이 경우 strip() 메서드를 사용하면 좌우 공백을 제거할 수 있습니다. 이때
    # 원본 문자열은 그대로 유지되고 공백이 제거된 새로운 문자열이 반환됩니다
    data1 = data.strip()
    print(data1)
    print(data)

    # 초보자를 위한 파이썬 300제
    # 03. 파이썬 문자열 041 ~ 050

    #041 upper 메서드
    ticker = "btc_krw"
    print(ticker.upper())
    print(ticker)
    # upper 메서드를 호출하면 이 경우 원본 문자열은 유지되고 대문자로 변경된 새로운 문자열 객체가 반환
    # 되는 겁니다 반환된 새로운 객체를 새로운 변수로 바인딩한 후 이를 print 함수로
    # 출력하면 됩니다.
    ticker1 = ticker.upper()
    print(ticker1)

    #042 lower 메서드
    # 이 경우도 원본 문자열은 유지되고 대문자로 변경된 새로운 문자열 객체가
    # 반환됩니다
    ticker = "BTC_KRW"
    ticker1 = ticker.lower()
    print(ticker1)

    #043 capitalize 메서드
    # 이 경우도 원본 문자열은 유지되고 문자열의 첫 글자를 대문자로 변환하고,
    # 나머지 문자는 소문자로 변환합니다
    hello = "hello"
    hello1 = hello.capitalize()
    print(hello1)
    print(hello)

    #044 endswith 메서드
    # 이 경우 파일 이름이 문자열로 저장되어 있을때 마지막 문자열이 일치하는지
    # 확인하고 true, false로 반환한다
    file_name = "보고서.xlsx"
    file_name1 = file_name.endswith("xlsx")
    print(file_name1)
    print(file_name)

    #045 endswith 메서드
    # 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이
    # 'xlsx' 또는 'xls'로 끝나는지 True/False 로 확인하기
    file_name = "보고서.xlsx"
    file_name1 = file_name.endswith(("xlsx", "xls"))
    print(file_name1)

    # startswith의 응용
    # 해당 리스트의 원소들이 각각 'L'로 시작하는지 여부를 True/False로 표시하기
    name_list = ['Anakin', 'Padme', 'Obiwan', 'Luke', 'Leia', 'R2-D2', 'C-3PO', 'Han']
    list_1 = []
    list_12 = []
    for i in name_list:
        s = i.startswith('L')
        list_1.append(s)
        list_12.append(i)
    print(s) #맨 마지막 단어 'Han'
    print(list_1)
    print(list_12)

    # test 중 test_list에서 마지막에 오는 단어를 기준으로 True, False를 반환함
    test_list = ['Love', 'Yeseul', 'Linda']
    for i in test_list:
        a = i.startswith('L')

    print(a) #마지막 단어가 Yesul이면 False가 뜸
    # append 메소드: 리스트에 요소를 추가하는 메소드로 리스트 마지막에
    # 순차적으로 요소를 추가
    print('*' * 40)
    name_list = ['Anakin', 'Padme', 'Obiwan', 'Luke', 'Leia', 'R2-D2', 'C-3PO', 'Han']
    list_2 = []
    for i in name_list:
        if i.startswith('L') :
            #여기는 조건문이 True일때지
            list_2.append(i)

    print(list_2)

    #046 startswith 메서드
    file_name = "2020_보고서.xlsx"
    print(file_name.startswith('2020'))

    #047 split 메서드
    #문자열이 있을때 공백을 기준으로 문자열을 분리해줍니다(리스트에 담아줌)
    a = "hello world"
    print(a.split())

    #048 split 메서드
    # split 메서드는 문자열을 분리할 때 사용합니다. 이때 어떤 값을 넘겨주면
    # 그 값을 기준으로 문자열을 분리해줍니다.
    ticker = "btc_krw"
    print(ticker.split("_"))

    #049 split 메서드
    date = "2020-05-01"
    date1 = date.split("-")
    print(date1)

    #050 rstrip 메서드
    # rstrip() 메서드를 사용하면 오른쪾 공백이 제거된 새로운 문자열 객체가 반환됩니다.
    # 그 값을 data라는 변수가 새로 바인딩합니다. 기존의 공백이 포함된 문자열은
    # 메모리에서 자동으로 삭제됩니다
    data = "039490      "
    data2 = data.rstrip()
    data.rstrip()
    data1 = "      039490"
    print(data.rstrip()) #공백없음 ->  이때 data에 주소(메모리에 할당된 주소 id)가 공백있는 data에서 공백없는 data로 덮어쓰기 된다
    print(data1.rstrip()) #왼쪽 공백있음
    print(data) #공백있음
    print(data2) #공백없음
    print(data) #공백있음 궁금한점 왜 공백이 있냐? data.rstrip()에서 공백삭제한거 아님?
    # rstrip() 메서드를 사용하면 오른쪽 공백이 제거된 새로운 문자열 객체가 반환됩니다
    print(data1.lstrip()) #공백없음 lstrip 왼쪽 공백 없앰

    # 초보자를 위한 파이썬 300제
    # 04. 파이썬 리스트 051 ~ 060

    #051 리스트 생성
    movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

    #052 리스트에 원소 추가
    # movie_rank1 = movie_rank.append("베트맨")
    # 변수에 넣는건 안됨 문자열은 변경할 수 없는 자료형이기 때문이다
    movie_rank.append("베트맨")
    print(movie_rank)

    #053 insert : 집어넣다
    movie_rank.insert(1, "슈퍼맨")
    print(movie_rank)

    #054 del 사용함
    movie_rank.remove("럭키")
    print(movie_rank)
    # remove를 사용하거나 del로 인덱스 번호를 지정해서 지울수 있다
    # del movie_rank[3]
    # print(movie_rank)


    #055 remove 사용함
    # movie_rank 리스트에서 '스플릿'과 '베트맨'을 삭제하라
    # '스플릿' 삭제
    del movie_rank[2]
    # '베트맨' 삭제, 스플릿 자리에 베트맨이 왔다
    del movie_rank[2]
    print(movie_rank)

    #056
    lang1 = ["C", "C++", "JAVA"]
    lang2 = ["Python", "Go", "C#"]
    langs = lang1 + lang2
    print(langs)

    #057
    nums = [1, 2, 3, 4, 5, 6, 7]
    print("max : ", max(nums))
    print("min : ", min(nums))

    #058
    nums = [1, 2, 3, 4, 5]
    result = sum(nums)
    print(result)

    #059
    # 중복도 포함
    cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
    print(len(cook))

    #060
    nums = [1, 2, 3, 4, 5]
    result = sum(nums) / len(nums)
    print(result)

    # 초보자를 위한 파이썬 300제
    # 04. 파이썬 리스트 061 ~ 070

    #061
    # 날짜 정보를 제외하고 가격 정보만을 출력하라
    price = ['20180728', 100, 130, 140, 150, 160, 170]
    print(price[1:])

    #062
    # 슬라이싱을 사용해서 홀수만 출력하라
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(nums[::2])

    #063
    # 슬라이싱을 사용해서 짝수만 출력하라
    print(nums[1::2])

    #064
    # 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라
    nums = [1, 2, 3, 4, 5]
    print(nums[::-1])

    #065
    # interest 리스트를 다음과 같이 출력하라
    # 삼성전자 naver
    # 작은 따옴표는 문자열을 뜻하는건데 replace로 작은 따옴표를 없애려고 했음
    interest = ['삼성전자', 'LG전자', 'Naver']
    print(interest[0], interest[2])

    #066 join메서드
    interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
    # ''.join(리스트) - ['a', 'b', 'c'] 이런식의 리스트를 'abc'의 문자열로 합쳐서 변환해주는 함수인 것이다
    # '구분자'.join(리스트) - '_'join(['a', 'b', 'c'])는 'a_b_c'의 문자열로 반환
    # 이건 '삼성전자LG전자NaverSK하이닉스미래에셋대우'
    print("".join(interest))
    # 이건 '삼성전자 LG전자 Naver SK하이닉스 미래에셋대우'
    print(" ".join(interest))

    #067 join 메서드
    print('/'.join(interest))

    #068 join 메서드
    print('\n'.join(interest))

    #069 문자열 split 메서드
    # 문자열.split 함수는 문자열을 일정한 규칙으로 잘라서 리스트로 만들어 주는 함수
    # 047 문자열이 있을때 공백을 기준으로 문자열을 분리해줍니다(리스트에 담아줌)
    # split 메서드는 문자열을 분리할 때 사용합니다. 이때 어떤 값을 넘겨주면
    # 그 값을 기준으로 문자열을 분리해줍니다.

    string = "삼성전자/LG전자/Naver"
    interest = string.split('/')
    print(interest)
    # 이거 중요
    print(string.split())
    string1 = "삼성전자 LG전자 Naver"
    print(string1.split())

    #070 리스트 정렬
    # 리스트 자체를 정렬시켜 버리는 것은 sort함수
    # 새로운 정렬된 리스트를 반환하는 함수는 sorted 함수
    data = [2, 4, 3, 1, 5, 10, 9]
    data.sort()
    print(data)
    data1 = sorted(data)
    print(data1)
    print(data)

    # 복습 이 단어를 보고 기능을 알수 있나요  split, strip, rstrip, replace, insert, join

    # 초보자를 위한 파이썬 300제
    # 05. 파이썬 튜플 071 ~ 080

    #071
    my_variable = ()
    print(my_variable)
    print(type(my_variable))

    #072
    movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
    print(movie_rank)


    #073
    # one 그냥 1로 나옴
    one = (1)
    print(one)
    print(type(one))

    # 튜플로 하나의 데이터가 저장되는 경우, 아래와 같이 쉼표를 입력해야만 합니다
    my_tuple = (1,)
    print(my_tuple)
    print(type(my_tuple))

    #074
    # t = (1, 2, 3)
    # t[0] = 'a'
    # typeError tuple은 원소(element)의 값을 변경할 수 없습니다

    #075
    # 원칙적으로 튜플은 괄호와 함께 데이터를 정의해야 하지만, 사용자 편의를 위해
    # 괄호없이도 동작합니다
    t = 1, 2, 3, 4
    print(t)
    print(type(t))

    #076
    t = ('a', 'b', 'c')
    result = t[0].capitalize() #이거 둘다 대문자로 되긴됨
    result = t[0].upper() #이거 둘다 대문자로 되긴됨
    print(result)
    print(t)
    # t[0] = 'A'로 튜플값은 변경 할 수 없기 때문에 새로 업데이트해야함
    t = ('A', 'b', 'c')
    print(t)

    #077
    hi = ('삼성전자', 'LG전자', 'SK Hynix')
    # result = " ".join(hi)
    # print(result) #join은 문자열
    print(type(hi))
    hello = list(hi)
    print(hello)


    #078
    print('-' * 30 + "078")
    interest = ['삼성전자', 'LG전자', 'SK Hynix']
    data = tuple(interest)
    print(data)

    #079 튜플 언팩킹
    temp = ('apple', 'banana', 'cake')
    a, b, c = temp
    print(a, b, c)
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))

    #080 range 함수
    a = range(2, 100, 2)
    print(tuple(a))

    # 초보자를 위한 파이썬 300제
    # 06. 파이썬 딕셔너리 081 ~ 090

    #081 별 표현식
    scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
    *others, _, _ = scores
    print(others)

    #082
    scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
    a,b,*others = scores
    print(others)

    #083
    scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
    _,*others,_ = scores
    print(others)

    #084 비어있는 딕셔너리
    temp = {}
    print(temp)

    #085
    icecream = {'메로나' : 1000, '폴라포': 1200, '빵빠레': 1800}
    print(icecream)

    #086
    icecream['죠스바'] = 1200
    icecream['월드콘'] = 1500
    print(icecream)

    #087
    merona = icecream['메로나']
    print("메로나 가격:",merona)
    print("메로나 가격: " + str(merona))

    #088
    merona = icecream['메로나'] = 1300
    print(merona)
    print(icecream)

    #089
    del icecream['메로나']
    print(icecream)

    #090
    # icecream['누가바']
    icecream['누가바'] = 1000
    print(icecream)
    # 정답: 딕셔너리에 없는 키를 사용해서 인덱싱하면 에러가 발생합니다

    # 초보자를 위한 파이썬 300제
    # 06. 파이썬 딕셔너리 091 ~ 100

    #091 딕셔너리 생성
    inventory = {'메로나': [300, 20],
                '비비빅': [400, 3],
                '죠스바': [250, 100]}
    print(inventory)

    #092 딕셔너리 인덱싱
    #숫자 + 문자열(원) -> ,
    print(inventory['메로나'][0], "원")

    #093 딕셔너리 인덱싱
    print(inventory['메로나'][1],"개", sep="")

    #094 딕셔너리 추가
    inventory['월드콘'] = [500, 7]
    print(inventory)

    #095 딕셔너리 keys() 메서드
    icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
    #내가 푼 것
    # keys = icecream.keys() -> 이게 리스트에 들어 있다
    # ice_keys = []
    # ice_keys.append(keys)
    # print(ice_keys)

    ice_keys = list(icecream.keys())
    print(ice_keys)

    #096 딕셔너리 values() 메서드
    #내가 푼 거
    ice_values = icecream.values()
    print(ice_values) #-> 왜 인지 튜플안에 리스트로 들어감, dictionary : 딕셔너리

    ice_values = list(icecream.values())
    print(ice_values)
    
    # 위에 value가 여러개 일 때
    in_values = list(inventory.values())
    print(in_values)

    #097 딕셔너리 values() 메서드
    icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
    ice_sum = sum(list(icecream.values()))
    print(ice_sum)

    #098 딕셔너리 update 메서드
    icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
    new_product = {'팥빙수': 2700, '아맛나': 1000}
    icecream.update(new_product)
    print(icecream)

    #099 zip과 dict

    name = ['merona', 'gugucon']
    price = [500, 1000]

    for n, p in zip(name, price):
        print(n, p)

    print('-' * 20)

    name = ['merona', 'gugucon']
    price = [500, 1000]

    z = zip(name, price)
    print(list(z))

    print('-' * 20)

    name = ['merona', 'gugucon']
    price = [500, 1000]

    icecream = dict(zip(name, price))
    print(icecream)

    print('-' * 20)

    keys = ("apple", "pear", "peach")
    vals = (300, 250, 400)

    result = dict(zip(keys, vals))
    print(result)

    #100
    data = {'09/05', '09/06', '09/07', '09/08', '09/09'}
    close_price = [10500, 10300, 10100, 10800, 11000]

    close_table = dict(zip(data, close_price))
    print(close_table)

    # 초보자를 위한 파이썬 300제
    # 07. 파이썬 분기문 101 ~ 110

    #101
    # True / False를 갖는 데이터 타입은
    # 'bool'타입 입니다 (불리언)
    print('-' * 30, '101', sep='')

    a = True
    print(type(a))

    #102
    print(3 == 5)

    #103
    print(3 < 5)

    #104
    x = 4
    print(1 < x < 5)

    #105
    print((3 == 3) and (4 != 3))

    #106
    #print(3 => 4)
    # 지원하지 않는 연산자 입니다

    #107
    if 4 < 3:
        print('Hello World')

    # 조건을 만족하지 않기 때문에 아무 결과도 출력되지 않습니다.

    #108
    if 4 < 3:
        print('Hello World')
    else:
        print('Hi, there')

    #109
    # 조건이 참이니까 참일떄 문장을 수행한다
    # 항상 파이썬 인터프리터는 위에서 아래로 실행된다 if문이 끝나면 수행되는 문장일 뿐이다

    if True:
        print('1')
        print('2')
    else:
        print('3')
    print('4')

    #110
    # if문에 조건이 참이니까 실행된거고 그안에 또 참이니까 실행된거
    if True :
        if False:
            print('1')
            print('2')
        else:
            print('3')
    else:
        print('4')
    print('5')

    # 초보자를 위한 파이썬 300제
    # 07. 파이썬 분기문 111 ~ 120

    #111
    # user = input("입력:")
    # print(user * 2)
    
    #112
    # number_user = input("숫자를 입력하세요:")
    # print(int(number_user) + 10)
    
    #113
    # number_user = input("숫자를 입력하세요 :")
    # if int(number_user) % 2 == 0 :
    #     print("짝수")
    # else:
    #     print("홀수")

    #114
    # a = input('숫자를 입력하세요:')
    # b = int(a) + 20
    # if b > 255 :
    #     print("255")
    # else :
    #     print(b)

    #115
    # a = input('숫자를 입력하세용:')
    # b = int(a) - 20
    # if 0 > b :
    #     print(0)
    # elif b > 255 :
    #     print(255)
    # else :
    #     print(b)

    #116
    #내가 푼것
    # a = input('시간을 입력하세요:')
    # b = a.endswith("00")
    # if b:
    #     print('정각입니다')
    # else:
    #     print('정각이 아닙니다')

    #정답
    # time = input("현재시간: ")
    # if time[-2:] == "00" :
    #     print("정각입니다.")
    # else:
    #     print('정각이 아닙니다.')
    #     print(time[::-1]) #이건 내가 넣은거

    #117 if문에서 in을 사용함
    # fruit = ['사과', '포도', '홍시']
    # a = input('좋아하는 과일은?')
    #
    # #내가 푼거(for문을 아직 사용하면 안됨)
    # for i in fruit :
    #     if a == i :
    #         print('정답입니다')
    #     else :
    #         print('오답입니다')
    #
    # print('-' * 30)
    #
    ##정답
    # if a in fruit:
    #     print('정답입니다')
    # else :
    #     print('오답입니다')

    #118
    # warn_investment_list = ['Microsoft', 'Google', 'Naver', 'Kakao', 'SAMSUNG', 'LG']
    # a = input('종목명을 입력하세요: ')
    # if a in warn_investment_list :
    #     print('투자 경고 종목입니다')
    # else :
    #     print('투자 경고 종목이 아닙니다')

    #119
    # fruit = {'봄': '딸기', '여름': '토마토', '가을': '사과'}
    # a = input('제가 좋아하는 계절은: ')
    #내가 푼것
    # if a in fruit.keys() :
    #     print('정답입니다')
    # else :
    #     print('오답입니다')
    #
    # #정답
    # if a in fruit:
    #     print('정답입니다')
    # else :
    #     print('오답입니다')

    #120
    # a = input('좋아하는 과일은?')
    # if a in fruit.values() :
    #     print('정답입니다')
    # else :
    #     print('오답입니다')

    # 초보자를 위한 파이썬 300제
    # 07. 파이썬 분기문 121 ~ 130
    
    #121
    # a = input('영어를 한글자를 입력하세요: ')
    # 내가 푼거
    # if a == a.upper() :
    #     print(a.lower())
    # else :
    #     print(a.upper())

    #정답
    # if a.islower() :
    #     print(a.upper())
    # else :
    #     print(a.lower())

    #122
    # score = input('score: ')

    #내가 푼 거
    # if int(a) <= 100 :
    #     print('grade is A')
    # elif int(a) <= 80 :
    #     print('grade is B')
    # elif int(a) <= 60 :
    #     print('grade is C')
    # elif int(a) <= 40 :
    #     print('grade is D')
    # else :
    #     print('grade is E')

    #정답
    # 정답보니까 조금 더 생각할껄 싶지? 다 아는데..휴
    # score = int(score)
    # if 81 <= score <= 100 :
    #     print('grade is A')
    # elif 61 <= score <= 80 :
    #     print('grade is B')
    # elif 41 <= score <= 60 :
    #     print('grade is C')
    # elif 21 <= score <= 40 :
    #     print('grade is D')
    # else :
    #     print('grade is E')

    #123
    # 내가 푼 것
    # a = input('입력: ')
    # dollar = 1167
    # yen = 1.096
    # euro = 1268
    # solace = 171
    # if a.endswith('달러') :
    #     print(f'{float(a[:-2]) * dollar} 원')
    # elif a.endswith('엔') :
    #     print(f'{int(a[:-1]) * yen} 원')
    # elif a.endswith('유로') :
    #     print(f'{int(a[:-2]) * euro} 원')
    # elif a.endswith('위안') :
    #     print(f'{int(a[:-2]) * solace} 원')

    #정답
    # 환율 = {'달러': 1167,
    #       '엔': 1.096,
    #       '유로': 1268,
    #       '위안': 171}
    # #입력할떄 띄어쓰기를 안하면 에러남
    # user = input('입력: ')
    # num, currency = user.split()
    # # 딕셔너리 value값 가져오는 법 -> 환율[currency]
    # print(float(num) * 환율[currency], '원')

    #124
    # a = input('input number1: ')
    # b = input('input number2: ')
    # c = input('input number3: ')
    # print(max(a,b,c))

    # #125
    #내가 푼거
    # phone = {'SKT': '011',
    #          'KT': '016',
    #          'LGU': '019',
    #         '알수없음': '010'}
    # a = input('휴대전화 번호 입력: ')
    # number = a.split('-')

    # 그런데 만약 value를 이용해서 자주 key를 찾는다면
    # 매번 딕셔너리 전체를 순회하면서 가져오기 때문에 비효율적입니다.
    # 다른 방법으로는 딕셔너리의 {key, value}를 뒤집어 {value: key} 저장해놓고 찾는 방법이 있습니다.

    # bb = {v:k for k,v in phone.items()} #{key:value}를 뒤집어 {value:key} 저장해놓고 찾는 방법

    # 기존 방법보다 2배의 저장공간을 사용하는 단점과 value값에 중복이 있는 경우 1개만 저장되는 단점이 있습니다
    # 그렇더라도 더 빠른 속도가 필요한 경우 유용하게 사용할 수 있습니다.

    # if number[0] in phone.values() :
    #     print(f'당신은 {bb.get(number[0])} 사용자 입니다.')

    #정답
    # number = input("휴대전화 번호 입력: ")
    # num = number.split('-')[0]
    # if num == "011" :
    #     com = "SKT"
    # elif num =="016" :
    #     com = "KT"
    # elif num == "019" :
    #     com = "LGU"
    # else :
    #     com = "알수없음"
    # print(f'당신은 {com} 사용자 입니다.')

    #126
    #내가 푼거
    # a = input("우편번호를 입력하세요: ")
    # if a.startswith(('010','011','010')) :
    #     result = '강북구'
    # elif a.startswith(('013', '014', '015')) :
    #     result = '도봉구'
    # elif a.startswith(('016', '017', '018', '019')) :
    #     result = '노원구'
    #
    # print(result)

    #정답
    # 우편번호 = input('우편번호를 입력하세요: ')
    # 우편번호 = 우편번호[:3]
    #
    # if 우편번호 in ['010', '011', '012'] :
    #     print("강북구")
    # elif 우편번호 in ['013', '014', '015'] :
    #     print("도봉구")
    # else :
    #     print("노원구")

    #127
    #내가 푼거
    # 주민번호 = input('주민등록번호: ')
    # 주민번호 = str(주민번호[7])
    # if 주민번호 in ('1','3') :
    #     print('남자')
    # else :
    #     print('여자')

    #정답
    # 주민번호 = input("주민등록번호: ")
    # 주민번호 = 주민번호.split('-')[1]
    # if 주민번호[0] == '1' or 주민번호[0] == '3' :
    #     print('남자')
    # else :
    #     print('여자')


    #128
    # 주민번호 = input('주민번호를 입력하세요: ')
    # 뒷자리 = 주민번호.split('-')[1]
    #
    # if 0 <= int(뒷자리[1:3]) <= 8 :
    #     print('서울 입니다.')
    #     print(int(뒷자리[2:3]))
    # else :
    #     print('서울이 아닙니다.')
    #     print(int(뒷자리[1:3]))

    #129
    #내가 푼 것
    # 주민번호 = input('주민등록번호: ')
    # 앞자리 = 주민번호.split('-')[0]
    # 뒷자리 = 주민번호.split('-')[1]
    # 앞자리숫 = int(앞자리)
    # 앞자리리 = list(map(int, str(앞자리숫)))
    # 뒷자리숫 = int(뒷자리)
    # 뒷자리리 = list(map(int, str(뒷자리숫)))
    # 앞자리곱 = [2,3,4,5,6,7]
    # 뒷자리곱 = [8,9,2,3,4,5]
    # 곱한값 = []
    # if True :
    #     print(type(앞자리[0]))
    #     print(type(앞자리곱[0]))
    #     print(앞자리숫)
    #     print(앞자리리)
    # # if 앞자리[0] * 앞자리곱[0] :
    # #     곱한값.append()
    #
    # 계산1 = (앞자리리[0] * 앞자리곱[0]) + (앞자리리[1] * 앞자리곱[1]) + (앞자리리[2] * 앞자리곱[2]) + (앞자리리[3] * 앞자리곱[3]) + (앞자리리[4] * 앞자리곱[4]) + (앞자리리[5] * 앞자리곱[5]) + (뒷자리리[0] * 뒷자리곱[0]) + (뒷자리리[1] * 뒷자리곱[1]) + (뒷자리리[2] * 뒷자리곱[2]) + (뒷자리리[3] * 뒷자리곱[3]) + (뒷자리리[4] * 뒷자리곱[4]) + (뒷자리리[5] * 뒷자리곱[5])
    # 계산2 = 11 - (계산1 % 11)
    # 계산3 = str(계산2)
    #
    # if 주민번호[-1] == 계산3[-1]:
    #     print("유효한 주민등록번호입니다.")
    #     print(계산3)
    # else:
    #     print("유효하지 않은 주민등록번호입니다.")
    #     print(계산3)
    #     print(계산3[-1])

    #정답
    # num = input("주민등록번호: ")
    # 계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
    #       int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10]) * 3 + \
    #       int(num[11]) * 4 + int(num[12]) * 5
    # 계산2 = 11 - (계산1 % 11)
    # 계산3 = str(계산2)
    #
    # if num[-1] == 계산3[-1]:
    #     print("유효한 주민등록번호입니다.")
    # else:
    #     print("유효하지 않은 주민등록번호입니다.")

    #130
    # 터미널에 pip install requests 를 입력해서 원래있는 패키지(확장프로그램)를 설치해준다
    btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

    변동폭 = float(btc['max_price']) - float(btc['min_price'])
    print(변동폭)

    가격 = float(btc['opening_price']) + 변동폭

    최고가 = float(btc['max_price'])

    if 가격 > 최고가 :
        print('상승장')
    else :
        print('하락장')

    # 초보자를 위한 파이썬 300제
    # 08. 파이썬 반복문 131 ~ 140

    #131 for문의 실행결과를 예측하라
    과일 = ['사과', '귤', '수박']
    for 변수 in 과일 :
        print(변수)

    #132 for문의 실행결과를 예측하라
    과일 = ['사과', '귤', '수박']
    for 변수 in 과일 :
        print('#####')

    # for문의 핵심은 '들여쓰기된 코드가 자료구조에 저장된 데이터 개수만큼
    # 반복된다'라고 설명했습니다. `과일 = ['사과', '귤', '수박']`에는
    # 세개의 데이터가 저장돼 있으므로 들여쓰기된 `print('####')` 코드가
    # 세번 실행됩니다

    #133
    for 변수 in ['A','B','C'] :
        print(변수)

    #내가 푼 것
    abc = ['A','B','C']
    if abc:
        print('A', 'B', 'C', sep="\n")

    #정답
    변수 = 'A'
    print(변수)
    변수 = 'B'
    print(변수)
    변수 = 'C'
    print(변수)

    #134
    for 변수 in ['A','B','C']:
        print('출력:', 변수)

    #정답
    변수 = 'A'
    print('출력:', 변수)
    변수 = 'B'
    print('출력:', 변수)
    변수 = 'C'
    print('출력:', 변수)

    print('출력:', 'A')
    print('출력:', 'B')
    print('출력:', 'C')

    #135
    for 변수 in ["A", "B", "C"]:
        b = 변수.lower()
        print("변환:", b)

    변수 = "A"
    b = 변수.lower()
    print('변환:',b)
    변수 = "B"
    b = 변수.lower()
    print('변환:', b)
    변수 = "C"
    b = 변수.lower()
    print('변환:', b)

    #136
    for 변수 in [10, 20, 30] :
        print(변수)

    #137
    for 변수 in [10, 20, 30] :
        print(변수)

    #138
    for 변수 in [10, 20, 30]  :
        print(변수)
        print('-------')

    #139
    print('++++')
    for 변수 in [10, 20, 30]:
        print(변수)

    #140
    for i in range(4):
        print('-------')

    for 변수 in [1,2,3,4]:
        print('-------')

    # 초보자를 위한 파이썬 300제
    # 08. 파이썬 반복문 141 ~ 150

    #141
    #내가 푼 것 - 문제를 똑바로 안봄 다 10원씩 더해야하는데...
    for 리스트 in [100,200,300]:
        print(int(리스트 * 1.1))

    #정답
    판매가 = [100,200,300]
    for 변수 in 판매가 :
        print(변수 + 10)

    #142
    리스트 = ['김밥', '라면', '튀김']

    for i in 리스트:
        print('오늘의 메뉴: ' + i)

    #143
    for 변수 in ['SK하이닉스', '심상전자', 'LG전자'] :
        print(len(변수))

    #144
    리스트 = ['dog', 'cat', 'parrot']
    for 변수 in 리스트:
        print(변수, len(변수))

    #145
    리스트 = ['dog', 'cat', 'parrot']
    for 변수 in 리스트:
        print(변수[0])
        
    #146
    리스트 = [1,2,3]
    for 변수 in 리스트:
        print(f'3 x {변수}')

    #정답
    리스트 = [1,2,3]
    for 변수 in 리스트:
        print('3 x', 변수)

    #147
    리스트 = [1,2,3]
    for 변수 in 리스트:
        print('3 x', 변수, '=', 3 * 변수)

    for 변수 in 리스트:
        print('3 x {} = {}'.format(변수, 3 * 변수))

    #148
    리스트 = ['가', '나', '다', '라']

    for 변수 in 리스트[1:]:
        print(변수)


    #149
    for 변수 in 리스트[0:3:2]:
        print(변수)

    #정답
    for 변수 in 리스트[::2]:
        print(변수)

    #150
    리스트 = ['가', '나', '다', '라']
    
    for 변수 in 리스트[::-1]:
        print(변수)

    # 초보자를 위한 파이썬 300제
    # 08. 파이썬 반복문 151 ~ 160

    #151
    리스트 = [3, -20, -3, 44]

    for 변수 in 리스트:
        if 0 > 변수 :
            print(변수)


    #152
    리스트 = [3, 100, 23, 44]

    for 변수 in 리스트:
        if 변수 % 3 == 0:
            print(변수)

    #153
    리스트 = [13, 21, 12, 14, 30, 18]

    for 변수 in 리스트:
        if 변수 < 20 :
            if 변수 % 3 == 0 :
                print(변수)
    
    #정답
    for 변수 in 리스트:
        if (변수 < 20) and (변수 % 3 == 0) :
            print(변수)

    #154
    리스트 = ['I', 'study', 'python', 'language', '!']

    for 변수 in 리스트:
        if len(변수) >= 3 :
            print(변수)

    #155
    리스트 = ['A', 'b', 'c', 'D']

    for 변수 in 리스트:
        if 변수.isupper():
            print(변수)
    
    #156
    
    for 변수 in 리스트:
        if 변수.islower() :
            print(변수)

    #정답
    for 변수 in 리스트:
        if 변수.isupper() == False:
            print(변수)

    for 변수 in 리스트:
        if 변수.isupper() != True:
            print(변수)

    for 변수 in 리스트:
        if not 변수.isupper() :
            print(변수)

    #157
    리스트 = ['dog', 'cat', 'parrot']

    for 변수 in 리스트:
        print(변수.capitalize())

    for 변수 in 리스트:
        print(변수[0].upper(), 변수[1:], sep="")

    #정답
    for 변수 in 리스트:
        print(변수[0].upper() + 변수[1:])

    #158
    리스트 = ['hello.py', 'ex01.py', 'intro.hwp']

    for 변수 in 리스트:
        print(변수.split('.')[0])

    #정답
    for 변수 in 리스트:
        split = 변수.split('.')
        print(split[0])
    
    #159
    리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
    
    for 변수 in 리스트:
        if 변수[-2::] == '.h':
            print(변수)

    #정답
    for 변수 in 리스트:
        split = 변수.split('.')
        if split[1] == 'h':
            print(변수)
            
    #160
    for 변수 in 리스트:
        split = 변수.split('.')
        if (split[1] == 'h') or (split[1] == 'c'):
            print(변수)

    # 초보자를 위한 파이썬 300제
    # 08. 파이썬 반복문 161 ~ 170

    # range(stop): 0부터 stop-1까지의 숫자를 생성합니다

    #161
    for 변수 in range(100):
        print(변수)
        
    #162
    for 변수 in range(2002,2051,4):
        print(변수)

    #163
    for 변수 in range(3,31,3):
        print(변수)
        
    #164
    # for 변수 in range(99,-1,-1):
    #     print(변수)

    #정답
    for i in range(100):
        print(99 - i)

    #165
    #정답
    for i in range(10):
        print(i / 10)

    #166
    for i in range(1,10):
        print('3 x', i, '=', 3 * i )

    #167
    for i in range(1,10):
        if i % 2 == 1:
            print('3 x', i, '=', 3 * i)

    #복수 정답
    for i in range(1,10,2):
        num = 3
        print(num, 'x', i, '=', num * i)

    #168
    #정답
    sum = 0
    for i in range(1,11):
        sum += i
        print('합 :', sum)

    #169
    sum = 0
    for i in range(1,11):
        if i % 2 == 1 :
            sum = sum + i
            print('합 :', sum)

    #170
    result = 1
    for i in range(1,11):
        result = result * i
        print(result)

    # 초보자를 위한 파이썬 300제
    # 08. 파이썬 반복문 171 ~ 180

    print('-' * 30, '171')
    # range(stop) : 0부터 stop-1까지의 숫자를 생성합니다
    # range(start, stop) : start부터 stop-1까지의 숫자를 생성합니다
    # range(start, stop, step) : start부터 stop-1까지 step 간격으로
    # 숫자를 생성합니다

    #171
    price_list = [32100, 32150, 32000, 32500]

    for i in range(len(price_list)):
        print(price_list[i])

    #172
    for i in range(len(price_list)):
        print(i, price_list[i])

    #range를 안쓰면 for문을 쓰면 되지

    for i in price_list:
        print(i)

    # 인덱스(index)와 원소를 동시에 접근하면서 루프돌리기
    # 파이썬 내장함수 enumerate()사용 for문의 in 뒷부분을 enumerate() 함수
    # 로 감싸주면 되는데 기본적으로 인덱스와 원소로 이루어진 튜플을 만들어줍니다
    for i in enumerate(price_list):
        print(i)
    # enumerate()함수를 인덱스와 원소를 각각 다른 변수에 할당하고 싶다면
    # 인자 풀기(unpacking)를 해줘야 합니다
    for i, j in enumerate(['A', 'B', 'C']):
        print(i, j)

    for i, j in enumerate(price_list):
        print(i, j)

    #173
    price_list = [32100, 32150, 32000, 32500]

    #정답
    for i in range(len(price_list)):
        print(3 - i, price_list[i])

    #복수정답
    for i in range(len(price_list)):
        print('복수정답:',(len(price_list) -1) - i, price_list[i])

    #174
    for i in range(len(price_list)):
        print('1', i, '0', price_list[i])

    #정답
    for i in range(1,4):
        print(90 + 10 * i, price_list[i])

    #175
    my_list = ['가', '나', '다', '라']

    for i in [0,1,2]:
        print(my_list[i], my_list[i + 1])

    for i in range(1, len(my_list)):
        print(my_list[i-1], my_list[i])

    #176
    my_list = ['가','나','다','라','마']

    for i in [0, 1, 2]:
        print(my_list[i], my_list[i + 1], my_list[i + 2])

    #177
    my_list = ['가','나','다','라']

    # for i in range(1,0,-1):
    #     print(my_list[i])

    for i in range(3, 0, -1):
        print(i)
        print(my_list[i], my_list[i - 1])

    #178
    my_list = [100, 200, 400, 800]

    for i in range(3):
        print(i)
        print(my_list[i + 1] - my_list[i])

    #복수정답
    for i in range(len(my_list) - 1):
        print(abs(my_list[i + 1] - my_list[i]))

    print('-' * 20)
    #179
    my_list = [100, 200, 400, 800, 1000, 1300]

    sum = 0
    for i in range(3):
        sum = sum + my_list[i]
        print('sum / 3 ', sum / 3)
        # print(my_list[i + 2] - my_list[i + 1])
        # print(my_list[i + 3] - my_list[i + 2])

    # 정답
    for i in [1,2,3,4]:
        print(abs(my_list[i - 1] + my_list[i] + my_list[i + 1]) / 3)
        print('i - 1 :', my_list[i - 1])
        print('i :', my_list[i])
        print('i + 1 :', my_list[i + 1])

    # 심화 정답
    for i in range(1, len(my_list) - 1):
        print(abs(my_list[i - 1] + my_list[i] + my_list[i + 1]) / 3)

    # i  -1 0 1
    # 1   0 1 2
    # 2   1 2 3
    # 3   2 3 4
    # 4   3 4 5
    
    # 인덱스의 범위와 순서가 헷갈려서 나오는 문제임
    #1,2,3,4는 횟수를 4번한단거고(4줄 print한다)
    # 4번째는 3 4 5 즉 my_list = [100, 200, 400, 800, 1000, 1300]
    # 800, 1000, 1300을 의미한다
    # i = 4는 3인덱스를 가르키는게 아니라 횟수로 4번이고 range범위를 넘어선
    # my_list의 3 4 5 인덱스도 간다

    #180
    low_prices = [100, 200, 400, 800, 1000]
    high_prices = [150, 300, 430, 880, 1000]

    a = []
    for i in [0,1,2,3,4]:
        volatility = high_prices[i] - low_prices[i]
        a.append(volatility)
        print(a)

    #정답
    volatility = []
    for i in range(len(low_prices)):
        volatility.append(high_prices[i] - low_prices[i])

    # 초보자를 위한 파이썬 300제
    # 08. 파이썬 반복문 181 ~ 190

    #181
    apart = [['101호', '102호'], ['201호', '202호'], ['301호', '302호']]
    print(apart)

    #182
    stock = [['시가',100, 200, 300], ['종가', 80, 210, 330]]
    print(stock)

    #183
    stock = {'시가': [100, 200, 300], '종가': [80, 210, 330]}
    print(stock)

    #184
    stock = {'10/10' : [80, 110, 70, 90], '10/11' : [210, 230, 190, 200]}
    print(stock)

    #185
    apart = [[101, 102], [201, 202], [301, 302]]

    # 내가 못 푼거
    print(apart[0][1])
    for i in range(len(apart)):
        print(apart[i])

    #정답
    for row in apart:
        for col in row:
            print(col, '호')
