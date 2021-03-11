def bubble(a):
    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]


def selection(a):
    for i in range(len(a)):
        m = a[i]
        m_i = i
        for j in range(i, len(a)):
            if m > a[j]:
                m = a[j]
                m_i = j
        a[i], a[m_i] = a[m_i], a[i]


def insertion(a):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1


def shell(a):
    print(f"\n\tInitial : {a}")
    g = len(a) // 2
    c_compare = 0
    while g > 0:
        for i in range(g, len(a)):
            j = i
            while j >= g and a[j] < a[j - g]:
                c_compare += 1
                a[j], a[j - g] = a[j - g], a[j]
                print(
                    f"\n{c_compare}\tCompare {a[j]} : {a[j - g]}\t | Gap : {g}\tSwap  to : {a}")
                j -= g

            if j >= g:
                c_compare += 1
                print(
                    f"\n{c_compare}\tCompare {a[j - g]} : {a[j]}\t | Gap : {g}\tNot Swap : {a}")

        g //= 2
        if g > 0:
            print("\n<-------------------- CHANGE GAP --------------------> ")
        else:
            print("\n<------------------- END PROCESS -------------------->")


def merge(a, l, r):
    if l < r:
        m = (l + r) // 2
        merge(a, l, m)
        merge(a, m + 1, r)
        q1, q2 = a[:m+1], a[m+1:r+1]
        while q1 and q2:
            if q1[0] < q2[0]:
                a[l] = q1.pop(0)
            else:
                a[l] = q2.pop(0)
            l += 1

        while q1:
            a[l] = q1.pop(0)
            l += 1
        while q2:
            a[l] = q2.pop(0)
            l += 1


def quick(a, l, r):
    c = 0
    if l < r:
        i, j = l
        p = r
        while j < p:
            if a[j] < a[p]:
                a[j], a[i] = a[i], a[j]
                i += 1
            j += 1
        a[p], a[i] = a[i], a[p]
        p, i = i, p
        quick(a, l, p - 1)
        quick(a, p + 1, r)


def heap(a):
    h = [-20000000] * (len(a)*2 + 2)
    size = len(a)
    j = 0
    # maxHeap
    while j != size:
        h[j] = a[j]
        t = j
        while t > 0 and h[t] > h[(t - 1) // 2]:
            h[t], h[(t - 1) // 2] = h[(t - 1) // 2], h[t]
            l = t
            while not (h[l] > h[l*2 + 1] and h[l] > h[l*2 + 2]):
                if h[l*2 + 1] > h[l*2 + 2]:
                    h[l], h[l*2 + 1] = h[l*2 + 1], h[l]
                    l = l*2 + 1
                else:
                    h[l], h[l*2 + 2] = h[l*2 + 2], h[l]
                    l = l*2 + 2
            t = (t - 1) // 2
        j += 1

    # pop
    j = size - 1
    while j >= 0:
        a[j] = h[0]
        h[0], h[j] = h[j], h[0]
        h[j] = -2000000000
        l = 0
        while j != 0 and not (h[l] > h[l*2 + 1] and h[l] > h[l*2 + 2]):
            if h[l*2 + 1] > h[l*2 + 2]:
                h[l], h[l*2 + 1] = h[l*2 + 1], h[l]
                l = l*2 + 1
            else:
                h[l], h[l*2 + 2] = h[l*2 + 2], h[l]
                l = l*2 + 2
        j -= 1
    print(a)


a = [5, 1, 4, 7, 9, 2, 3, 0, 6, 8]
shell(a)
