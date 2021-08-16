import pandas as pd
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import dill

def main():
    clf = SGDClassifier()

    # Entrada de datos
    df = pd.read_csv("data/data.csv", sep = "|")
    print(df.head(5))
    print(df["y"].value_counts())

    # Variables
    random_state = 1
    features = ["sepal length (cm)","sepal width (cm)","petal length (cm)","petal width (cm)"]
    label = "y"

    # Preprocesamiento
    X_train, X_test, y_train, y_test = train_test_split(
        df[features], 
        df[label], 
        test_size = 0.20, 
        random_state = random_state
    )

    # Entrenamiento
    clf.fit(X_train, y_train)

    # Coefficientes
    print("coef: ", clf.coef_)
    print("inter: ", clf.intercept_)

    # Métricas
    print("score in: ", clf.score(X_train, y_train))
    print("score out: ", clf.score(X_test, y_test))

    y_pred = clf.predict(X_test)
    cmdf = pd.DataFrame(
        confusion_matrix(y_test, y_pred),
        columns = [0,1,2],
        index = [0,1,2]
    )
    print(cmdf)

    #print(classification_report(y_test, y_pred))

    # Exportar modelo
    with open('model/model.pkl', 'wb') as file:
        dill.dump(clf, file)

if __name__ == '__main__':
    main()