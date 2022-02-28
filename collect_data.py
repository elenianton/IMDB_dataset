import os
import pandas as pd
import glob


#set paths for folders
files_neg1 = os.path.abspath("./IMDB-dataset/test/neg")
files_neg2 = os.path.abspath("./IMDB-dataset/train/neg")
files_pos1 = os.path.abspath("./IMDB-dataset/test/pos")
files_pos2 = os.path.abspath("./IMDB-dataset/train/pos")

#define list for reviews 
list_neg_1 = []
list_neg_2 = []
list_pos_1 = []
list_pos_2 = []

#define paths
path_neg_1 = "./IMDB-dataset/test/neg"
path_neg_2 = "./IMDB-dataset/train/neg"
path_pos_1 = "./IMDB-dataset/test/pos"
path_pos_2 = "./IMDB-dataset/train/pos"


#read txt file and append append them to a list
def read_text_file(file_path, list_name):
    with open(file_path, 'r', encoding='utf-8') as f:
        for file in f:
            list_name.append(file)
    
#listdir folder and define filepath for every ".txt" file                     
def define_path(folder_path, path, list_name):
    for file in os.listdir(folder_path):
        # Check whether file is in text format or not
        if file.endswith(".txt"):
            file_path = f"{path}\{file}"
            # call read text file function
            lists = read_text_file(file_path, list_name)
    
    print("Done!")
  

#create dataframes and define them with "negative" or "positive" label       
#files_neg_1
files_path_neg1 = define_path(files_neg1, path_neg_1, list_neg_1)
df_neg_1= pd.DataFrame(list_neg_1, columns=['review'])
df_neg_1['sentiment'] = 'negative'   

#files_neg_2
files_path_neg2 = define_path(files_neg2, path_neg_2, list_neg_2)
df_neg_2 = pd.DataFrame(list_neg_2, columns=['review'])
df_neg_2['sentiment'] = 'negative'   

#files_pos_1
files_path_pos1 = define_path(files_pos1, path_pos_1, list_pos_1)
df_pos_1 = pd.DataFrame(list_pos_1, columns=['review'])
df_pos_1['sentiment'] = 'positive'   

#files_pos_2
files_path_pos2 = define_path(files_pos2, path_pos_2, list_pos_2)
df_pos_2 = pd.DataFrame(list_pos_2, columns=['review'])
df_pos_2['sentiment'] = 'positive'   


#concatenate dataframes
frames = [df_neg_1, df_neg_2, df_pos_1, df_pos_2]
total_df = pd.concat(frames)
total_df = total_df.sample(frac = 1)

#save dataframes into a csv file
total_df.to_csv("./IMDB_reviews.csv", encoding='utf-8', index=False)
