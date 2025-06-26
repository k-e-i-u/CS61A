import pysnooper
import icecream as ic

# mutual recursion的例子
# 通过recursion计算一个正整数N是否是even的
@pysnooper.snoop()
def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)
    
@pysnooper.snoop()
def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)

# 作为相互递归的另一个例子，请看一个双人游戏，在这个游戏中，
# 桌子上有 n 个初始鹅卵石。游戏者轮流从桌上取走一颗或两颗卵石，
# 取走最后一颗卵石的游戏者获胜。
# 假设爱丽丝和鲍勃玩这个游戏，各自使用一种简单的策略：
# 爱丽丝总是取出一颗卵石如果桌子上的卵石数量是偶数，
# 鲍勃取出两颗卵石，否则取出一颗。
# 给定 n 个初始卵石，爱丽丝开始，谁会赢得游戏？
# 对这个问题的自然分解是将每个策略封装在自己的函数中。
# 这样，我们就可以在修改一种策略的同时不影响另一种策略，
# 从而保持两者之间的抽象屏障。为了结合游戏的回合性质，这两个函数会在每个回合结束时互相调用。
@pysnooper.snoop()
def play_alice(n):
    if n == 0:
        print("Bob wins!")
    else:
        play_bob(n-1)

@pysnooper.snoop()
def play_bob(n):
    if n == 0:
        print("Alice wins!")
    elif is_even(n):
        play_alice(n-2)
    else:
        play_alice(n-1)


def main():
    """Main function to test all debugging methods."""
    try:
        # result_sum_digits = sum_digits(12345)

        # result_fact_iter = fact_iter(5)

        # result_fact_recur = fact_recur(5)

        # result = is_even(4)

        play_bob(3)  # 测了很多遍，感觉Bob总是赢。
    
    except AssertionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()

