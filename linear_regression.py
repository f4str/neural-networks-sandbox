import numpy as np


class LinearRegression:
	def __init__(self, fit_intercept=True):
		self.weights = []
		self.bias = 0
		self.fit_intercept = fit_intercept
	
	def fit(self, X, y):
		X = np.array(X)
		if len(X.shape) == 1:
			X = X.reshape(-1, 1)
		if self.fit_intercept:
			ones = np.ones((X.shape[0], 1))
			X = np.concatenate((ones, X), 1)
		
		# closed form
		beta = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y)
		
		y_pred = np.dot(X, beta)
		sse = np.sum(np.square(np.subtract(y, y_pred)))
		s_yy = np.sum(np.square(np.subtract(y, np.mean(y))))
		
		# mean squared error loss
		loss = sse / len(y)
		# r^2 accuracy
		acc = 1 - sse / s_yy
		
		if self.fit_intercept:
			self.bias = beta[0]
			self.weights = beta[1:]
		else:
			self.weights = beta
		
		return loss, acc
	
	def predict(self, X):
		return np.dot(X, self.weights) + self.bias
	
	def score(self, X, y):
		y_pred = self.predict(X)
		sse = np.sum(np.square(np.subtract(y, y_pred)))
		s_yy = np.sum(np.square(np.subtract(y, np.mean(y))))
		
		return 1 - sse / s_yy
