## HW 2 Assignment

# import python packages

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import RocCurveDisplay, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis as QDA, LinearDiscriminantAnalysis as LDA
import seaborn as sns

# function to read and prepare the data. 
def read_prep_data():
    
    # 1. indicate path where the data is to be imported from.

    # Modify path to your setup
    # My data was on the C: drive without going into the Users folder. Change accordingly.
    
    dataPath = "C:/ML_AI_Algorithms/HW2/Data/HW2_train_data.csv"

    # 2. Load data as a pandas dataframe

    # pandas read_csv function will load the data as a pandas dataframe. header = 0 to use the first row as the column headers
    train_data= pd.read_csv(dataPath, header = 0)


    # Since we're only working with x1-x15 to predict y
    # I will select only those columns to reduce the dimensions of the pandas dataframe
    # Using iloc to select columns by index, I can generate the list of columns - the first 15 variables for x1-x15 and y by using the -1 index value
    train_data = train_data.iloc[:, list(range(15))+ [-1]]
    

    # variables are declared to be global as we will be using the same data for each model. 
    # However, during each model, we will be splitting the data into training and test datasets with unique seeds (random_state)
    
    global X, y 

    # X contains x1-x15
    X = train_data.iloc[:,0:15]
    # y contains the y column, the last one
    y = train_data.iloc[:,15]
    return X, y

    
