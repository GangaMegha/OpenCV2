import sklearn.metrics as met
from sklearn.ensemble import BaggingClassifier
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

class_labels=[]
for i in range(1,30):
	class_labels.append('class'+str(i))


X_train=np.loadtxt('X_train_p.csv', delimiter=',')
X_validate=np.loadtxt('X_validate_p.csv', delimiter=',')
#X_test=np.loadtxt('X_test_p.csv', delimiter=',')
Y_train=np.loadtxt('Y_train.csv', delimiter=',') 
Y_validate=np.loadtxt('Y_validate.csv', delimiter=',')

bagging = BaggingClassifier(KNeighborsClassifier(),max_samples=0.5, max_features=0.5)


neigh = KNeighborsClassifier(n_neighbors=5)
neigh.fit(X_train, Y_train) 

Y_out=neigh.predict(X_validate)
print(met.classification_report(Y_validate, Y_out, target_names=class_labels))
#np.savetxt("results\Y_out.csv", Y_out, fmt='%d',delimiter=',', newline='\n', header='id,label',comment=None)
