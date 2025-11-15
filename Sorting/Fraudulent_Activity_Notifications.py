def activityNotifications(exp, d):
    count = [0] * 201
    for i in range(d):
        count[exp[i]] += 1
    
    def median():
        s = 0
        if d % 2 == 1:
            m = d // 2 + 1
            for i in range(201):
                s += count[i]
                if s >= m:
                    return i
        
        else:
            a = b = None
            m1 = d // 2
            m2 = m1 + 1
            for i in range(201):
                s += count[i]
                if a is None and s >= m1:
                    a = i
                if s >= m2:
                    b = i
                    break
            return (a + b) / 2

    noti = 0
    for i in range(d, len(exp)):
        if exp[i] >= median() * 2:
            noti += 1
        count[exp[i-d]] -= 1
        count[exp[i]] += 1
    
    return noti