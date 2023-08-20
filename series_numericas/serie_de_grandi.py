# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 10:58:58 2023

The Grandi serie is a divergent serie.

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
    print(f'{"|":<1} {"Grandi serie":^75} {"|":>1}')
    print("-".center(79, "-"))
    print()

def main():
    """
    Principal.

    Returns
    -------
    None.

    """
    head_msg()

    try:
        k = int(input("Value of k [k=1].: ").strip())
        for i in range(1, k+1):
            result = 0
            type_expr = 'sum'
            for j in range(1, i+1):
                if type_expr == 'minus':
                    result = result - 1
                    type_expr = 'sum'
                else:
                    result = result + 1
                    type_expr = 'minus'

            print(f"S{i} = {result:0.15f}")
    except ValueError as msg_err:
        print(f"Error: {msg_err}")

if __name__ == "__main__":
    main()
