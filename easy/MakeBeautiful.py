

if __name__ == "__main__":
    inputs = ['0000', '1010', '01011', '1001', '01010010101', '10111', '000001', '101010000010110100', '111110001', '01010100',
              '11', '10000110', '10001011101', '110100000101', '1010', '1010010110', '01010111010', '111100000', '110011001100']
    outputs = [2, 0, 1, 2, 5, 1, 2, 6, 3, 1, 1, 3, 2, 3, 0, 4, 1, 4, 6]
    results = []
    for s in inputs:
        counter_1 = 0
        counter_2 = 0
        m_list = list(map(int, s))
        head = m_list[0]
        for i in range(0, len(m_list) - 1):
            d = m_list[i]
            if d == m_list[i+1]:
                counter_1 += 1
                if d == 0:
                    m_list[i+1] = 1
                else:
                    m_list[i+1] = 0
        m_list = list(reversed(list(map(int, s))))
        for i in range(0, len(m_list) - 1):
            d = m_list[i]
            if d == m_list[i + 1]:
                counter_2 += 1
                if d == 0:
                    m_list[i + 1] = 1
                else:
                    m_list[i + 1] = 0
        results.append(min(counter_1, counter_2))
    print(outputs)
    print(results)
