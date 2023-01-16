tower = {}
def tower_of_hanoi(n, source, target, auxiliary):
    if n > 0:
        # Move all the disks except the bottom disk to the auxiliary rod
        tower_of_hanoi(n - 1, source, auxiliary, target)
        # Move the bottom disk from the source rod to the target rod
        print(f"Move disk {n} from {source} to {target}")
        tower[n] = target
        # Move all the remaining disks from the auxiliary rod to the target rod
        tower_of_hanoi(n - 1, auxiliary, target, source)

tower_of_hanoi(3,"source","target","auxiliary")
print(tower)