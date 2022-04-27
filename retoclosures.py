def make_div_by(n):
    def div(x):
        return x / n
    return div

def run():
    div_by_3 = make_div_by(3)
    div_by_5 = make_div_by(5)
    div_by_18 = make_div_by(18)

    print(int(div_by_3(18)))
    print(int(div_by_5(100)))
    print(int(div_by_18(54)))


if __name__ == "__main__":
    run()