import sys

def calc_recursive(number, exponent, modulus):
    if exponent == 0:
        return 1
    n_pow_2 = number * number % modulus
    n_pow_2e_div_2 = calc_recursive(n_pow_2, exponent // 2, modulus)

    if exponent % 2 == 0:
        return n_pow_2e_div_2
    else:
        return (number * n_pow_2e_div_2) % modulus


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python calc_mod.py <number> <exponent> <modulus>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        exponent = int(sys.argv[2])
        modulus = int(sys.argv[3])
    except ValueError:
        print("All arguments must be integers.")
        sys.exit(1)

    result = calc_recursive(number, exponent, modulus)
    print(f"{number}^{exponent} mod {modulus} = {result}")
    print(f"{number}^{exponent} mod {modulus} = {number ** exponent % modulus}")  # For verification