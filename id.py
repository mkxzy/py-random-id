# 生成不重复ID
import random

# ID取值范围
id_pool = set([x for x in range(100000, 1000000)])

# 已经被使用的ID列表
id_used = set([100000, 200000])

# 求集合的差得到可用的ID
id_available = id_pool - id_used

# 从可用ID列表中随机取一个ID
id = random.choice(list(id_available))
print(id)
