def solve():
    print("Solving")
    with open('../../inputs/2022/testcase.txt') as f:
        lines = f.read().splitlines()

    adj_list = {}
    flow_rates = {}
    cache = {}
    for line in lines:
        line = line.replace(",", "").split(' ')
        adj_list[line[1]] = line[9:]
        flow_rates[line[1]] = int(line[4].strip(";").split("=")[1])


def dfs(adj_list, flow_rates, cache, move_to, ):

    if (x, y, z) in cache:
        return cache[(x, y, z)]

    dfs(adj_list, flow_rates, cache, move_to, )



if __name__ == '__main__':
    solve()
