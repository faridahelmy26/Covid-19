import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

def evaluate_model(model, test_generator):
    y_true = test_generator.classes
    y_pred = np.argmax(model.predict(test_generator), axis=1)

    print(confusion_matrix(y_true, y_pred))
    print(classification_report(y_true, y_pred))