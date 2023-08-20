# -*- coding: utf-8 -*-
"""

Numeric serie that converge

@autor Rogerio Ribeiro Macedo
"""

def head_msg():
    """
    Print the head message 

    Returns
    -------
    None.

    """
    print()
    print("-".center(79, "-"))
    print(f'{"|":<1} {"Serie that converge":^75} {"|":>1}')
    print("-".center(79, "-"))
    print()

def main():
    """
    Principal

    Returns
    -------
    None.

    """
    head_msg()

    try:
        k = int(input("Value of k [k=1].: ").strip())
        for i in range(1, k+1):
            soma = 0
            for j in range(1, i+1):
                soma = soma + (1 / 2**j)
            print(f"S{i} = {soma:0.15f}")
    except ValueError as msg_err:
        print(f"Erro: {msg_err}")

if __name__ == "__main__":
    main()
