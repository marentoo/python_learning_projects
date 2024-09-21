import pandas as pd

def prep(file):
    a_list = []
    with open(file, "r") as f:
        for line in f:
            a_list.append(line)
    return a_list


#chose smaller number e.g. first 200
def to_df(a_list):
    a_list = a_list[:201]
    words = [word.split()[0] for word in a_list if word.split()[0].isalpha()]
    df = pd.DataFrame(words, columns=["words"])
    return df