def train_model(model):

    if model == 'QDA':
        
        # 3. Split your data for your own training and testing datasets. Make sure to use a random seed

        # Now, let's split the data 80/20 for train and test datasets. I will be using the sklearn train_test_split method
        # To get the same results, the random seed can be set inside the method using random_state. 
        # In this case, I chose 156.
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 156)

        # we can verify that we got the same values back. 
        print("First 5 values in x1 are 0.904918, 0.916862, -1.293618, 1.121028, and 2.846816\n", X_train.head(5)['x1'], sep = '')

        # 4. Investigate the training data (min, max, missings, histogram)

        # To investigate the training data, we can use describe() for the x1-x15 columns

        print("Brief overview of each factor:\n", X_train.describe(), sep = '')

        print("""
              It looks like x1-x10 were generated from a distribution centered around 1-10 
              accordingly (x1 with a mean of 1, x2 with a mean of 2, as so on), with a 
              standard deviation of 1. It's highly likely that the data comes from a Normal distribution. 
              x11-15 do not have a noticeable pattern but I would venture to guess that it 
              came from a Uniform distribution centered at 0 with the min/max set at the 
              corresponding variable's name, i.e. x11 has a max of 11 and a minimum of -11
              """)

        # Any missing values?
        print("Here are the number of missing values in each column:\n" ,X_train.isna().sum(),sep='')

        # Luckily, since this was a dataset that was likely artificially produced, there aren't any missing values 
        # that we need to fill in. Otherwise, I may have considered using the mean value or removing them from the 
        # dataset if there weren't a lot of NA's.

        # We can also generate histograms for each variable. 
        # Don't forget to delete the popup plot to keep code running.
        X_train.hist(bins = 15, figsize = (10,10))
        plt.tight_layout()
        plt.title("Histograms for each predictor variable")
        plt.show()

        print("It seems that my intuition was correct. The variables do follow a Normal and Uniform Distribution.")

        # Let's also take a look at the y column, the values that these 15 predictor variables are attempting to predict
        y_train.reset_index()
        sns.barplot(x = y_train.value_counts().index, y = y_train.value_counts().values)
        plt.title("Barplot showing how many 0's and 1's there are in y_train")
        plt.show()

        print("Here are the number of missing values in the y column:", y_train.isna().sum(), sep = '')

        # Good. No missing values in the y column. Looks like there are a lot more 1's than 0's. This may be something to keep an eye out for during model evaluation...

        # 5. Prepare the datasets for modeling: standardize variables, fill in missing values, etc.

        # I will be standardizing the data regardless of the shape of the distribution using sklearn's StandardScaler method
        # Logistic and linear discriminating analysis are most suitable with this standardization.
        # We can make use of the pipeline method in sklearn to help with processing the training data and putting it into the model

        # The pipeline contains two steps. First scale the data provided to a mean of 0 and a unit variance of 1.
        # Then, run the provided data into the model. In this case, QDA for Quadratic Discriminant Analysis
        pipeline = make_pipeline(StandardScaler(), QDA())

        # 6. Use at least 3 models and train them on the training data (QDA here, first model)

        # Code to scale the data and feed to QDA model
        pipeline.fit(X_train,y_train)

        # You can find the model accuracy by scaling the testing set and running it through the QDA model. 
        print("Model accuracy: ", pipeline.score(X_test, y_test))

        #7. Plot the ROC and find the AUC for each model on both the train and test datasets.

        # Generate the ROC plot/AUC value by using this method.
        # We're interested in this for both train and test datasets.
        # A good AUC value on the training dataset tells us that the model is learning as it should.
        # A good AUC value on the testing dataset tells us that the model is performing well on unseen data.
        RocCurveDisplay.from_estimator(pipeline, X_train, y_train)
        plt.title("QDA: AUC Value and ROC curve for training data")
        plt.show()


        # Here we look at the ROC plot and AUC value for the test dataset in the model.
        y_pred = pipeline.decision_function(X_test)

        RocCurveDisplay.from_predictions(y_test, y_pred)
        plt.title("QDA: AUC Value and ROC curve for testing data")
        plt.show()

        # I was also interested in looking at the precision, recall and weighted F1 score.
        y_pred_test = pipeline.predict(X_test)
        
        # Classification report for precision, recall and weighted F1 score.
        print(classification_report(y_test, y_pred_test))
        
        # Confusion matrix for testing data
               
        cmatrix(y_test, y_pred_test, "test")

        # Confusion matrix for training data.
        
        # predicted y values from training data
        y_pred_train = pipeline.predict(X_train)

        cmatrix(y_train, y_pred_train, "train")   

        # this function asks whether or not you want to do another model or not. See below for the code.
        cont()

    #############################
    # Let's move to Logistic Regression. We need to re-split our training and testing set. 
    # I'll use the random seed of 387. We'll need to investigate the data again.
    # I won't be making as many comments here as the code is roughly re-used.
    #############################
            
    if model == 'LR':
        
        # 3. Split the data into train/test datasets.

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 387)
        # we can verify that we got the same values back.
        print("First 5 values in x1 are 0.16877, 0.452884, 3.657831, 0.15843, 1.14582\n", X_train.head(5)['x1'], sep = '')

        # 4. Investigate the training data (min, max, missings, histogram)

        # To investigate the training data at a glance, we can use describe()

        print("Brief overview of each factor:\n", X_train.describe(), sep = '')

        # Same as before, histograms look roughly the same.
        print("""
              It looks like x1-x10 were generated from a distribution centered around 1-10 
              accordingly (x1 with a mean of 1, x2 with a mean of 2, as so on), with a 
              standard deviation of 1. It's highly likely that the data comes from a Normal distribution. 
              x11-15 do not have a noticeable pattern but I would venture to guess that it 
              came from a Uniform distribution centered at 0 with the min/max set at the 
              corresponding variable's name, i.e. x11 has a max of 11 and a minimum of -11
              """)
        
        # Missing values
        print("Here are the number of missing values in each column:\n" ,X_train.isna().sum(),sep='')

        # We can also generate histograms for each variable. 
        
        X_train.hist(bins = 15, figsize = (10,10))
        plt.tight_layout()
        plt.title("Histograms for each predictor variable")
        plt.show()

        print("It seems that my intuition was correct. The variables do follow a Normal and Uniform Distribution")

        # Again, investigate how the training data looks for the y column.
        y_train.reset_index()
        sns.barplot(x = y_train.value_counts().index, y = y_train.value_counts().values)
        plt.title("Barplot showing how many 0's and 1's there are in y_train")
        plt.show()

        print("Here are the number of missing values for the y column: " ,y_train.isna().sum(),sep='')

        # 5. Prepare the datasets for modeling: standardize variables, fill in missing values, etc.

        pipeline = make_pipeline(StandardScaler(), LogisticRegression())

        # 6. Use at least 3 models and train them on the training data. (Logistic Regression here, second model)
        pipeline.fit(X_train,y_train)

        print("Model accuracy: ", pipeline.score(X_test, y_test))

        # 7. Plot the ROC and find the AUC value for both training and testing datasets.

        # ROC/AUC for training
        RocCurveDisplay.from_estimator(pipeline, X_train, y_train)
        plt.title("LogReg: AUC Value and ROC curve for training data")
        plt.show()

        # ROC/AUC for testing
        y_pred = pipeline.decision_function(X_test)

        RocCurveDisplay.from_predictions(y_test, y_pred)
        plt.title("LogReg: AUC Value and ROC curve for testing data")
        plt.show()

        y_pred_test = pipeline.predict(X_test)
        # Classification report for precision, recall and weighted F1 score.
        print(classification_report(y_test, y_pred_test))
        
        # Confusion matrix for testing data
        
        
        cmatrix(y_test, y_pred_test, "test")

        # Confusion matrix for training data.
        
        # predicted y values from training data
        y_pred_train = pipeline.predict(X_train)

        cmatrix(y_train, y_pred_train, "train")

        # call function to choose another model. See below for the code.
        cont()

    #################################
    # THIS SECTION IS FOR LDA MODEL. Seed has been set to 578. This is the third and final model. 
    #################################       
    if model == 'LDA':

        # 3. Split the data into train/test datasets.
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 578)
        # we can verify that we got the same values back.
        print("First 5 values in x1 are 1.293178,-0.538069, -0.032293, 0.225572, -0.280648\n", X_train.head(5)['x1'], sep = '')


        # 4. Investigate the training data (min, max, missings, histogram)
        # To investigate the training data at a glance, we can use describe()

        print("Brief overview of each factor:\n", X_train.describe(), sep = '')

        print("""
              It looks like x1-x10 were generated from a distribution centered around 1-10 
              accordingly (x1 with a mean of 1, x2 with a mean of 2, as so on), with a 
              standard deviation of 1. It's highly likely that the data comes from a Normal distribution. 
              x11-15 do not have a noticeable pattern but I would venture to guess that it 
              came from a Uniform distribution centered at 0 with the min/max set at the 
              corresponding variable's name, i.e. x11 has a max of 11 and a minimum of -11
              """)
        
        print("Here are the number of missing values in each column:\n" ,X_train.isna().sum(),sep='')

        # We can also generate histograms for each variable. 
        
        X_train.hist(bins = 15, figsize = (10,10))
        plt.tight_layout()
        plt.title("Histograms for each predictor variable")
        plt.show()

        print("It seems that my intuition was correct. The variables do follow a Normal and Uniform Distribution")

        # Again, investigate how the training data looks for the y column.
        y_train.reset_index()
        sns.barplot(x = y_train.value_counts().index, y = y_train.value_counts().values)
        plt.title("Barplot showing how many 0's and 1's there are in y_train")
        plt.show()
       
        print("Here are the number of missing values for the y column: " ,y_train.isna().sum(),sep='')

        # 5. Prepare the datasets for modeling: standardize variables, fill in missing values, etc.

        pipeline = make_pipeline(StandardScaler(), LDA())

        # 6. Use at least 3 models and train them on the training data. (Linear Discriminant Analysis here, third and final model)
        pipeline.fit(X_train,y_train)

        print("Model accuracy: ", pipeline.score(X_test, y_test))


        # 7. Plot the ROC and find the AUC value for both training and testing datasets.

        # ROC/AUC for training data.
        RocCurveDisplay.from_estimator(pipeline, X_train, y_train)
        plt.title("LDA: AUC Value and ROC curve for training data")
        plt.show()


        # ROC/AUC for testing data.
        y_pred = pipeline.decision_function(X_test)

        RocCurveDisplay.from_predictions(y_test, y_pred)
        plt.title("LDA: AUC Value and ROC curve for testing data")
        plt.show()

        # predicted y values using testing set
        y_pred_test = pipeline.predict(X_test)
        # Classification report for precision, recall and weighted F1 score.
        print(classification_report(y_test, y_pred_test))
        
        # Confusion matrix for testing data
        
        
        cmatrix(y_test, y_pred_test, "test")

        # Confusion matrix for training data.
        
        # predicted y values from training data
        y_pred_train = pipeline.predict(X_train)

        cmatrix(y_train, y_pred_train, "train")
        
        cont()

