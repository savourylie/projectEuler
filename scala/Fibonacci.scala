object Fibonacci {
    def fib(n: Int): Int = {
        val first = 0
        val second = 1

        if (n == 1) {
            first
        }

        else if (n == 2) {
            second
        }

        else {
            fib(n - 1) + fib(n - 2)
        }
    }

    def main(args: Array[String]): Unit = {
        @annotation.tailrec
        def go(n: Int): Unit = {
            if (n == 1) {
                fib(1)
            }

            else {
                println(fib(n))
                go(n - 1)   
            }
        }

        go(20)

    }
}

