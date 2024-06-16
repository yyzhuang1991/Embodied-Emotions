# Embodied-Emotions

This repository contains the dataset released in the paper: [My Heart Skipped a Beat! Recognizing Expressions of Embodied Emotion in Natural Language](https://aclanthology.org/2024.naacl-long.193.pdf).

Dataset: The training, development and test data can be found in the *data* directory. Each data file is a json file, where instances are stored in a list. An instance contains a target body part to classify, and it is represented by a dictionary with the following keys and values: 
   
   * `label`: the gold label produced by human annotators. It is either Embodied Emotion or Neutral.
   * `tokens`: a list of tokens of the sentence that contains the target body part mention.  
   * `lemmatized_tokens`: a list of lemmatized tokens of the sentence that contains the target body part mention. 
   * `body_part_token_idx`: the index of the target body part mention in *tokens*. The index starts from 0.  
   * `preceding_context_tokens`: tokens of the preceding sentences, which are stored in a nested list. 
   * `preceding_context_lemmatized_tokens`: lemmatized tokens of the preceding sentences. 


## Contact 
If you have any questions regarding our paper or codes, please contact the author via the email: yuan.zhuang@utah.edu 


## Citation

Please cite our work if you use it in your research. 
    
    @inproceedings{zhuang-etal-2024-heart,
    title = "My Heart Skipped a Beat! Recognizing Expressions of Embodied Emotion in Natural Language",
    author = "Zhuang, Yuan  and Jiang, Tianyu  and Riloff, Ellen",
    editor = "Duh, Kevin  and Gomez, Helena  and Bethard, Steven",
    booktitle = "Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)",
    month = jun,
    year = "2024",
    address = "Mexico City, Mexico",
    publisher = "Association for Computational Linguistics",
    }


 
   