# function that takes in two arrays: actual y values and the predicted y values. Generates confusion matrix plot.
def cmatrix(y_actual, y_predict, string):
    cm = confusion_matrix(y_actual, y_predict)

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(cm)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
    ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
    ax.set_ylim(1.5, -0.5)
    for i in range(2):
        for j in range(2):
            ax.text(j, i, cm[i, j], ha='center', va='center', color='red')
    if string == "train":
        plt.title("Confusion matrix for training data")
    elif string == "test":
        plt.title("Confusion matrix for test data")
    else: 
        print("Enter valid string: train or test")
    plt.show()
    
# Function that is called at the end of each model fitting and evaluation to see if you'd like to 
# run another model or move onto the final conclusion.
def cont():

    # take down the input provided by user. Use upper method to make the string all uppercase. Not case sensitive answers.
    c = input("Would you like to try another model? Y/N: ").upper()
    
    # Check for valid inputs. Call function again to prompt for another input.
    if c not in ['Y','N']:
        print("Please select a valid response")
        return cont()
    # If the answer is Yes, send them back to choose the model.
    if c == 'Y': 
        select_model()
    else: 
        # otherwise, the answer is No and they want to read the conclusion, presumably after seeing all three models. 
        conclusion()
    

# Function to select which model to run. 
def select_model():

    # input from keyboard is automatically upper-cased so selection is not case sensitive.
    m = input("Please select the model you'd like to use. QDA, LR, LDA: ").upper()
    
    # however, if selection is not within the following options, ask to select the model again. 
    if m not in ['QDA','LR', 'LDA']: 
        print("Your selection was invalid. Please try again")
        select_model()
    # if valid selection is made, send the inputted string to the train_model function.
    else: 
        return train_model(m)


