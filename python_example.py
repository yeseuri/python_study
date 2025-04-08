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
    a = "{0}월 {1}일 입니다. {2}월 {3}일 입니다. {4}월 {5}일 입니다".format(10, 31, 12, 3, 7, "안녕하세요")
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

    #튜블의 패킹과 언패킹
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

    # 튜플 패킹
    tri_one = (12, 15)  # 밑변 길이 12와 높이 길이 15를 묶어 놓은 것
    # tri_one = 12, 15 이렇게 소괄호 생략할 수도 있다.
    tri_two = 12, 15
    print(tri_one)
    print(tri_two)


    #튜플을 언패킹 하더라도 *로 묶어서 푼 경우 리스트로 묶인 것을 확인할 수 있다
    # 궁금한점 위에 sum함수에서는 *로 묶었는데 *nums가 튜플로나옴..
    nums = (1,2,3,4,5)
    n1,n2, *others = nums  #튜플의 언패킹
    print(n1)
    print(n2)
    print(others)

    def show_man(name,age,height):
        print(name,age,height, sep=', 1')

    p = ('Yoon', 22, 180)
    show_man(*p)
    # show_man함수에 return이란 글씨가 없어도 print됨
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

    # name,( , height), , = p
    # print(name, height)
    #공백은 안되고 _를 사용해야한다

    # for문 예시 메모장에서 링크, for문 시작할때 보기 (25.03.30)
    # 생략 나중에 for문 들어가서 고민하기
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
    string.replace('b','B')
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
    print(result, type(result))

    # a = "안녕"
    # b = 2.5
    # result = a + b
    # print(result) 타입에러가 뜬다 문자열과 실수는 연결할수 없다고 한다

    # 파이썬 숫자와 문자열 기초
    # https://wikidocs.net/26718
    # a = 아이유가 부릅니다 "삐삐" 는 문법에러 입니다
    b = '아이유가 부릅니다 "삐삐"'
    c = "I'm a doy"
    # 문법오류 SyntaxError
    # d = I'm a doy
    print(b)
    print(c)

    # 파이썬에서의 "숫자"는 천단위 구분기호 없이 오로지 숫자로만 구성된 데이터입니다.
    # a = 2025/03/31 는 문법에러 입니다
    # 1000.0은 실수입니다

    # 사칙연산에는 연산자 우선 순위가 적용되어 덧셈, 뺄셈 보다는 곱셈, 나눗셈이 우선합니다
    # 연산자 우선순위가 헷갈린다면 괄호를 사용해서 가독성을 높일 수 있습니다
    a = 10 + (2 * 3)
    print(a)

    # 파이썬 문자열은 덧셈과 곱셈을 지원합니다. 두개의 문자열을 더하면 문자열이 이어 붙어
    # 하나의 새로운 문자열을 만듭니다
    a = "안녕" + "하세요"
    print(a)
    # 곱셈은 곱한 숫자만큼 문자열을 반복해서 이어 붙입니다
    b = "안녕" * 3
    print(b)

    # 내장 함수
    # 함수이름() -> 함수 호출 방법
    # print(   100   +   3   ) -> 코드를 작성할때 코드 중간에 포함되는 공백은 결과에 아무런 영향을
    # 미치지 않습니다
    # print 함수 괄호안에 들어가는 값을 함수의 입력이라고 부르며, 다른 말로 파라미터라고 부릅니다
    print(      100    +    3      )
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

    # 앞에 770000 * 3 주식만 10% 상승으로 장을 마감할 경우 전체 평가 금액을 출력하여라
    # 내가 푼 것
    print(((770000 * 3 * int(0.1) + 292000 * 4 + 38350 * 4)))
    # 정답)
    print(770000 * 3 * 1.1 + 292000 * 4 + 38350 * 4)

    # 032
    print("Hi" * 3)

    # 033
    print("-" * 80)

    # 034
    t1 = "python"
    t2 = "java"
    print((t1 + " " + t2 + " ") * 4)

    # 035
    # "%s %s %s %d"%.format("이름:", "김민수", "나이:", 10) -> 내가 푼 거
    # "{1} {2} {3} {4}".format("이름:", "김민수", "나이:", 10) -> 내가 푼 거
    # 내가 푼 거
    name1 = "김민수"
    age1 = 10
    name2 = "이철희"
    age2 = 13
    print("이름: %s 나이: %d" % (name1, age1))
    print("이름: %s 나이: %d" % (name2, age2))
    # 밑에꺼 타입 str
    a = "이름: %s 나이: %d" % (name2, age2)
    print(a, type(a))

    # 036 문자열 출력
    #{} 중괄호가 비어도 되지만 {}숫자를 넣을때 꼭 0부터 넣어야함
    print("{0} {1} {2} {3}".format("이름:", "김민수", "나이:", 10))
    print("이름: {} 나이: {}".format(name1, age1))
    print("이름: {0} 나이: {1}".format("김민수", 10))
    # 밑에꺼 타입 str
    a = "이름: {0} 나이: {1}".format("김민수", 10)
    print(a, type(a))

    # 037 문자열 출력 f-string을 사용해서 풀어보세요
    # f-string 은 파이썬 버전 3.6부터 할수있는 기능입니다
     # f-string은 f와 {}만 알면됩니다 문자열 맨앞에 f를 붙여주고 중괄호 안에
     # 직접 변수이름이나 출력 하고 싶은것을 바로 넣으면 됩니다
     # f'문자열 {변수} 문자열'
     # 밑에꺼 타입 str
    result = f'이름: {name1} 나이: {age1}'
    print(result)
    result1 = f'{name1}'
    result2 = f'123{name1}'
    print(result, type(result))
    print(result1, type(result1))
    print(result2, type(result2))
    print(name1, type(name1))


    # 038 컴마 제거 하기
    상장주식수 = "5,969,782,550"

    # 내가 푼 거
    # def sum(*p) :
    #   return int(p)

    # print(sum(상장주식수))
    # 궁금한점 뒤에 for문을 배우면 다시 해보자
     # def sum(*p) :
     #     for i in p:
     #         return int(i)
     #
     # print(sum(상장주식수))

    컴마제거 = 상장주식수.replace(",", "")
    타입변환 = int(컴마제거)
    print(타입변환, type(타입변환))

    # 039
    분기 = "2020/03(E) (IFRS연결)"
    # print(분기[0:7]) -> 내가 푼 거
    print(분기[:7])

    # 040 strip 메서드
    data = "    삼성전자    "
    print(data.strip())

    # 이 경우 strip() 메서드를 사용하면 좌우 공백을 제거할 수 있습니다. 이때
    # 원본 문자열은 그대로 유지되고 공백이 제거된 새로운 문자열이 반환됩니다
    data1 = data.strip()
    print(data1)

    # 초보자를 위한 파이썬 300제
    # 03. 파이썬 문자열 041 ~ 050

    # 041 upper 메서드
    ticker = "btc_krw"
    print(ticker.upper())
    print(ticker)
    # upper 메서드를 호출하면 이 경우 원본 문자열은 유지되고 대문자로 변경된 새로운 문자열 객체가 반환
    # 되는 겁니다 반환된 새로운 객체를 새로운 변수로 바인딩한 후 이를 print 함수로
    # 출력하면 됩니다.
    ticker1 = ticker.upper()
    print(ticker1)

    # 042 lower 메서드
    # 이 경우도 원본 문자열은 유지되고 대문자로 변경된 새로운 문자열 객체가
    # 반환됩니다
    ticker = "BTC_KRW"
    ticker1 = ticker.lower()
    print(ticker1)

    # 043 capitalize 메서드
    # 이 경우도 원본 문자열은 유지되고 문자열의 첫 글자를 대문자로 변환하고,
    # 나머지 문자는 소문자로 변환합니다
    hello = "hello"
    hello1 = hello.capitalize()
    print(hello1)
    print(hello)

    # 044 endswith 메서드
    # 이 경우 파일 이름이 문자열로 저장되어 있을때 마지막 문자열이 일치하는지
    # 확인하고 true, false로 반환한다
    file_name = "보고서.xlsx"
    file_name1 = file_name.endswith("xlsx")
    print(file_name1)
    print(file_name)

    # 045 endswith 메서드
    # 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이
    # 'xlsx' 또는 'xls'로 끝나는지 True/False 로 확인하기
    file_name = "보고서.xlsx"
    file_name1 = file_name.endswith(("xlsx", "xls"))
    print(file_name1)

    # startswith의 응용
    # 해당 리스트의 원소들이 각각 'L'로 시작하는지 여부를 True/False로 표시하기
    name_list = ['Anakin', 'Padme', 'Obiwan', 'Luke', 'Leia', 'R2-D2', 'C-3PO', 'Han']
    list_1 = []
    for i in name_list:
        s = i.startswith('L')
        list_1.append(s)
    print(s) #맨 마지막 단어 'Han'
    print(list_1)
    print(i)

    # test 중 test_list에서 마지막에 오는 단어를 기준으로 True, False를 반환함
    test_list = ['Love', 'Yeseul', 'Linda']
    for i in test_list:
        a = i.startswith('L')

    print(a) #마지막 단어가 Yesul이면 False가 뜸
    # append 메소드: 리스트에 요소를 추가하는 메소드로 리스트 마지막에
    # 순차적으로 요소를 추가

    name_list = ['Anakin', 'Padme', 'Obiwan', 'Luke', 'Leia', 'R2-D2', 'C-3PO', 'Han']
    list_2 = []
    for i in name_list:
        if i.startswith('L') == True:
            list_2.append(i)#마지막 단어가 Yesul이면 False가 뜸

    print(list_2)

    # 046 startswith 메서드
    file_name = "2020_보고서.xlsx"
    print(file_name.startswith('2020'))

    # 047 split 메서드
    # 문자열이 있을때 공백을 기준으로 문자열을 분리해줍니다(리스트안에 담아줌)
    a = "hello world"
    print(a.split())

    # 048 split 메서드
    # split 메서드는 문자열을 분리할 때 사용합니다. 이때 어떤 값을 넘겨주면
    # 그 값을 기준으로 문자열을 분리해줍니다.
    ticker = "btc_krw"
    print(ticker.split("_"))

    # 049 split 메서드
    date = "2020-05-01"
    date1 = date.split("-")
    print(date1)

    # 050 rstrip 메서드
    # rstrip() 메서드를 사용하면 오른쪾 공백이 제거된 새로운 문자열 객체가 반환됩니다.
    # 그 값을 data라는 변수가 새로 바인딩합니다. 기존의 공백이 포함된 문자열은
    # 메모리에서 자동으로 삭제됩니다
    data = "039490      "
    data2 = data.rstrip()
    data.rstrip()
    data1 = "      039490"
    print(data.rstrip())  # 공백없음 ->  이때 data에 주소(메모리에 할당된 주소 id)가 공백있는 data에서 공백없는 data로 덮어쓰기 된다
    print(data1.rstrip())  # 왼쪽 공백있음
    print(data)  # 공백있음
    print(data2)  # 공백없음
    print(data)  # 공백있음 궁금한점 왜 공백이 있냐? 521번줄에서 공백삭제한거 아님?
    # rstrip() 메서드를 사용하면 오른쪽 공백이 제거된 새로운 문자열 객체가 반환됩니다
    print(data1.lstrip())  # 공백없음 lstrip 왼쪽 공백 없앰

    # 초보자를 위한 파이썬 300제
    # 04. 파이썬 리스트 051 ~ 060

    # 051 리스트 생성
    movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

    # 052 리스트에 원소 추가
    # movie_rank1 = movie_rank.append("베트맨")
    # 변수에 넣는건 안됨 문자열은 변경할 수 없는 자료형이기 때문이다
    movie_rank.append("베트맨")
    print(movie_rank)

    # 053 insert : 집어넣다
    movie_rank.insert(1, "슈퍼맨")
    print(movie_rank)

    # 054 remove 사용함
    movie_rank.remove("럭키")
    print(movie_rank)

    # 055 del 사용함
    del movie_rank[2]
    del movie_rank[2]
    print(movie_rank)

    # 056
    lang1 = ["C", "C++", "JAVA"]
    lang2 = ["Python", "Go", "C#"]
    langs = lang1 + lang2
    print(langs)

    # 057
    nums = [1, 2, 3, 4, 5, 6, 7]
    print("max : ", max(nums))
    print("min : ", min(nums))

    # 058
    nums = [1, 2, 3, 4, 5]
    result = sum(nums)
    print(result)

    # 059
    # 중복도 포함
    cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
    print(len(cook))

    # 060
    nums = [1, 2, 3, 4, 5]
    result = sum(nums) / len(nums)
    print(result)

    # 초보자를 위한 파이썬 300제
    # 04. 파이썬 리스트 061 ~ 070

    # 061
    # 날짜 정보를 제외하고 가격 정보만을 출력하라
    price = ['20180728', 100, 130, 140, 150, 160, 170]
    print(price[1:])

    # 062
    # 슬라이싱을 사용해서 홀수만 출력하라
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(nums[::2])

    # 063
    # 슬라이싱을 사용해서 짝수만 출력하라
    print(nums[1::2])

    # 064
    # 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라
    nums = [1, 2, 3, 4, 5]
    print(nums[::-1])

    # 065
    # interest 리스트를 다음과 같이 출력하라
    # 삼성전자 naver
    # 작은 따옴표는 문자열을 뜻하는건데 replace로 작은 따옴표를 없애려고 했음
    interest = ['삼성전자', 'LG전자', 'Naver']
    print(interest[0], interest[2])

    # 066 join메서드
    interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
    # ''.join(리스트) - ['a', 'b', 'c'] 이런식의 리스트를 'abc'의 문자열로 합쳐서 변환해주는 함수인 것이다
    # '구분자'.join(리스트) - '_'join(['a', 'b', 'c'])는 'a_b_c'의 문자열로 반환
    # 이건 '삼성전자LG전자NaverSK하이닉스미래에셋대우'
    print("".join(interest))
    # 이건 '삼성전자 LG전자 Naver SK하이닉스 미래에셋대우'
    print(" ".join(interest))

    # 067 join 메서드
    print('/'.join(interest))

    # 068 join 메서드
    print('\n'.join(interest))

    # 069 문자열 split 메서드
    # 문자열.split 함수는 문자열을 일정한 규칙으로 잘라서 리스트로 만들어 주는 함수
    # 047번 문제 참고 문자열이 있을때 공백을 기준으로 문자열을 분리해줍니다(리스트에 담아줌)
    # split 메서드는 문자열을 분리할 때 사용합니다. 이때 어떤 값을 넘겨주면
    # 그 값을 기준으로 문자열을 분리해줍니다.
    string = "삼성전자/LG전자/Naver"
    interest = string.split('/')
    print(interest)
    # 이거 중요
    print(string.split())
    string1 = "삼성전자 LG전자 Naver"
    print(string1.split())

    # 070 리스트 정렬
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

    # 071
    my_variable = ()
    print(my_variable)
    print(type(my_variable))

    # 072
    movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
    print(movie_rank)

    # 073
    # one 그냥 1로 나옴
    one = (1)
    print(one)
    print(type(one))

    # 튜플로 하나의 데이터가 저장되는 경우, 아래와 같이 쉼표를 입력해야만 합니다
    my_tuple = (1,)
    print(my_tuple)
    print(type(my_tuple))

    # 074
    # t = (1, 2, 3)
    # t[0] = 'a'
    # typeError tuple은 원소(element)의 값을 변경할 수 없습니다

    # 075
    # 원칙적으로 튜플은 괄호와 함께 데이터를 정의해야 하지만, 사용자 편의를 위해
    # 괄호없이도 동작합니다
    t = 1, 2, 3, 4
    print(t)
    print(type(t))

    # 076
    t = ('a', 'b', 'c')
    result = t[0].capitalize()  # 이거 둘다 대문자로 되긴됨
    result = t[0].upper()  # 이거 둘다 대문자로 되긴됨
    print(result)
    print(t)
    # t[0] = 'A'로 튜플값은 변경 할 수 없기 때문에 새로 업데이트해야함
    t = ('A', 'b', 'c')
    print(t)

    # 077
    hi = ('삼성전자', 'LG전자', 'SK Hynix')
    # result = " ".join(hi)
    # print(result) #join은 문자열
    print(type(hi))
    hello = list(hi)
    print(hello)

    # 078
    interest = ['삼성전자', 'LG전자', 'SK Hynix']
    data = tuple(interest)
    print(data)

    # 079 튜플 언팩킹
    temp = ('apple', 'banana', 'cake')
    a, b, c = temp
    print(a, b, c)
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))

    # 080 range 함수
    a = range(2, 100, 2)
    print(tuple(a))

    # 초보자를 위한 파이썬 300제
    # 06. 파이썬 딕셔너리 081 ~ 090

    # 081 별 표현식
    scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
    *others, _, _ = scores
    print(others)

    # 082
    scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
    a, b, *others = scores
    print(others)

    # 083
    scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
    _, *others, _ = scores
    print(others)

    # 084 비어있는 딕셔너리
    temp = {}
    print(temp)

    # 085
    icecream = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
    print(icecream)

    # 086
    icecream['죠스바'] = 1200
    icecream['월드콘'] = 1500
    print(icecream)

    # 087
    merona = icecream['메로나']
    print("메로나 가격:", merona)
    print("메로나 가격: " + str(merona))

    # 088
    merona = icecream['메로나'] = 1300
    print(merona)
    print(icecream)

    # 089
    del icecream['메로나']
    print(icecream)

    # 090
    icecream['누가바'] = 1000
    print(icecream)
    # 정답: 딕셔너리에 없는 키를 사용해서 인덱싱하면 에러가 발생합니다

    # 초보자를 위한 파이썬 300제
    # 06. 파이썬 딕셔너리 091 ~ 100

    # 091 딕셔너리 생성
    inventory = {'메로나': [300, 20],
                 '비비빅': [400, 3],
                 '죠스바': [250, 100]}
    print(inventory)

    # 092 딕셔너리 인덱싱
    # 숫자 + 문자열(원) -> ,
    print(inventory['메로나'][0], "원")

    # 093 딕셔너리 인덱싱
    print(inventory['메로나'][1], "개", sep="")

    # 094 딕셔너리 추가
    inventory['월드콘'] = [500, 7]
    print(inventory)

    # 095 딕셔너리 keys() 메서드
    icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
    # 내가 푼 것
    # keys = icecream.keys() -> 이게 리스트에 들어 있다
    # ice_keys = []
    # ice_keys.append(keys)
    # print(ice_keys)

    ice_keys = list(icecream.keys())
    print(ice_keys)

    # 096 딕셔너리 values() 메서드
    # 내가 푼 거
    ice_values = icecream.values()
    print(ice_values)  # -> 왜 인지 튜플안에 리스트로 들어감, dictionary : 딕셔너리

    ice_values = list(icecream.values())
    print(ice_values)

    # 위에 value가 여러개 일 때
    in_values = list(inventory.values())
    print(in_values)

    # 097 딕셔너리 values() 메서드
    icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
    ice_sum = sum(list(icecream.values()))
    print(ice_sum)

    # 098 딕셔너리 update 메서드
    icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
    new_product = {'팥빙수': 2700, '아맛나': 1000}
    icecream.update({'팥빙수': 2700, '아맛나': 1000})
    print(icecream)

    # 099 zip과 dict

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

    # 100
    data = {'09/05', '09/06', '09/07', '09/08', '09/09'}
    close_price = [10500, 10300, 10100, 10800, 11000]

    close_table = dict(zip(data, close_price))
    print(close_table)

    # 초보자를 위한 파이썬 300제
    # 07. 파이썬 분기문 101 ~ 110

    # 101
    # True / False를 갖는 데이터 타입은
    # 'bool'타입 입니다 (불리언)
    a = True
    print(type(a))

    # 102
    print(3 == 5)

    # 103
    print(3 < 5)

    # 104
    x = 4
    print(1 < x < 5)

    # 105
    print((3 == 3) and (4 != 3))

    # 106
    # print(3 => 4)
    # 지원하지 않는 연산자 입니다

    # 107
    if 4 < 3:
        print('Hello World')

    # 조건을 만족하지 않기 때문에 아무 결과도 출력되지 않습니다.

    # 108
    if 4 < 3:
        print('Hello World')
    else:
        print('Hi, there')

    # 109
    # 조건이 참이니까 참일떄 문장을 수행한다
    # 항상 파이썬 인터프리터는 위에서 아래로 실행된다 if문이 끝나면 수행되는 문장일 뿐이다

    if True:
        print('1')
        print('2')
    else:
        print('3')
    print('4')

    # 110
    # if문에 조건이 참이니까 실행된거고 그안에 또 참이니까 실행된거
    if True:
        if False:
            print('1')
            print('2')
        else:
            print('3')
    else:
        print('4')
    print('5')

    # 111
    # 내가 푼거
    # print('안녕하세요' * 2)

    user = input("입력:")
    print(user * 2)

    # 112
    number_user = input("숫자를 입력하세요:")
    print(int(number_user) + 10)

    # 113
    number_user = input()
    if int(number_user) % 2 == 0:
        print("짝수")
    else:
        print("홀수")

    # 114
