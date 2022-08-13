import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

mnist = fetch_openml('mnist_784', version=1)

# mnist is a dictionary, with the following keys 
print(mnist.keys())

# Use mnist['DESCR'] to read more information about the data
#Extract features and labels
X = np.c_[mnist['data']]
y = np.c_[mnist['target']]

# investigate data
print(X.shape) # 70000 images, with 784 pixels
print(y.shape) # 70000 labels of which number the picture is of

# extract single digit
instance_index = 2
single_digit = X[instance_index,:]
single_digit_image = single_digit.reshape(28,28)

# plot the digit
import matplotlib.pyplot as plt
plt.imshow(single_digit_image, cmap='binary')
plt.axis('off')
plt.show()

# each instance is a and drawn digit between 0 and 1 (28X28 pixels equals 784 flatten pixels)
print(y[instance_index])
print(type(y[instance_index])) # every label is a string

# change labels to number
y=y.astype(np.uint8)
print(type(y[instance_index])) # every label is now numeric
np.max(X)


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.1, random_state=420)

X_train_prep = X_train/255

for i in y_train:
    if i != 5:
        i = 0

model = LogisticRegression()
model.fit(X_train_prep, y_train)
model.predict(X_train_prep)
model.predict_proba(X_train_prep)