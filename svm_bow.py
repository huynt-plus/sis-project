from sklearn.feature_extraction.text import CountVectorizer
from load_data import load_all_use_of_proceeds, load_all_use_of_proceeds_Detailed_Review_Reporting_Means_of_Disclosure_information_published_in_ad_hoc
from sklearn.model_selection import StratifiedKFold
from sklearn import svm
from sklearn.metrics import classification_report
import numpy as np


x_data, y_data = load_all_use_of_proceeds_Detailed_Review_Reporting_Means_of_Disclosure_information_published_in_ad_hoc()
vectorizer = CountVectorizer()
x_data = vectorizer.fit_transform(x_data)

skf = StratifiedKFold(n_splits=5)
accs = 0
for train_index, test_index in skf.split(x_data, y_data):
	X_train, X_test = x_data[train_index], x_data[test_index]
	y_train, y_test = y_data[train_index], y_data[test_index]
	clf = svm.SVC()
	clf.fit(X_train, y_train)	
	y_pred = clf.predict(X_test)	
	acc = (len(y_pred) -  np.sum(np.abs(y_pred-y_test)))/(len(y_pred)*1.0)
	print ("Acc:",acc)
	accs += acc
	print(classification_report(y_test, y_pred))
	
print ("Avg acc", accs/5)

#92.25 information published in ad hoc
#89.97 information published in financial report
#90.36 information published in sustainability report