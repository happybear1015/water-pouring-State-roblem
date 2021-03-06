def successor(x,y,X,Y):
    """
    x:表示当前的第 1 个杯子的水量
    y:表示当前的第 2 个杯子的水量
    X:第 1 个杯子的容积
    Y:第 2 个杯子的容积
    """
    return {
        (x, 0): "杯子1有一点，杯子2全部倒掉",
        (0, y): "杯子2有一点，杯子1全部倒掉",
        (x, Y): "杯子1有一点，杯子2全部装满",
        (X, y): "杯子2有一点，杯子1全部装满",
        # (0, x+y): "杯子1有一点，杯子2全部转满",
        (0, x+y) if x+y<=Y else (x+y-Y,Y):"第1个杯子的水倒给第2个杯子",
        (x+y, 0) if x+y<=X else (X,x+y-X):"第2个杯子的水倒给第1个杯子",
    }

# 指定一个初始状态（30，40），以及杯子容量（90，40）【第一个杯子90mL,第二个杯子40mL】
# 只进行一次倒水，输出结果，看看第二个状态有多少种可能性
print(successor(30,40,90,40))