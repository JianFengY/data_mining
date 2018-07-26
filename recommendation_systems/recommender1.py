"""
Created on 2018/7/26
@Author: Jeff Yang
"""

from math import sqrt

users = {
    "Angelica": {
        "Blues Traveler": 3.5,
        "Broken Bells": 2.0,
        "Norah Jones": 4.5,
        "Phoenix": 5.0,
        "Slightly Stoopid": 1.5,
        "The Strokes": 2.5,
        "Vampire Weekend": 2.0
    },
    "Bill": {
        "Blues Traveler": 2.0,
        "Broken Bells": 3.5,
        "Deadmau5": 4.0,
        "Phoenix": 2.0,
        "Slightly Stoopid": 3.5,
        "Vampire Weekend": 3.0
    },
    "Chan": {
        "Blues Traveler": 5.0,
        "Broken Bells": 1.0,
        "Deadmau5": 1.0,
        "Norah Jones": 3.0,
        "Phoenix": 5,
        "Slightly Stoopid": 1.0
    },
    "Dan": {
        "Blues Traveler": 3.0,
        "Broken Bells": 4.0,
        "Deadmau5": 4.5,
        "Phoenix": 3.0,
        "Slightly Stoopid": 4.5,
        "The Strokes": 4.0,
        "Vampire Weekend": 2.0
    },
    "Hailey": {
        "Broken Bells": 4.0,
        "Deadmau5": 1.0,
        "Norah Jones": 4.0,
        "The Strokes": 4.0,
        "Vampire Weekend": 1.0
    },
    "Jordyn": {
        "Broken Bells": 4.5,
        "Deadmau5": 4.0,
        "Norah Jones": 5.0,
        "Phoenix": 5.0,
        "Slightly Stoopid": 4.5,
        "The Strokes": 4.0,
        "Vampire Weekend": 4.0
    },
    "Sam": {
        "Blues Traveler": 5.0,
        "Broken Bells": 2.0,
        "Norah Jones": 3.0,
        "Phoenix": 5.0,
        "Slightly Stoopid": 4.0,
        "The Strokes": 5.0
    },
    "Veronica": {
        "Blues Traveler": 3.0,
        "Norah Jones": 5.0,
        "Phoenix": 4.0,
        "Slightly Stoopid": 2.5,
        "The Strokes": 3.0
    }
}


def compute_manhattan(rating1, rating2):
    """计算曼哈顿距离，rating1和rating2参数数据格式均为{'The Strokes': 3.0, 'Slightly Stoopid': 2.5}"""
    distance = 0
    for key in rating1:
        if key in rating2:
            # print(key)
            distance += abs(rating1[key] - rating2[key])
    return distance


def compute_nearest_neighbor(username, users):
    """计算所有用户至username的距离，倒序排列返回结果列表"""
    return sorted([(compute_manhattan(users[username], users[user]), user) for user in users if user is not username])


def recommend(username, users):
    """返回推荐列表"""
    # 找到距离最近的用户
    nearest_neighbor = compute_nearest_neighbor(username, users)[0][1]
    # 找到距离最近用户评分过而username没有评价的乐队
    return sorted(((band, users[nearest_neighbor][band]) for band in users[nearest_neighbor] if
                   band not in users[username]), key=lambda artistTuple: artistTuple[1], reverse=True)


def compute_minkowski(rating1, rating2, r):
    """计算闵可夫斯基距离，r用1表示使用曼哈顿距离，r用2表示使用欧几里得距离"""
    distance = 0
    for key in rating1:
        if key in rating2:
            # pow(x, y)计算x的y次方
            distance += pow(abs(rating1[key] - rating2[key]), r)
    return pow(distance, 1.0 / r)


def pearson(rating1, rating2):
    """计算皮尔逊相关系数"""
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    for key in rating1:
        if key in rating2:
            n += 1
            x = rating1[key]
            y = rating2[key]
            sum_xy += x * y
            sum_x += x
            sum_y += y
            sum_x2 += pow(x, 2)
            sum_y2 += pow(y, 2)
    # 计算分母
    denominator = sqrt(sum_x2 - pow(sum_x, 2) / n) * sqrt(sum_y2 - pow(sum_y, 2) / n)
    if denominator == 0:
        return 0
    else:
        return (sum_xy - (sum_x * sum_y) / n) / denominator


if __name__ == '__main__':
    # print(compute_manhattan(users["Jordyn"], users["Hailey"]))
    ##########
    # print(compute_nearest_neighbor("Hailey", users))
    ##########
    # print(recommend('Hailey', users))
    # print(recommend('Sam', users))
    # print(recommend('Angelica', users))
    ##########
    # print(compute_nearest_neighbor('Angelica', users))
    ##########
    # print(compute_minkowski(users["Angelica"], users["Bill"], 2))
    ##########
    print(pearson(users['Angelica'], users['Bill']))
    print(pearson(users['Angelica'], users['Hailey']))
    print(pearson(users['Angelica'], users['Jordyn']))
