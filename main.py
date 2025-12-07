#import random

def simulate_game(prob_a):
    """模拟一局比赛，prob_a是A选手每球获胜的概率"""
    score_a, score_b = 0, 0
    while True:
        # 模拟每球胜负
        if random.random() < prob_a:
            score_a += 1
        else:
            score_b += 1
        # 判断该局胜负（11分制，领先2分）
        if (score_a >= 11 or score_b >= 11) and abs(score_a - score_b) >= 2:
            return 1 if score_a > score_b else 0

def simulate_match(prob_a, best_of):
    """模拟一场比赛（best_of为总局数，如3局2胜则best_of=3）"""
    wins_a, wins_b = 0, 0
    for _ in range(best_of):
        if simulate_game(prob_a):
            wins_a += 1
        else:
            wins_b += 1
        # 判断比赛胜负
        if wins_a > best_of//2 or wins_b > best_of//2:
            break
    return 1 if wins_a > wins_b else 0

# 示例：模拟1000次5局3胜比赛，A选手每球胜率0.6
num_simulations = 1000
prob_a = 0.6
best_of = 5
a_wins = sum(simulate_match(prob_a, best_of) for _ in range(num_simulations))
print(f"A选手获胜概率: {a_wins/num_simulations:.2f}") 在这个文件里编写代码
