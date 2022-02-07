from pydes import *
import matplotlib.pyplot as plot
import statistics


# calculate hamming distance between two  strings
def hamming_dis(inp1, inp2):
    dis = 0
    for i in range(len(inp1)):
        if inp1[i] != inp2[i]:
            dis += 1
    return dis

 # call the encrypt function and store outputs of rounds 1 to 16(/IP-1 since the
 # swap and inverse permutation do not change the hamming distance)


def get_lis(pt, key):
    k = des(key)
    lis = []
    print('\nplaintext\tciphertext\tkey')
    for plaintext in pt:
        d = k.encrypt(plaintext)
        print(plaintext, d, key, sep='\t')
        lis.append(lis_main.copy())
        lis_main.clear()
    print('\n')

    return lis


def get_plot(lis, name, increment, initial):
    base = lis[0]
    compare = lis[1:]

    x = initial
    hamming = []
    for i, li in enumerate(compare):
        temp = []
        temp.append(x)
        # store output of round 0 (plaintext/P since permutation does not change hamming distance)
        x += increment
        for j, string in enumerate(li):
            str1 = ''.join([str(x) for x in base[j]]).strip()
            str2 = ''.join([str(x) for x in compare[i][j]]).strip()
            temp.append(hamming_dis(str1, str2))
        hamming.append(temp)

    plot_lis = []
    for j in range(len(hamming[0])-1):
        temp = []
        for i in range(len(hamming)):
            # calculate hamming distances between outputs of various round
            temp.append(hamming[i][j])
        plot_lis.append(temp)

    print('Hamming distances')
    for s, kk in enumerate(plot_lis):
        print('Round '+str(s), kk, sep=' ')

    plot_lis = tuple(plot_lis)
    medians = [statistics.median(test_list) for test_list in plot_lis]

    fig = plot.figure()                           # plot the box whisker plot
    plot.boxplot(plot_lis, positions=[l for l in range(0, 17)])
    plot.plot([l for l in range(0, 17)], medians)
    fig.suptitle(name)
    plot.xlabel('Rounds')
    plot.ylabel('HD')
    fig.savefig(name+'.png')

    plot.show()




# i)
# The first string of pti is the reference plaintext others have a HD of one w.r.t to this reference plaintext
pti = [b'anshulra', b'`nshrlra', b'anshulha',
       b'anshelra', b'anchulra', b'anbhulra']
get_plot(get_lis(pti, b"stuvwxyz"),
         "5 different plaintexts with each having a \n hamming distance of one w.r.t the base plaintext", 0, 1)

# ii)
# The first string of pti is the reference plaintext others have
# HDs of one, two, three, four, five respectively w.r.t to this reference plaintext
ptii = [b'anshulra', b'bnshulra', b'qwshulra',
        b'qwehulra', b'zxcvulra', b'bfsdblra']
get_plot(get_lis(ptii, b"stuvwxyz"),
         "5 different plaintexts with each having a hamming distance \n increasing from one to five w.r.t the base plaintext", 1, 1)

# iii)
# The first string of k_list is the reference key others have a HD of one w.r.t to this reference key
k_list = [b'abcdefgh', b'a`cdefgh', b'cbcdefgh',
           b'ebcdefgh', b'ibcdefgh', b'qbcdefgh']
plaintext = b"stuvwxyz"

lis = []
print('\nplaintext\tciphertext\tkey')
for i, key in enumerate(k_list):
    key = des(key)
    d = key.encrypt(plaintext)
    print(plaintext, d, k_list[i], sep='\t')
    lis.append(lis_main.copy())
    lis_main.clear()
print('\n')

get_plot(lis, "5 different keys with each having a \n hamming distance of one w.r.t the base key", 0, 0)
