# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import category_encoders as ce
from sklearn.metrics import mean_squared_error
d1 = pd.read_excel('ML Main/traning.xlsx')
d2 = pd.read_excel('ML Main/test_dump.xlsx')
# for x in count:
#     print(x)
# print(len(d1.iloc[:,4]))
# print(type(count))
# Create a synthetic dataset
data = {
    'prob': d1.iloc[:,3].tolist(),
    'size': d1.iloc[:,4].tolist(),
    'tech_sc': d1.iloc[:,6].tolist()
}
df = pd.DataFrame(data)

# Separate features (X) and target variable (y)
X = df[['prob', 'size', 'tech_sc']]
y = d1.iloc[:,5].tolist()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Binary Encoding:
binary_encoder = ce.BinaryEncoder(cols=['prob'])
X_train_binary = binary_encoder.fit_transform(X_train[['prob']])

# Build linear regression model
model_binary = LinearRegression().fit(X_train_binary, y_train)

# Evaluate model on the test set
X_test_binary = binary_encoder.transform(X_test[['prob']])
y_pred_binary = model_binary.predict(X_test_binary)
mse_binary = mean_squared_error(y_test, y_pred_binary)
print(f"Binary Encoding Model - Mean Squared Error: {mse_binary}")