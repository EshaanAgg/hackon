# Amazon HackOn

This is the team `Quadeyes` submission for `Amazon HackOn 2023`.

## Overview of the Proposed Solution

## Demonstrations

We have designed two client-side applications to show how the developed solution is independent of the client. Both use the same backend model, `Holo`, which we have trained for the user `Eshaan` based on his searching, movie streaming, and music history. You can see the sample interaction here.

### App

https://github.com/EshaanAgg/hackon/assets/96648934/5f9bfd93-1908-46df-80e6-7dd43f961c8f

### Website

https://github.com/EshaanAgg/hackon/assets/96648934/3d94e1f3-3561-4785-8750-245a63549c47

### How does the demo work?

We are using a thin wrapper on `OpenAI` over the `Holo` model, as the same can only give textual responses or choices. We use `OpenAI` as the NLP processor, which decides which kind of recommendation should be provided to the user. We call the right API of the `Holo` model using `OpenAI functions`. Detailed documentation of the internal models used in `Holo` is included below.

Both the clients call the uniformly developed central backend API, which first communicates with OpenAI functions to figure out the right action/model to call in response to the message, calls the same and then calls OpenAI again to present the user in natural text form to the user. Thus, we can build a client-agnostic solution that works on multiple categories of data and is human-interactable.

## Technologies Used

## Holo: ML Documentation

### Datasets:

The following datsets have been used to train the model

* [https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/](https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/)
* [https://grouplens.org/datasets/movielens/25m/](https://grouplens.org/datasets/movielens/25m/)

* Other similar datasets can be found here - [https://jmcauley.ucsd.edu/data/amazon/](https://jmcauley.ucsd.edu/data/amazon/)

### 1) Rank Based Product Recommendation

**Approach:**
* `Calculating Average Ratings:` It calculates the average rating for each product. This is a measure of how well-received a product is among users.
* `Total Number of Ratings:` It also calculates the total number of ratings or interactions for each product. This indicates how popular a product is in terms of user engagement.
* `DataFrame Creation:` These calculated values are used to create a structured data format called a DataFrame. This format allows for efficient sorting and analysis of the product data.
* `Sorting by Average:` The DataFrame is sorted based on the average ratings, which helps identify the most highly rated products.
* `Function for Recommendations:` A function is written to retrieve the top 'n' products with a specified minimum number of interactions. This function forms the core of the recommendation engine.

**Alignment with the problem statement and solution proposed:**
* `Lack of Personalization:` E-commerce interactions often lack personalization. The Rank Based Product Recommendation model addresses this issue by suggesting popular products with high ratings. While it's not deeply personalised, it offers a basic form of personalization by recommending items that many other users have liked.
* `Solving the Cold Start Problem:` The "Cold Start Problem" refers to difficulties in recommending products to new users. This model overcomes this challenge by recommending well-rated, popular products with a minimum number of interactions, helping new users get started with product recommendations when they have limited interaction history.
* `Decoupling User Interface and Recommendation Logic:` The proposed solution is to create an AI-powered shopping assistant as an API, which can be integrated into various client interfaces. The Rank Based Product Recommendation model aligns with this approach, allowing the separation of recommendation logic from the user interface. It can be a part of the broader system, providing efficient and uniform product recommendations across different platforms.

### 2) Similarity-Based Collaborative Filtering

**Approach:**
* `User Conversion:` User IDs are converted from objects to integers for ease of handling in the system.
* `Finding Similar Users:` The model calculates the similarity score of the desired user with each other user in the interaction matrix using cosine similarity. The scores are collected in a list and sorted to identify the most similar users. The original user is removed from this list, and the rest are returned as similar users.
* `Recommendation Function:` This function calls the previously mentioned similar user function to find users similar to the desired user. It identifies the products with which the original user has interacted (observed interactions). For each similar user, it finds 'n' products with which the similar user has interacted but not the original user. The specified number of such products is returned as recommendations for the user.

**Alignment with the problem statement and solution proposed:**
* `Personalization:` The model directly aligns with the problem statement's challenge of lacking personalization. By considering the behaviour of similar users, it tailors product recommendations to individual preferences, enhancing personalization.
* `User Data Integration:` It fits well with the proposed solution's emphasis on centralised data integration. By considering user interactions, this model leverages data from the interaction matrix, making it a part of the broader AI-powered assistant system.
* `Real-time Interaction:` The model can contribute to real-time interactions by providing dynamic, personalised recommendations based on user behaviour and similarities, enhancing the user experience as proposed in the solution.

### 3) Model-Based Collaborative Filtering

**Approach:**
* `CSR Matrix Conversion:` The matrix of product ratings is converted into a CSR (Compressed Sparse Row) matrix. This compression optimises memory and computational efficiency by storing only non-zero values.
* `Singular Value Decomposition (SVD):` SVD is performed on the CSR matrix to reduce its dimensionality to 50 latent features. This reduction simplifies the complexity of the rating matrix.
Predicted Ratings Calculation: Predicted ratings for all users are calculated by multiplying the U matrix, the sigma matrix, and the Vt matrix. These predicted ratings are stored in a DataFrame where rows represent users, columns represent products, and values represent predicted ratings.
* `Recommendation Function:` This function uses a user's actual ratings and the predicted ratings from the matrix to create a DataFrame.
It identifies products the user has not rated and sorts them by predicted ratings, recommending the top products.
*`Model Evaluation:` Average ratings are calculated for both actual and predicted ratings. A DataFrame is created with average actual and predicted ratings. The Root Mean Square Error (RMSE) is calculated to evaluate the model's accuracy.

**Alignment with the problem statement and solution proposed:**
* `Efficiency and Scalability:` The use of SVD and CSR matrix conversion aligns with the solution's emphasis on efficiency and resource optimization, enabling the model to handle large datasets efficiently.
* `Decoupled Recommendation Logic:` The model-based approach allows for decoupling the recommendation logic from the user interface, which is consistent with the proposed solution's strategy of separating the client interface from recommendation algorithms.
* `User-Initiated Actions:` While the model primarily provides personalised recommendations, it can also align with the solution's goal of reducing the need for user-initiated actions. By proactively suggesting relevant products, it initiates interactions.
* `Real-time Interaction:` By efficiently calculating recommendations based on user behaviour and preferences, this model supports the real-time interaction aspect of the solution, offering dynamic and relevant product suggestions.
