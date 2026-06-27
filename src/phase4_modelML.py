import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
# Load Phase 3 Data
X, y, vectorizer = pickle.load(open("data/processed_data.pkl", "rb"))

print("Data loaded successfully")

# Train / Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Data split completed")

# Train Models
# Logistic Regression
lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train, y_train)
lr_preds = lr_model.predict(X_test)
lr_accuracy = accuracy_score(y_test, lr_preds)
print("Logistic Regression Accuracy:", lr_accuracy)

# Linear SVC
svc_model = LinearSVC()
svc_model.fit(X_train, y_train)
svc_preds = svc_model.predict(X_test)
svc_accuracy = accuracy_score(y_test, svc_preds)
print("LinearSVC Accuracy:", svc_accuracy)

# Show Report of each model
print("\nLogistic Regression Report:")
print(classification_report(y_test, lr_preds))

# Confusion Matrix for Logistic Regression
cm = confusion_matrix(y_test, lr_preds)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Negative", "Neutral", "Positive"]
)

disp.plot(cmap="Blues")
plt.title("Logistic Regression Confusion Matrix")
plt.show()

print("\nLinearSVC Report:")
print(classification_report(y_test, svc_preds))

# Choose the best model (best accuracy)
if svc_accuracy > lr_accuracy:
    best_model = svc_model
    model_name = "LinearSVC"
else:
    best_model = lr_model
    model_name = "LogisticRegression"

print("Best model selected:", model_name)

# Save best model
pickle.dump(best_model, open("models/sentiment_model.pkl", "wb"))
pickle.dump(vectorizer, open("models/vectorizer.pkl", "wb"))