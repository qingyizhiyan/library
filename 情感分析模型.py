import pandas
from snownlp import SnowNLP

def open_file():
    file_name = input("file name:")
    dataframe = pandas.read_csv(file_name ,encoding='GBK')
    chosen_columns = input("choose columns:")
    return chosen_columns,dataframe


def text_analyze(text):
    return SnowNLP(text).sentiments


def main():
    chosen_columns,dataframe = open_file()
    dataframe['score'] = dataframe[chosen_columns].apply(text_analyze)
    print(dataframe)


if __name__ == "__main__":
    main()
