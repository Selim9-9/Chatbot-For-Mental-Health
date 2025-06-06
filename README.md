# Chatbot Project

Welcome to the Chatbot Project! This repository contains code for a chatbot along with tools for local usage, data augmentation, and more.

This is a multiclassification task of building a chatbot model, not a generative model, so the users' answers are fixed but the model will choose the best responses to users' inputs.

## Live Usage:

- **Try the Chatbot Online:**

-![Chatbot_interface](Screenshots/interface.JPG)
  [Chatbot Live website](http://mental-health-ai.up.railway.app)  
  _*Link will be updated soon when the project is uploaded.*_
  
## Local Setup

If you want to run the chatbot locally, please follow these steps:

1. **Download the Pretrained Word2Vec Model:**  
   The chatbot uses a pretrained model named `GoogleNew-Negatie-300.bin`.  
   - **Download Link:** [GoogleNew-Negatie-300.bin](https://www.kaggle.com/datasets/sandreds/googlenewsvectorsnegative300)  
   _*Make sure to download this file before running the project.*_

2. **Install Required Packages:**  
   All necessary packages are listed in the `requirements.txt` file. You can install them by running the following command in your terminal:

   ```bash
   pip install -r requirements.txt
   ```

3. **Notebooks & Dataset on Kaggle:**  
   The two notebooks for this project and the new dataset generated are available on Kaggle:
   - [Mental Health Chatbot Notebook](https://www.kaggle.com/code/selimkhaled50/complete-mental-health-chatbot)
   - [Chatbot New Dataset](https://www.kaggle.com/datasets/selimkhaled50/new-data)
   
## Technical Highlights:
- Leveraged LSTM neural networks for natural language understanding
- Applied data augmentation using the Pegasus paraphrasing model to balance 70+ conversation intents
- Deployed by Flask framework
- Implemented Word2Vec embeddings for semantic understanding
- Achieved ~75% accuracy on validation data after 40 training epochs Achieved ~70% accuracy on test data
 ![the result](Screenshots/model_performance.png)
## Data Augmentation

This project also includes a `data_augmentation` folder where additional experiments were conducted in a separate environment, to solve the problem of data imbalance, The original data comes from this [Link](https://www.kaggle.com/datasets/elvis23/mental-health-conversational-data).
-![Unbalanced data](Screenshots/original_data_distribution.png)

I used the HuggingFace model to paraphrase patterns by pegasus model, model name is: "tuner007/pegasus_paraphrase", and ran it locally with Visual Studio code editor, I used CUDA as I have a GPU for faster processing, so this step has a separate virtual environment from the main model (each environment has its requirement file containing their packages).
-![Balanced Data](Screenshots/balanced_data_distribution.png)

- **Install Data Augmentation Dependencies:**  
  The `data_augmentation` folder contains its own `requirements.txt` file. To install the necessary packages, run:

  ```bash
  pip install -r data_augmentation/requirements.txt
  ```

## Acknowledgements

- A huge thanks to [AMIT](https://www.linkedin.com/company/amit-learning/posts/?feedView=all) for the assistance and guidance during the development of this project.

## Contact & Feedback

If you have any comments, issues, or questions, please feel free to reach out through any of the following channels:

- **GitHub:** [here](https://github.com/Selim9-9/)
- **Kaggle:** [here](https://www.kaggle.com/selimkhaled50)
- **LinkedIn:** [here](https://www.linkedin.com/in/saleem-khaled-a502b3253/)
- **Email:** [here](saleim023Gmail.com)

---

Happy coding!
Happy Learning!



