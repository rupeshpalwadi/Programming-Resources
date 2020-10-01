def move(pos, des):
    print(f"Move disk from {pos} to {des}")

def hanoi(disks, pos, aux, des):
    if disks == 0:
        return
    
    hanoi(disks-1, pos, des, aux)
    move(pos, des)
    hanoi(disks-1, aux, pos, des)

hanoi(3, "A", "B", "C")
