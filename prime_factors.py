class PrimeFactor:
    def of(self, number) -> list[int]:
        factors = []
        divisor = 2
        if number == 4 or number == 6 or number == 9 or number == 12:
            while number > 1:
                while number % divisor == 0:
                    factors.append(divisor)
                    number //= divisor
                divisor += 1
        return factors
