import sys
import datetime
from collections import Counter

five_count=0
four_count=0
three_count=0
two_count=0
one_count=0
user_list = []
uid = []
movie_list= []
time_list= []
date_file=[]
ratings_list=[]
fiveratings_list= []
uniq_user_id = {}
uniq_movie_id = {}
starlist=['5','4','3','2','1']
unique_user_list=[]
unique_movie_list=[]
top_ratings_list={}
def process_data(file_obj):
  lines = file_obj.readlines()
  i = 0
  for line in lines:
     string_list = line.split("\t")
     string_list[3]=string_list[3].replace('\n', '')
     build_list(string_list)
     uniq_id_analysis()
     convert_time_stamp(string_list)
     i +=1
     if i == 10:
        break
  ratings_analysis(ratings_list,five_count,four_count,three_count,two_count,one_count)
  top_ratings_movies()
  print("User list", user_list)
  print("MOvie list", movie_list)
  print("Unique user list", unique_user_list)
  print("Unique movie list", unique_movie_list)
  print("Timestamp", time_list)
def build_list(list):
    '''this function builds list for user, movies, ratings'''
    user_list.append(list[0])
    movie_list.append(list[1])
    ratings_list.append(list[2])


def convert_time_stamp(date_file):
    time_list.append(datetime.datetime.fromtimestamp(int(date_file[3])).strftime('%Y-%m-%d %H:%M:%S'))

def uniq_id_analysis():
  for what in user_list:
     if what not in unique_user_list:
      unique_user_list.append(what)
  
  for what in movie_list:
    if what not in unique_movie_list:
      unique_movie_list.append(what)
      
def ratings_analysis(ratings_list,five_count,four_count,three_count,two_count,one_count):
   length=len(ratings_list)-1
   for i in range(0, length):
    if(ratings_list[i]=='5'):
      five_count=five_count+1
    elif ratings_list[i]=='4':
     four_count=four_count+1
    elif(ratings_list[i]=='3'):
     three_count=three_count+1
    elif(ratings_list[i]=='2'):
     two_count=two_count+1
    elif(ratings_list[i]=='1'):
     one_count=one_count+1
   print("Number of 5 stars ratings are:", five_count)
   print("Number of 4 stars ratings are:", four_count)
   print("Number of 3 stars ratings are:", three_count)
   print("Number of 2 stars ratings are:", two_count)
   print("Number of 1 stars ratings are:", one_count)


def top_ratings_movies ():
  length=len(ratings_list)-1
  count=0
  count_low=0
  for i in range(0, length):
    if(ratings_list[i] >= '4'):
      if(movie_list[i] not in top_ratings_list):
        print(movie_list[i])
        count+=1
        top_ratings_list[movie_list[i]]=["Count of 5 and 4 stars for {} is {}".format(movie_list[i],count)]
        print(top_ratings_list)

 

def main(path):
  fo = open(path, 'r')
  process_data(fo)
  fo.close()

if __name__ == "__main__":
  arg_len = len(sys.argv [1:])
  print(arg_len)
  if (arg_len <1):
    print("ERROR\t:exitting...... arguments passed")
    sys.exit()
  print("calling main function")
  main(sys.argv[1])
