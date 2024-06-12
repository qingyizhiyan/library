import pandas
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score


def evaluate_model(model, feature_train, target_train, feature_test, target_test):
    model.fit(feature_train, target_train)
    y_pred = model.predict(feature_test)
    accuracy = model.score(feature_test, target_test)
    f1 = f1_score(target_test, y_pred)
    return accuracy, f1


def main():
    t_dataframe = pandas.read_csv(r"C:\Users\apexon\Downloads\Titantic.csv", encoding='GBK')
    target = t_dataframe['Survived']
    feature = t_dataframe.drop(['Survived'], axis=1)
    feature_train, feature_test, target_train, target_test = train_test_split(feature, target, stratify=target, random_state=999)

    lda_model = LinearDiscriminantAnalysis()
    tree_model = DecisionTreeClassifier(max_depth=3, random_state=888)
    forest_model = RandomForestClassifier(n_estimators=100, random_state=777)

    models = [lda_model, tree_model, forest_model]
    model_names = ['Linear Discriminant Analysis', 'Decision Tree', 'Random Forest']

    for model, name in zip(models, model_names):
        accuracy, f1 = evaluate_model(model, feature_train, target_train, feature_test, target_test)
        print(f"{name}:\n Accuracy={accuracy}, F1 Score={f1}")


if __name__ == "__main__":
    main()
