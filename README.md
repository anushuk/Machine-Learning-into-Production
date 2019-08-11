# Data-Science-test
Assignment for ALIZ

## 1) 1_Basics

The `1_Basics` folder contains contains two folder `Flask_app` and `model_build`

### 1.1) model_build
The `model_build` folder contains `main.py` file which builds the logistic regression model using dataset stored in folder `Data` in the  root directory.
The model is succcessfully saved at `1_Basics\Flask_app\pklobjects\`

To build the logistic regression model again just navigate to `1_Basics\model_build\` directory and run `python main.py`

### 1.2) Flask_app

The `Flask_app` folder contains the <b> Flask app </b> that deploys the already built model into production

#### To run the model locally
1) Create a virtual environment by installing all dependencies listed in `1_Basics\Flask_app\requirements.txt` file
2) Just navigate to `1_Basics\Flask_app\` directory and run `python main.py`
3) This will run the flask app at http://localhost:8000/ 
4) In case you want to change the port navigate to `1_Basics\Flask_app\main.py` and change port in `app.run(host='localhost', port=8000, debug=True)`

#### To deploy the model in Google Cloud
1) Download and put your gcloud JSON service key to `1_Basics\Flask_app\`
2) Navigate to `1.Basics\Flask_app\main.py ` and put the following command there `os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="<key.json>"` replace <key.json> with your JSON service key file name.
3) Navigate to `1_Basics\Flask_app\main.py` and change the command `app.run(host='localhost', port=8000, debug=True)` to `app.run(debug=Fasle)`
4)Upload folder `1_Basics\Flask_app\` to your Gcloud console
5)Navigate to folder where your `app.yaml` file is stored and run `gcloud init` and then `gcloud app deploy`

## 2) 2_custom_estimator




 


  




