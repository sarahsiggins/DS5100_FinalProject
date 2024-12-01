import pandas as pd
import numpy as np

class Game:
    
    def __init__(self,name,email,fav_genre,num_books=0, book_list=pd.DataFrame({'book_name':[],'book_rating':[]})):
        self.name = str(name)
        self.email = str(email)
        self.fav_genre = str(fav_genre)
        self.num_books = num_books
        self.book_list = book_list
        #self.book_list = pd.DataFrame({'book_name':[],'book_rating':[]})
 
    def add_book(self,book_name,book_rating):
        new_book = pd.DataFrame({
            'book_name': [book_name], 
            'book_rating': [book_rating]})
        if str(book_name) in str(self.book_list.book_name):
            raise ValueError("Book already in List")
        else:
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)