def teilbar(x,y):
    if y== 0:
        print("Durch null ist nicht teilbar")
    elif x % y == 0:
        print("X ist durch Y teilbar")
    else:
        print("x ist nicht durch Y teilbar")

teilbar(6,2)
