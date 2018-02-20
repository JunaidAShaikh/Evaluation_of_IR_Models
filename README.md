# Evaluation_of_IR_Models
The goal of this project is to implement various IR models(BM25, Vector Space Model, Divergence From Randomness), evaluate the IR system and improve the search result based on our understanding of the models, the implementation and the evaluation.

1. Index the tweets provided into a Solr instance.
2. Evaluate the search resuls returned for the sample Solr queries provided and calculate Mean Average Precision of the results returned.
3. Initialize Solr with the 3 different IR models by changing the Solr instance's similarity model.
4. Evaluate the MAP returned using the different models and try to improve efficienct of each of the models.
5. We have created a few shell scripts to automate the intialization of Solr instance with different models plus different parameters for each model to fine tune the indexing strategy and obtain the maximum MAP value for the results returned.