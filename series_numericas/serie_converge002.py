# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 15:09:58 2023

série -> sum 1/k **3

@author: rogerio
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

    with open("serie_converge002.dat", "w", encoding="utf-8") as serie_file:
        try:
            k = int(input("Value of k [k=1].: ").strip())
            for i in range(1, k+1):
                soma = 0
                for j in range(1, i+1):
                    soma = soma + (1 / (j ** 3))

                serie_file.write(f"{soma:0.15f}\n")
                print(f"S{i} = {soma:0.15f}", end="\r")

            print("\nFile serie_converge.dat saved!")
        except ValueError as msg_err:
            print(f"Erro: {msg_err}")

if __name__ == "__main__":
    main()
