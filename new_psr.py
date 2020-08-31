def Psr_list(s_sequence):   #本身已经不计算第一位bit，所以输入为当前n长状态
    size = len(s_sequence)
    sums = 0

    for i in range(1, size):
        sums = sums + s_sequence[i]
    return sums


def if_nk(s_sequence):      #必须输入n+1长的cycle，输出是否是nk结果
    period = 1
    order = len(s_sequence)
    for i in range(1, order):
        if s_sequence[i] > s_sequence[i-period]:
            period = i+1
        elif s_sequence[i] < s_sequence[i-period]:
            return False
    return order % period == 0


def if_consecutive_twoZero(s_sequence):     #输入以0开头的状态，输出是否有连续的两个0结果
    order = len(s_sequence)
    for i in range(order - 1):
        if s_sequence[i] == 0 and s_sequence[i+1] == 0:
            return True
    return s_sequence[order - 1] == 0


def twoZero_shift(s_sequence, k):       #输入以0开头的状态,直接输出移k位是否是nk结果
    order = len(s_sequence)
    state = s_sequence[:]
    state = [0] + state
    state += state
    cnt = 0
    i = 0

    while cnt < k:
        i = (i + 1) % (order + 1)
        if state[i] == 0 and state[i + 1] == 0:
            cnt += 1

    return if_nk(state[i:i+order+1])


def next_zero(s_sequence):      #输入以0开头的状态,判断条件2
    order = len(s_sequence)
    state = s_sequence[:]
    state = state + [1]
    state += state

    for i in range(1, order):
        if state[i] == 0:
            return if_nk(state[i:i+order+1])


def alg_mix_orderA(s_sequence, k_number):
    state = None
    retval = []

    while state != s_sequence:
        if state is None:
            state = s_sequence[:]

        v_state = [0] + state[1:]
        sum_ci = Psr_list(state)
        clcyc_c = v_state + [sum_ci % 2]
        condition_a = None

        if sum_ci % 2 == 0 and if_consecutive_twoZero(clcyc_c):
            condition_a = twoZero_shift(v_state, k_number)
        elif not if_consecutive_twoZero(clcyc_c):
            condition_a = next_zero(v_state)

        if sum_ci == len(s_sequence) - 1:
            state = state[1:] + [(1 + state[0]) % 2]
        elif condition_a:
            state = state[1:] + [(1 + Psr_list(state) + state[0]) % 2]
        else:
            state = state[1:] + [(Psr_list(state) + state[0]) % 2]

        retval.append(state[-1])

    return retval


start = [0] * 6
db_sequences = []
for ks in range(1, 20):
    s = ''.join([str(x) for x in alg_mix_orderA(start, ks)])
    s += s
    idx = s.find('0' * len(start))
    if s[idx:idx + 2 ** (len(start))] not in db_sequences:
        db_sequences.append(s[idx:idx + 2 ** (len(start))])
        print('k={}'.format(ks), s[idx:idx + 2 ** (len(start))])
