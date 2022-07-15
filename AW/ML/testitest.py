import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

mnist = fetch_openml('mnist_784', version=1)

# mnist is a dictionary, with the following keys
print(mnist.keys())

# Use mnist['DESCR'] to read more information about the data
# Extract features and labels
X = np.c_[mnist['data']]
y = np.c_[mnist['target']].reshape(-1)

# investigate data
print(X.shape)  # 70000 images, with 784 pixels
print(y.shape)  # 70000 labels of which number the picture is of

# extract single digit
instance_index = 2
single_digit = X[instance_index, :]
single_digit_image = single_digit.reshape(28, 28)

# plot the digit

plt.imshow(single_digit_image, cmap='binary')
plt.axis('off')
plt.show()

# each instance is a and drawn digit between 0 and 1 (28X28 pixels equals 784 flatten pixels)
print(y[instance_index])
print(type(y[instance_index]))  # every label is a string

# change labels to number
y = y.astype(np.uint8)
print(type(y[instance_index]))  # every label is now numeric

# np.max(X)

X = X / 255

y_train_is5 = (y == 5)*1


X_train, X_test, y_train, y_test = train_test_split(
    X, y_train_is5, test_size=0.1, random_state=420)


model = LogisticRegression(max_iter=1000)
model.fit(X=X_train, y=y_train)
y_pred = model.predict(X_test)

confusion_matrix(y_true=y_test, y_pred=y_pred)
# array([[6333,   49],
#       [ 109,  509]], dtype=int64)
# precision = 509 / (509 + 49)   0.91
# recall = 509 / (509 + 109)      0.82

constant_0 = [0 for x in range(63000)]
confusion_matrix(y_true=y_test, y_pred=constant_0)
# array([[57305,     0],
#        [ 5695,     0]], dtype=int64)
# precision_0 = 0 / (0 + 0)          0
# recall0 = 0 / (0+5695)             0

y_pred_prob = model.predict_proba(X_test)


def threshold_for_1(threshold, array):
    """denne funksjonen er sjuk

    Args:
        threshold (float): float som skal brukes som threshold
        array (array): arrayen den skal sjekke

    Returns:
        list: liste med 1 og 0
    """
    ls = []
    for i in array:
        if i[1] > threshold:
            ls.append(1)
        else:
            ls.append(0)
    return ls


adjusted_prob = threshold_for_1(0.1, y_pred_prob)
confusion_matrix(y_true=y_test, y_pred=adjusted_prob)
# array([[57147,   158],
#      [ 1799,  3896]], dtype=int64)
# precision_1 = 3896 / (3896 + 158)   0.96
# recall_1 = 3896 / (3896 + 1799)     0.68
