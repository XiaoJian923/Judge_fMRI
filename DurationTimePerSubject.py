import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calc(data, threshold):
    number = 0
    for i in data:
        if i < threshold:
            number = number + 1
    return number

#TODO: Just modify the threshold parameter

threshold = 3
save_path = 'DurationTimePerSubject'
numbers_dict = {}
want = {}
df1 = pd.read_excel('All_eprime_data.xlsx')
data = df1[['Subject', 'Probe.RT']]


for i in range(48):
    first = i * 30
    end = (i + 1) * 30
    want[data.loc[first]['Subject']] = np.array(data['Probe.RT'][first:end])/1000


# print(want)
for i in want:
    y = want[i]
    number = calc(y, threshold)
    numbers_dict[i] = number
    plt.plot([-1, 30], [threshold, threshold], c='r', label='%ds'%threshold)
    plt.title('Subject-%03d'%i + '   Below threshold Number:%02d'%number)
    plt.plot(y)
    plt.legend()
    plt.savefig(os.path.join(save_path, 'Subject-%03d'%i + '-Below threshold Number-%02d'%number + '.png'))
    # plt.show()
    plt.close()


x_subs = []
heights_subs = []
for i in sorted(numbers_dict.keys()):
    x_subs.append(i)
    heights_subs.append(numbers_dict[i])


plt.bar(x_subs, heights_subs)
plt.title('Overall Below threshold Number:%02d'%sum(heights_subs))
for a, b in zip(x_subs, heights_subs):
    plt.text(a, b, b, ha='center', va='bottom')
plt.savefig(os.path.join(save_path, 'Overall-Below threshold Number-%02d'%sum(heights_subs) + '.png'))
plt.show()