# 8. Comment on your findings: how do the 3 models compare? Do you see any overfitting or concerns with your models?
def conclusion():
    
    print("""
          Across all models, the accuracy was roughly 84-85%. I'd say that the model performed decently well but it 
          definitely could have performed better (maybe aim for >90%). However, it is not good practice to compare using 
          the accuracy. Instead, we should compare models on the weighted F1 values. These values is calculated from using 
          both the precision and recall, so it provides a better comparison across classification models. We see that it is 
          roughly 0.81 in each of the three models. This suggests that each of the models are performing similarly. Additionally, 
          there is no clear evidence of overfitting for these models. The tell-tale sign for that would be a clear difference 
          between model accuracy, with the model performing exceptionally well on training data and very poorly on test data. 
          However, we're getting pretty much the same results for both training and test data, which indicates that the 
          model is performing as intended. The performance on the test set reflects what it learned in the training set, 
          hence the similar AUC/ROC curves. However, there is one area of concern with all three models. There was a 
          very low recall value (around 0.20) for 0's which means the model is not correctly identifying all 0's. My concern 
          with the dataset is that this is an imbalanced dataset i.e. there are much more 1's in the dataset, both in 
          the training and test split. That is why the model learns well and can identify correctly on the 1's but very 
          poorly on the 0's. Imbalanced datasets can be common problems when dealing with classification problems and there 
          are ways to combat it. One such way is to cut down randomly on the majority group until it is similar in size to the 
          minority group. Although a simple fix, it comes with major disadvantages such as losing useful information in the 
          training data and losing the representation of the population, thus possibly making the model unable to properly
          generalize on unseen data. The alternative is to increase the number of the minority group to the size of the
          majority group. This means no information is actually lost, but the replication process might increase the chances
          of overfitting the model. There are also some cases where decision trees perform well even with imbalanced datasets 
          so it may be worth it to research which algorithm you should choose if this problem persists even after trying 
          with the first two solutions that I presented.
          """)

if __name__ == "__main__":
    print("Welcome to HW2, you will be selecting a model out of three options. If code does not seem to run, don't forget to close the plot if it popped out.")
    print("You will be seeing histogram plots, barplots, ROC/AUC plots, and confusion matrices.")
    print("Your model choices are Quadratic Discriminant Analysis, Logistic Regression, and Linear Discriminant Analysis.")
    global X,y
    read_prep_data()
    select_model()

    
    