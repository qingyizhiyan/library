from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pyreadstat

def Linear(for_feature,for_target,to_feature,to_target):
    model = LinearDiscriminantAnalysis()
    model.fit(for_feature,for_target)
    print(model.score(to_feature,to_target))
def Tree(for_feature,for_target,to_feature,to_target):
    tree = DecisionTreeClassifier(max_depth=3,random_state=888)
    tree.fit(for_feature,for_target)
    print(tree.score(to_feature,to_target))
def Ramdom_forest(for_feature,for_target,to_feature,to_target):
    forest = RandomForestClassifier(n_estimators=100,random_state=777)
    forest.fit(for_feature,for_target)
    print(forest.score(to_feature,to_target))
def Nerve(for_feature,for_target,to_feature,to_target):
    nerve = MLPClassifier(solver='lbfgs',random_state=111,hidden_layer_sizes=[10,10],alpha=0.6,max_iter=10000)
    nerve.fit(for_feature,for_target)
    print(nerve.score(to_feature,to_target))
RiskLoan_dataframe,meta=pyreadstat.read_sav(r"C:\Users\apexon\Downloads\信用还贷风险判别.sav",encoding='GBK')
RiskLoan_unknown = RiskLoan_dataframe[RiskLoan_dataframe['违约'].isnull()==True]
feature_unknown = RiskLoan_unknown.drop(['违约'],axis=1)
RiskLoan_dataframe = RiskLoan_dataframe[RiskLoan_dataframe['违约'].isnull()==False]
target = RiskLoan_dataframe['违约']
feature = RiskLoan_dataframe.drop(['违约'],axis=1)
feature_train,feature_test,target_train,target_test = train_test_split(feature,target,stratify=target,random_state=999)

Linear(feature_train,target_train,feature_test,target_test)
Tree(feature_train,target_train,feature_test,target_test)
Ramdom_forest(feature_train,target_train,feature_test,target_test)
Nerve(feature_train,target_train,feature_test,target_test)