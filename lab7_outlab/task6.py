import pandas as pd  
import argparse
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', default='./sml.csv', type=str, help='data file')
    args = parser.parse_args()

    df = pd.read_csv(args.data)
    df_by_instance = df.groupby(['instance'])

    legend_config = {
    'epsilon-greedy-0.002': lambda x,y,label: plt.plot(x, y, color='green', marker='o', linewidth=2, markersize=12,label=label),
    'epsilon-greedy-0.02': lambda x,y,label: plt.plot(x, y, color='red', marker='v', linewidth=2, markersize=12,label=label),
    'epsilon-greedy-0.2': lambda x,y,label: plt.plot(x, y, color='cyan', marker='^', linewidth=2, markersize=12,label=label),
    'kl-ucb': lambda x,y,label: plt.plot(x, y, color='blue', marker='<', linewidth=2, markersize=12,label=label),
    'round-robin': lambda x,y,label: plt.plot(x, y, color='black', marker='>', linewidth=2, label=label),
    'thompson-sampling': lambda x,y,label: plt.plot(x, y, color='magenta', marker='1', linewidth=2, markersize=12,label=label),
    'ucb': lambda x,y,label: plt.plot(x, y, color='burlywood', marker='*', linewidth=2, markersize=12,label=label)
    }
    
    graph_num = 1
    for group_itr in df_by_instance.groups.keys():
        df_instance = df_by_instance.get_group(group_itr)
        df_by_algo = df_instance.groupby(['algorithm', 'epsilon'])
        map = {algo:[] for algo in df_by_algo.groups.keys()}
        for algo_itr in df_by_algo.groups.keys():
            df_algo = df_by_algo.get_group(algo_itr)
            for horizon_itr, df_by_horizon in df_algo.groupby(['horizon']):
                map[algo_itr].append((horizon_itr, df_by_horizon.sample(n=50)['REG'].mean(axis=0)))
        
        plt.xlabel('horizon (log10)') 
        plt.ylabel('REG (log10)')  
        plt.title(group_itr) 

        for k,v in map.items():
            x = np.log10([i[0] for i in v])
            y = np.log10([i[1] for i in v])
            label = (k[0] if k[1] == 0 else k[0] + '-' + str(k[1]))
            legend_config[label](x, y, label)
        plt.legend()
        plt.savefig('instance'+str(graph_num)+'.png')
        graph_num += 1
        plt.clf()
