import life
import random

def random_cell():
    cell = []
    for i in range(3):
        cell.append([])
        for j in range(3):
            cell[i].append(random.choice([True, False]))
    return cell

if __name__ == '__main__':
    c = random_cell()
    # c = life.initialize_cell()
    print(c)
    print(f"Is alive? {life.is_alive(c)}")
    print(f"Is dead? {life.is_dead(c)}")
    print(f"Live Neighbours? {life.count_neighbours(c, True)}")
    print(f"Dead Neighbours? {life.count_neighbours(c, False)}")
