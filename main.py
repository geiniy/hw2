def bad_character_table(pattern):
    table = [-1] * 256 
    for i in range(len(pattern)):
        table[ord(pattern[i])] = i
    return table

def good_suffix_table(pattern):
    m = len(pattern)
    suff = [0] * m

    #для каждого индекса i вычисляем длину наибольшего суффикса строки pattern[:(i+1)] совпадающего с суффиксом pattern
    suff[m - 1] = m
    g = m - 1
    f = 0
    for i in range(m - 2, -1, -1):
        '''if not i > g:
            print(str(i > g))
        else:
            print(str(i > g), str(suff[i + m - 1 - f] < i - g))'''
        if i > g and suff[i + m - 1 - f] < i - g:
            suff[i] = suff[i + m - 1 - f]
        else:
            if i < g:
                g = i
            f = i
            '''if not g >= 0:
                print(str(g >= 0))
            else:
                print(str(g >= 0), str(pattern[g] == pattern[g + m - 1 - f]))'''
            while g >= 0 and pattern[g] == pattern[g + m - 1 - f]:
                g -= 1
            suff[i] = f - g

    #для каждого суффикса строки pattern хотим найти сдвиг, который совмещает этот суффикс с его более левым вхождением, либо суффикс этого суффикса с каким-то префиксом pattern
    shift = [m] * m
    j = 0
    #тут ищутся вторые
    for i in range(m - 1, -1, -1):
        if suff[i] == i + 1:
            while j < m - 1 - i:
                shift[j] = m - 1 - i
                j += 1
    #а тут первые
    for i in range(m - 1):
        shift[m - 1 - suff[i]] = m - 1 - i
    return shift


def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)

    if not m == 0:
        bad_char = bad_character_table(pattern)
        good_suffix = good_suffix_table(pattern)

    s = 0  
    while s <= n - m:
        j = m - 1
        '''if not j >= 0:
            print(str(j >= 0))
        else:
            print(str(j >= 0), str(pattern[j] == text[s + j]))'''
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s 
        bad_char_shift = j - bad_char[ord(text[s + j])]
        good_suffix_shift = good_suffix[j] if j < m - 1 else 1
        s += max(bad_char_shift, good_suffix_shift)

    return -1  