import pandas
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score,StratifiedKFold


def evaluate_model(model, target, feature):
    cv = StratifiedKFold(n_splits=5,shuffle=True,random_state=999)
    f1 = cross_val_score(model,feature,target,cv=cv,scoring='f1')
    accuracy = cross_val_score(model,feature,target,cv=5,scoring='accuracy')
    return accuracy.mean(), f1.mean()


def open_file():
    file_name = input("file name:")
    feature_label = input("feature label:")
    columns_to_remove_amount = int(input("the amount of columns to remove:"))
    t_dataframe = pandas.read_csv(file_name ,encoding='utf-8')
    target = t_dataframe[feature_label]
    if columns_to_remove_amount:
        all_columns = []
        for i in range(columns_to_remove_amount):
            all_columns.append(input("columns to remove:"))
        feature = t_dataframe.drop(columns=[feature_label] + all_columns,axis=1)
    else:
        feature = t_dataframe.drop([feature_label],axis=1)
    return target,feature


def main():
    lda_model = LinearDiscriminantAnalysis()
    tree_model = DecisionTreeClassifier(max_depth=3, random_state=888)
    forest_model = RandomForestClassifier(n_estimators=300, random_state=777)

    models = [lda_model, tree_model, forest_model]
    model_names = ['Linear Discriminant Analysis', 'Decision Tree', 'Random Forest']

    target,feature = open_file()

    for model, name in zip(models, model_names):
        accuracy, f1 = evaluate_model(model, target, feature)
        print(f"{name}:\n Accuracy={accuracy:.3f}, F1 Score={f1:.3f}")


if __name__ == "__main__":
    main()

