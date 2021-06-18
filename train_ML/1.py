import numpy as np

usr = [1, 1, 1, 0.9, 0.7, 1.2]


def recommend(user_att):
    global count_1_1, count_2_1
    W1 = np.loadtxt("layer1_W.csv", delimiter=",")
    W2 = np.loadtxt("layer2_W.csv", delimiter=",")
    # 获取各层数量
    ip_len = W1[0].__len__()
    layer1_len = W1.__len__()
    layer2_len = W2.__len__()
    layer0 = [0] * ip_len
    layer1 = [0] * layer1_len
    layer2 = [0] * ip_len
    # 进行计算
    count_0 = 0
    for i in user_att:
#        print("test:",count_0)
        layer0[count_0] = i
        count_0 += 1
        count_1_1 = 0
    for x in layer1:
        count_1 = 0
        count_1_1 += 0
        for y in layer0:
            x = y * W1[count_1_1][count_1]
            count_1 += 1
        count_2_1 = 0
    print(layer1)
    for x in layer2:
        count_2 = 0
        count_2_1 += 0
        for y in layer1:
            print(count_2)
            x = y * W2[count_2_1][count_2]
            count_2 += 1
    print(layer2)


recommend(usr)
