"""

Gidhelp (Github Description Helper):
==================================

    Documentation updated on: 11/02/2025

    
    Introduction:
    ------------
        Gidhelp is a tool that helps us to write our Github profile description.
        It is based on next word predictor technique.
        It has several versions i.e., Gidhelp_75, Gidhelp_500, etc
        currently there are available only one model Gidhelp_75
        more models will comming soon.

        
    How It Works:
    ------------
        In the working of these models first of all we apply Tokenization on text afterthat converting
        data into a supervised labeled data (input and output fully labeled) and then apply Padding 
        to all the sequences.
        
    
    Currently Available Models:
    -------------------------
        -> Gidhelp_75
        -> Gidhelp_500 (upcomming)

"""



# files addresses
GIDHELP_75_MODEL_PATH = "/workspaces/gidhelp/gidhelp_75.h5"
GIDHELP_75_TOKENIZER_PATH = "/workspaces/gidhelp/gidhelp_75_tokenizer.pkl"



# importing utilities and packages
from tensorflow import keras
from typing import List, Tuple, AnyStr, SupportsInt
from keras.preprocessing.sequence import pad_sequences
from numpy import argmax
from time import sleep 

import pickle 






class Gidhelp_75:


    def __init__(self):
        self.model = keras.models.load_model(GIDHELP_75_MODEL_PATH)         # loading trained model
        self.tokenizer_75 = pickle.load(open(GIDHELP_75_TOKENIZER_PATH, 'rb'))   # fecthing tokenizer
        
        



    def predict(self,
        text: AnyStr,
        is_return: bool = True,
        prediction_words_length: SupportsInt = 5,
        verbose = False
    ) -> Tuple[str, List]:

        """ This function will print a tuple of string [complete prediction] and a list [prediction words] """
        
        # initializing and declaring some useful variables
        predicted_words = []
        predicted_text = ""

        # displaying user provided text
        if verbose == True:
            print(text.capitalize(), end=" ")

        updated_text = text 
        for i in range(prediction_words_length):                # predicting `n` - numbers of words

            # tokenizing
            text_tokenized = self.tokenizer_75.texts_to_sequences([updated_text])[0]

            # applying padding on text
            text_padded = pad_sequences([text_tokenized], maxlen=23, padding='pre')

            # prediction 
            pred = self.model.predict(text_padded, verbose=False)

            # getting most probably word
            word_position: int = argmax(pred)

            # getting suitable word
            for word, index in self.tokenizer_75.word_index.items():
                if index == word_position:
                    updated_text += " " + word                  # updating text for next word prediction
                    predicted_text += word + " "                # updating predicted text 
                    predicted_words.append(word)                # updating predicted words list
                    if verbose:
                        sleep(0.2)
                        print(word, end=" ")
            if verbose:
                print()

        if is_return:
            return (predicted_text, updated_text, predicted_words)





if __name__ == "__main__":

    model = Gidhelp_75()

    return_material = model.predict("myself archit tyagi ")

    print(return_material)




