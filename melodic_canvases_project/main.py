#we gonna use this file in streamlit for frontend



#preprocess the data
def preprocess():
    pass
    """
    - Query the raw dataset from Le Wagon's BigQuery dataset
    - Cache query result as a local CSV if it doesn't exist locally
    - Process query data
    - Store processed data on your personal BQ (truncate existing table if it exists)
    - No need to cache processed data as CSV (it will be cached when queried back from BQ during training)
    """
    #your code here


    #retrieve data
    #your code here


    #process data
    #your code here

    #load data
    #your code here


#train on processed data and save model weights


def train(learning_rate= , batch_size = , ):
    pass
    """
    - Download processed data from cloud or local
    - Train on the preprocessed dataset
    - Store training results and model weights

    Return val_mae as a float
    """
    #your code here


    # Load processed data using some_get_data_func()
    # Try it out manually on console.cloud.google.com first!
    #your code here

    # Create (X_train_processed, y_train, X_val_processed, y_val)
    #your code here

    # Train model using `model.py`
    #your code here


    #save results and model weights



#evaluate the performance of the latest trained model on new data


def evaluate():
    """
    Evaluate the performance of the latest production model on processed data
    Return MAE as a float
    """
    #your code here

    # Query your BigQuery processed table and get data_processed using `get_data_with_cache`
    #your code here


#make a prediction on a DataFrame with a specific version of the trained model


def pred():
    #Make a prediction using the latest trained model
    #your code here
    pass
