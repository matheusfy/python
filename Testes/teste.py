def merge_the_tools(string, k):
    for i in range(len(string)):
        if i == 0:
            print(list(set(string[i:k])))
            i = k-1
        else:
            print(list(set(string[i:i+k])))
            i = i+k-1
if __name__ == '__main__':

    string, k = 'AAABCADDE', 3
    merge_the_tools(string, k)