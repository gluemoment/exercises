def matryoshka(n):
    if n ==1:
        print("Матрешечка")
    else:
        print("Верх матрешки n=", n)
        matryoshka(n-1)
        print("Низ матрешки n=", n)

#if __name__ == "__main__":
    # execute only if run as a script
#    matryoshka(5)
matryoshka(5)
