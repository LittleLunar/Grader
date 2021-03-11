def min_weight(cargo, n):
    if n == 1:
        return sum(cargo)
    
    min_ = 999999999999999999
    for i in range(len(cargo)):
        if len(cargo[i:]) < n - 1:
            break
        this_box = sum(cargo[:i])
        other_box = min_weight(cargo[i:], n - 1)
        min_ = min(max(this_box,other_box),min_)
    return min_

cargo, box = input("Enter Input : ").split('/')
cargo = list(map(int, cargo.split()))
print(f"Minimum weigth for {box} box(es) = {min_weight(cargo,int(box))}")