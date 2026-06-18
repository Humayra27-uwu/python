def list_of_rewards(gold,count):
    rewards = []
    for i in range(1,count+1):
        rewards.append(gold*i)
    return rewards
print(list_of_rewards(100, 5))