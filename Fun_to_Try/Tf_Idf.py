from collections import Counter
import math
import numpy as np

class TFIDF:
    
    ls_docs = []
    
    def __init__(self,docs):
        self.ls_docs = docs
    
    def cal_tf(self,inp_word,doc):
        words = doc.split()
        dic_doc_wordCnt= Counter(words)
        return dic_doc_wordCnt[inp_word]/len(words) if inp_word in words else 0
    
    def cal_idf(self,inp_word):
        doc_wrd_cnt = 0 
        final_vec = []
        

        doc_wrd_cnt = sum([1 for doc in self.ls_docs if inp_word in doc  ]) # Check if present in each doc
        idf = math.log(len(self.ls_docs)/doc_wrd_cnt) if doc_wrd_cnt>0 else 0 #Check divide zero error
        
        for doc in self.ls_docs:
          
            tf= self.cal_tf(inp_word,doc)
            tfidf = tf*idf
            final_vec.append(tfidf)
        
        return np.array(final_vec)

webpages = [
    "machine learning is amazing",
    "deep learning and machine learning are popular",
    "gradient descent is used in machine learning",
    "machine learning models use gradient descent"
]
keyword = "amazing"

obj = TFIDF(webpages)
print (obj.cal_idf(keyword))