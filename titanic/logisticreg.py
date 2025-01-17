import numpy as np
from sklearn.preprocessing import StandardScaler
def sigmoid(x):
    return 1/(1+np.exp(-x))

class LogisticRegression():
    
    def __init__(self,lr=0.1,n_iters=1000):
        self.lr=lr
        self.n_iters=n_iters
        self.weights=None
        self.bias=None
    
    def fit(self,X,y):
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        y_scaled = scaler.transform(y)
        n_samples,n_features=X_scaled.shape
        self.weights=np.zeros(n_features)
        self.bias=0

        for _ in range(self.n_iters):
            linear_pred=np.dot(X_scaled,self.weights)+self.bias
            predictions=sigmoid(linear_pred)

            dw=(1/n_samples)* np.dot(X.T,(predictions-y_scaled))
            db=(1/n_samples)* np.sum(predictions-y_scaled)

            self.weights=self.weights-self.lr*dw
            self.bias=self.bias=self.lr*db
    
    def predict(self,X):
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        linear_pred=np.dot(X,self.weights)+self.bias
        y_pred=sigmoid(linear_pred)
        class_pred=[0 if y<=0.5 else 1 for y in y_pred]
        return class_pred