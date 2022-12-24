import numpy as np
from math import log2

class MultinominalNB():
  def __init__(self, alpha = 1):
    self.alpha = alpha

  def get_info(self):
    return {'prob_class': self.arr_prob_class, 'prob_feature_class': self.arr_prob_feature_class, 'classes': self.classes, 'features': self.features, 'symptoms': self.list_all_symptom}

  def save_model(self, filename):
    return np.save(filename, [self.arr_prob_class, self.arr_prob_feature_class, self.classes, self.features, self.list_all_symptom])
  
  def load(self, filename):
    load = np.load(filename, allow_pickle=True)
    self.arr_prob_class = load[0]
    self.arr_prob_feature_class = load[1]
    self.classes = list(load[2])
    self.features = list(load[3])
    self.list_all_symptom = list(load[4])

  def prob_class(self, c):
    count_c = sum([self.y_train[i] == c for i in range(self.total)])
    return count_c/self.total

  def prob_feature_class(self, f, c):
    count_f = 0
    count_c = 0
    for i in range(self.total):
      if self.y_train[i] == c:
        if self.X_train[i, f] > 0:
          count_f += self.X_train[i, f]
        count_c += sum(self.X_train[i])
    return (count_f + self.alpha)/(count_c + self.alpha*len(self.features))
  
  def fit(self, X_train, y_train, feature, prognosis):
    self.total = len(X_train)
    self.X_train = X_train
    self.y_train = y_train
    self.features = feature
    self.classes = prognosis
    n_classes = len(self.classes)
    n_features = len(self.features)
    self.arr_prob_class = np.zeros(n_classes)
    self.arr_prob_feature_class = np.zeros((n_classes, n_features))
    for i in range(n_classes):
      self.arr_prob_class[i] = self.prob_class(self.classes[i])
      for j in range(n_features):
        self.arr_prob_feature_class[i, j] = self.prob_feature_class(j, self.classes[i])
    self.all_symptoms()

  def prob_test_class(self, test, c):
    prob_test_log2 = log2(self.arr_prob_class[self.classes.index(c)])
    for i in range(len(self.features)):
      prob_feature = self.arr_prob_feature_class[self.classes.index(c), i]
      if test[i] > 0:
        prob_test_log2 += log2(prob_feature)

    return prob_test_log2

  def predict_test(self, test):
    list_prob = [self.prob_test_class(test, c) for c in self.classes]
    return self.classes[list_prob.index(max(list_prob))]
  
  def predict_test_near(self, test):
    list_prob = [self.prob_test_class(test, c) for c in self.classes]
    first_position = list_prob.index(max(list_prob))
    list_prob_temp = [] + list_prob
    list_prob_temp.pop(first_position)
    second_result = self.classes[list_prob.index(max(list_prob_temp))]
    second_position = list_prob_temp.index(max(list_prob_temp))
    list_prob_temp.pop(second_position)
    third_result = self.classes[list_prob.index(max(list_prob_temp))]
    return second_result, third_result

  def accuracy(self, X_test, y_test):
    arr_predict_test = np.array([self.predict_test(X_test[i]) for i in range(len(X_test))])
    return np.sum(y_test == arr_predict_test)/len(y_test)

  def symptoms_disease(self, disease):
    first_flag = True
    symptoms = np.zeros(len(self.features))
    for i in range(self.total):
      if y_train[i] == disease:
        if first_flag:
          symptoms = X_train[i]
          first_flag = False
        else:
          symptoms += X_train[i]
    return list(self.features[i] for i in range(len(self.features)) if symptoms[i] > 0)

  def all_symptoms(self):
    self.list_all_symptom = []
    for disease in self.classes:
      self.list_all_symptom.append(self.symptoms_disease(disease))

  def get_symptoms(self, disease):
    return self.list_all_symptom[self.classes.index(disease)]

  def predict_input_symptoms(self, list_symptom):
    """Predict disease which causes list_symptom"""
    # Convert to np array
    np_symptom = np.zeros(len(self.features))
    for symptom in list_symptom:
      if symptom in self.features:
        np_symptom[self.features.index(symptom)] = 1
    # Predict disease
    disease = self.predict_test(np_symptom)
    return disease

  def predict_near_input_symptoms(self, list_symptom):
    """Get disease near predicted disease which causes list_symptom"""
    # Convert to np array
    np_symptom = np.zeros(len(self.features))
    for symptom in list_symptom:
        if symptom in self.features:
          np_symptom[self.features.index(symptom)] = 1
    # Predict disease
    second_disease, third_disease = self.predict_test_near(np_symptom)
    return second_disease, third_disease