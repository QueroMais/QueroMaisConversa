"Plot road map of a user case"

import sys
import json
import matplotlib.pyplot as plt


class PlotUserCase:


    def __init__(self, path):

        # label : (priority, value)
        self.name = path[:-5]
        self.data = json.load(open(path, 'r'))[0]

    def _extract_data(self, data):
        items = data.items()

        user_case_list = []

        for item in items:

            user_case_list.append([item[0], item[1]])

        user_case_list = sorted(user_case_list,
                                key=lambda item: item[1],
                                reverse=True)

        for idx in range(1, len(user_case_list))[::-1]:
            user_case_list[idx -1][1] += user_case_list[idx][1]

        return user_case_list

    def plot_graph(self):

        data = self._extract_data(self.data)

        for each in range(len(data)):

            plt.scatter(each, data[each][1], label=data[each][0])
        data = list(map(lambda x : x[1], data))

        print(range(len(data)))

        plt.xlabel('Tempo')
        plt.ylabel('Prioridade')

        plt.xticks(list(range(len(data))))
        plt.yticks(data)

        plt.title(self.name.replace('_', ' '))

        plt.legend(loc='upper right')
        plt.plot(list(range(len(data))), data , c='black')
        plt.show()

if __name__ == '__main__':
    PlotUserCase(sys.argv[1]).plot_graph()
