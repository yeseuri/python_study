if __name__ == '__main__':
    def sum(n1, n2):
        return n1 + n2

    def sub(n1, n2):
        return n1 - n2

    def mul(n1, n2):
        return n1 * n2

    def div(n1, n2):
        return n1 / n2

    def to_string(n):
        return str(n)

    num_1 = 100
    num_2 = 200
    print("num_1 + num_2 = " +
          to_string(
              sum(num_1, num_2)

          )

          )
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