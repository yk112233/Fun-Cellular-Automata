import random
import numpy as np
import matplotlib.pyplot as plt
import math
import time

def get_neighbors(i, j, M, N):
    ans = []
    for p in [i-1, i, i+1]:
        for q in [j-1, j, j+1]:
            if(p<0 or p>=M or q<0 or q>=N):
                continue
            else:
                ans.append((p, q))
    
    ans.remove((i, j))
    return ans

def conway(State):
    for i in range(State.shape[0]):
        for j in range(State.shape[1]):
            cnt = 0
            for x in get_neighbors(i, j, State.shape[0], State.shape[1]):
                if(State[x]!=0):
                    cnt += 1
            
            if cnt == 3:
                State[i, j] = 1
            if cnt < 2 or cnt > 3:
                State[i, j] = 0
            if cnt == 2 or cnt == 3:
                pass


def main():
    M, N = 100, 100
    State = np.zeros((M, N))
    for i in range(200):
        x = random.randint(0, 2500-1)
        State[int(x/50), x%50] = 1

    figure, ax = plt.subplots()
    ax.grid(color='r', lw=10, ls='-.')
    for k in range(10000):
        # plt.clf()
        ax.cla()
        conway(State)
        ax.matshow(State)
        plt.pause(0.1)


if __name__ == "__main__":
    main()