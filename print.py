if __name__=="__main__":

    # print("4""5""6")
    # print("4","5","6")
    # print("4", "5", "6")
    # print("4","5","6", sep="")
    # print(4,5,6)
    # print(456)

    # print("I like")
    # print("money")
    # print("I like", end="")
    # print("money")
    #
    # print("I like", end=" ")
    # print("money")

    # print("I like", end=" gold and ")
    # print("money")

    def sum(n1, n2) :
        return n1 + n2

    def sub(n1, n2) :
        return n1 - n2

    def mul(n1, n2) :
        return n1 * n2

    def div(n1, n2) :
        return n1 / n2

    def to_string(n1) :
        return str(n1)

    num_1 = 100
    num_2 = 200

    print("num_1 + num_2 = " +
            to_string(
                sum(num_1,num_2)
            )
          )

    # 문자열 + 숫자 할려고 %d 사용해 봤는데 함수는 사용 못해요
    # print("%s %d"%("num_1 - num_2 = ", sub(num_1,num_2))

    print("%s을 %d개 주세요."%("아이스크림", 10))

    print("num_1 - num_2 = " +
          to_string(
              sub(num_1, num_2)
          )
        )


    print("num_1 * num_2 = " +
          to_string(
              mul(num_1, num_2)
          )
        )

    print("num_1 / num_2 = " +
          to_string(
              div(num_1, num_2)
          )
        )



    print("====================================================================")

    print("num_1 + num_2",sum(num_1, num_2), '100+200', 1500, sep=" = " )




