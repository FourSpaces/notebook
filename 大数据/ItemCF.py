#!/usr/sbin/env python
# -*- coding:utf-8 -*-
 
import math
# ItemCF算法
def ItemSimilarity(train):
    # 物品-物品的共同矩阵， 即买了当前物品，又买了其他物品的计算
    # 见：https://blog.csdn.net/u013063153/article/details/53838674
    C = dict()
    # 物品被多少个不同用户购买
    N = dict()
    for u, items in train.items():
        for i in items.keys():
            N.setdefault(i, 0)
            N[i] += 1
            C.setdefault(i, {})
            for j in items.keys():
                if i == j:
                    continue
                C[i].setdefault(j, 0)
                C[i][j] += 1
    # 计算相似度矩阵
    W = dict()
    for i, related_items in C.items():
        W.setdefault(i, {})
        for j, cij in related_items.items():
            W[i][j] = cij / math.sqrt(N[i] * N[j])
    return W


 
# 推荐前K个用户
def Recommend(train, user_id, W, K):
    rank = dict()
    action_item = train[user_id]
    for item, score in action_item.items():
        for j, wj in sorted(W[item].items(), key=lambda x:x[1], reverse=True)[0:K]:
            if j in action_item.keys():
                continue
            rank.setdefault(j, 0)
            rank[j] += score * wj
    print rank.items()
    return sorted(rank.items(), key=lambda x:x[1], reverse=True)
 
train = dict()
for line in open('requests.txt', 'r'):
    user, item, score = line.strip().split(",")
    train.setdefault(user, {})
    train[user][item] = float(score)
W = ItemSimilarity(train)
result = Recommend(train, '5', W, 3)
print result