import datetime

log_data = []

f = open('index.txt', 'r')
datalist = f.readlines()
for data in datalist:
    log_data.append(list(data.rstrip('\n').split(',')))

f.close()


def questions_1(log):
    # serverの故障検知
    break_servers = []
    for i, servers in enumerate(log):
        if servers[2] != '-' or len(servers) > 3:
            continue
        else:
            server_name = servers[1]
            break_time = datetime.datetime.strptime(servers[0], '%Y%m%d%H%M%S')

            for j in range(i + 1, len(log)):
                next_servers = log_data[j]
                if next_servers[1] != server_name:
                    continue
                elif next_servers[1] == server_name and next_servers[2] == '-':
                    next_servers.append('Flag')
                    continue
                else:
                    revival_time = datetime.datetime.strptime(next_servers[0], '%Y%m%d%H%M%S')
                    break_period = float((revival_time - break_time).total_seconds()) + (float(next_servers[2]) / 1000)
                    break_servers.append({server_name, break_period})
                    break

    return break_servers


print('questions1')
print(f'break server:{questions_1(log_data)}')
print('-' * 100)


def questions_2(log, n):
    # serverの故障検知
    break_servers = []
    for i, servers in enumerate(log):
        if servers[2] != '-' or len(servers) > 3:
            continue
        else:
            count = 1
            server_name = servers[1]
            break_time = datetime.datetime.strptime(servers[0], '%Y%m%d%H%M%S')

            for j in range(i + 1, len(log)):
                next_servers = log_data[j]
                if next_servers[1] != server_name:
                    continue
                elif next_servers[1] == server_name and next_servers[2] == '-':
                    count += 1
                    next_servers.append('Flag')
                    continue
                else:
                    if count >= n:
                        revival_time = datetime.datetime.strptime(next_servers[0], '%Y%m%d%H%M%S')
                        break_period = float((revival_time - break_time).total_seconds()) + (
                                float(next_servers[2]) / 1000)
                        break_servers.append({server_name, break_period})
                    break

    return break_servers


print('questions2')
print(f'break server:{questions_2(log_data, 2)}')
print('-'*100)


def questions_3(log, n, m, t):
    break_servers = []
    over_load = {}

    for i, servers in enumerate(log):

        # server負荷の検知
        if servers[2] == '-':
            print('server error')
            over_load[servers[1]] = []
            print(f'server reset: {over_load}')
        else:
            if servers[1] in over_load:
                over_load[servers[1]].append(int(servers[2]))

                if len(over_load[servers[1]]) > m:
                    over_load[servers[1]].pop(0)
                    av_time = sum(over_load[servers[1]]) / m
                    if av_time > t:
                        print(f'over load server: {servers[1]}, {sum(over_load[servers[1]])}ms')
                elif len(over_load[servers[1]]) == m:
                    av_time = sum(over_load[servers[1]]) / m
                    if av_time > t:
                        print(f'over load server: {servers[1]}, {sum(over_load[servers[1]])}ms')
            else:
                over_load[servers[1]] = [int(servers[2])]

        # server故障の検知
        if servers[2] != '-' or len(servers) > 3:
            continue
        else:
            count = 1
            server_name = servers[1]
            break_time = datetime.datetime.strptime(servers[0], '%Y%m%d%H%M%S')

            for j in range(i + 1, len(log)):
                next_servers = log_data[j]
                if next_servers[1] != server_name:
                    continue
                elif next_servers[1] == server_name and next_servers[2] == '-':
                    count += 1
                    next_servers.append('Flag')
                    continue
                else:
                    if count >= n:
                        revival_time = datetime.datetime.strptime(next_servers[0], '%Y%m%d%H%M%S')
                        break_period = float((revival_time - break_time).total_seconds()) + (
                                float(next_servers[2]) / 1000)
                        break_servers.append({server_name, break_period})
                    break

    return break_servers


print('questions3')
print(f'break server:{questions_3(log_data, 2, 3, 15)}')
print('-'*100)


def questions_4(log, n, m, t):
    break_servers = []
    over_load = {}

    for i, servers in enumerate(log):

        # server負荷の検知
        if servers[2] == '-':
            print('server error')
            over_load[servers[1]] = []
            print(f'server reset: {over_load}')
        else:
            if servers[1] in over_load:
                over_load[servers[1]].append(int(servers[2]))

                if len(over_load[servers[1]]) > m:
                    over_load[servers[1]].pop(0)
                    av_time = sum(over_load[servers[1]]) / m
                    if av_time > t:
                        print(f'over load server: {servers[1]}, {sum(over_load[servers[1]])}ms')
                elif len(over_load[servers[1]]) == m:
                    av_time = sum(over_load[servers[1]]) / m
                    if av_time > t:
                        print(f'over load server: {servers[1]}, {sum(over_load[servers[1]])}ms')
            else:
                over_load[servers[1]] = [int(servers[2])]

        # server故障の検知
        if servers[2] != '-' or len(servers) > 3:
            continue
        else:
            count = 1
            server_name = servers[1]
            break_time = datetime.datetime.strptime(servers[0], '%Y%m%d%H%M%S')

            for j in range(i + 1, len(log)):
                next_servers = log_data[j]
                if next_servers[1] != server_name:
                    continue
                elif next_servers[1] == server_name and next_servers[2] == '-':
                    count += 1
                    next_servers.append('Flag')
                    continue
                else:
                    if count >= n:
                        revival_time = datetime.datetime.strptime(next_servers[0], '%Y%m%d%H%M%S')
                        break_period = float((revival_time - break_time).total_seconds()) + (
                                float(next_servers[2]) / 1000)
                        s1, s2, s3, s4 = server_name.split('.')
                        subnet_server = s1 + '.' + s2 + '.' + s3
                        break_servers.append(subnet_server)
                    break

    return break_servers


print('questions4')
print(f'break server:{questions_4(log_data, 2, 3, 15)}')
