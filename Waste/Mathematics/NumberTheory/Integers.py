class Integer:
    def __init__(self, even_odd, positive_negative_zero, prime_composite_one):

        if even_odd == "even":
            self.even_odd = "even"
        elif even_odd == "odd":
            self.even_odd = "odd"

        if positive_negative_zero == "positive":
            self.positive_negative_zero = "positive"
        elif positive_negative_zero == "negative":
            self.positive_negative_zero = "negative"
        elif positive_negative_zero == "zero":
            self.positive_negative_zero = "zero"

        if self.positive_negative_zero == "positive":
            if prime_composite_one == "one":
                self.prime_composite_one = "one"
            elif prime_composite_one == "prime":
                self.prime_composite_one = "prime"
            elif prime_composite_one == "composite":
                self.prime_composite_one = "composite"



five = Integer("odd", "positive", "prime")

print(five.even_odd)
