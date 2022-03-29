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
        (0, x+y) if x+y<=Y else (x+y-Y,Y):"第1个杯子的水倒给第2个杯子", # (0, x+y): "杯子1有一点，杯子2全部转满",
        (x+y, 0) if x+y<=X else (X,x+y-X):"第2个杯子的水倒给第1个杯子",
    }
# 指定一个初始状态（30，40），以及杯子容量（90，40）【第一个杯子90mL,第二个杯子40mL】
# 只进行一次倒水，输出结果，看看第二个状态有多少种可能性
# print(successor(30,40,90,40))


def search_solution(capacity1,capacity2,goal,start=(0,0)):
    """
    查找结果函数
    capacity1：容器1的体积
    capacity2：容器2的体积
    goal：要实现的目标
    start：初始状态的两个杯子中的水含量
    """

    if goal in start:
        return [start] # 如果目标在初始转态中，直接返回初始状态

    explored=set() # 已经探测过的点

    paths=[[('init',start)]] #正在探索的路线

    while paths:
        path =paths.pop(0)
        (x,y)=path[-1][-1]

        for state,action in successor(x,y,capacity1,capacity2).items():
        ### 注意：state为最终杯子里的具体数值，action为所采取的方式动作
            if state not in explored:
                explored.add(state) # 已经探索过的点
            new_path=path+[(action,state)]
            if goal in state:
                return new_path
            else:
                paths.append(new_path)

    return []

if __name__=="__main__":
    result=search_solution(90,40,60)
    for s in result:
        print(s)


