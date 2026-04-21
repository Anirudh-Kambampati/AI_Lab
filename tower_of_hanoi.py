def TOH(n, source, aux, dest):
    if n == 1:
        print("Move disk 1 from", source, "to", dest)
        return

    TOH(n-1, source, dest, aux)
    print("Move disk", n, "from", source, "to", dest)
    TOH(n-1, aux, source, dest)

TOH(4, 'A', 'B', 'C')