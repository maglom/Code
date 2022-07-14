from cgi import test

import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

mnist = fetch_openml('mnist_784', version=1)

# mnist is a dictionary, with the following keys 
print(mnist.keys())
# Use mnist['DESCR'] to read more information about the data
#Extract features and labels
X = np.c_[mnist['data']]
y = np.c_[mnist['target']].reshape(-1)
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
# np.max(X)

X_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=420)
X_train_prep = X_train / 255
x_test_prep = x_test / 255

y_train_is5 = []
for i in y_train:
    if i == 5:
        y_train_is5.append(i)
    else:
        y_train_is5.append(0)

model = LogisticRegression()
model.fit(X=X_train_prep, y=y_train_is5)
y_pred = model.predict(X_train_prep)

confusion_matrix(y_true=y_train_is5, y_pred=y_pred)
# array([[56860,   445],
#        [  990,  4705]], dtype=int64)
#precision = 4705 / (4705 + 1522)   0.75
#recall = 4075 / (4705 + 1325)      0.67

constant_0 = [0 for x in range(63000)]
confusion_matrix(y_true=y_train_is5, y_pred=constant_0)
# array([[57305,     0],
#        [ 5695,     0]], dtype=int64)
#precision_0 = 0 / (0 + 0)          0
#recall0 = 0 / (0+5695)             0

y_pred_prob = model.predict_proba(X_train_prep)
def threshold_for_1(threshold, array):
    ls = []
    for i in array:
        if i[1] > threshold:
            ls.append(5)
        else:
            ls.append(0)
    return ls
adjusted_prob = threshold_for_1(threshold=0.75, array=y_pred_prob)
confusion_matrix(y_true=y_train_is5, y_pred=adjusted_prob)
#array([[57147,   158],
#      [ 1799,  3896]], dtype=int64)
#precision_1 = 3896 / (3896 + 158)   0.96
#recall_1 = 3896 / (3896 + 1799)     0.68