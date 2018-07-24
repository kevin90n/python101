import sys
import datetime

user_list = []
movie_list= []
time_list= []
date_file=[]
ratings_list=[]
fiveratings_list= []
uniq_user_id = {}
uniq_movie_id = {}



def read_lines_for(file_obj):
  lines = file_obj.readlines()
  i = 0
  for line in lines:
#    print(type(line))
    print (line)
    i += 1
    if i ==10:
      break


def process_data(file_obj):
  lines = file_obj.readlines()
  i = 0
  for line in lines:
     string_list = line.split("\t")
     string_list[3]=string_list[3].replace('\n', '')
     user_list.append(string_list[0])
     movie_list.append(string_list[1])
     ratings_list.append( string_list [1] + "   " + string_list[2])
     i += 1
     if i ==10:
        break
 # uniq_id_analysis(user_list)
  ratings_analysis(ratings_list)

#  print(user_list)   
#  print(movie_list)

def convert_time_stamp(date_file):
  lines = date_file.readlines()
  i = 0
  for line in lines:
    string_list = line.split("\t")
    string_list[3]=string_list[3].replace('\n', '')
    time_list.append(datetime.datetime.fromtimestamp(int(string_list[3])).strftime('%Y-%m-%d %H:%M:%S'))
    i += 1
    if i ==10:
      break

  print(time_list)

def uniq_id_analysis(uniqu):
  for k in range(0, len(uniqu)):
     print(uniqu[k])
     for j in range(1, len(uniqu)):
       print(uniqu[j])
  #     if uniqu[k] == uniqu[j]:
  #       del uniqu[j]

        
  

def ratings_analysis(date_file):
  fiveratings_list=list(date_file)
  #lines = date_file.readlines()
  #for line in lines:
  ##  string_list = line.split("   ")
   # if string_list[2] == "5":
   #   fiveratings_list.append(string_list[1])
   #   print("okay", fiveratings_list)  
#  print(fiveratings_list)
  print(list(date_file))
  return

def top_ratings_movies ():
  return  

def main(path):
  fo = open(path, 'r')
#  read_lines_for(fo)
  process_data(fo)
#  convert_time_stamp(fo)
  ratings_analysis(fo)
  fo.close()

if __name__ == "__main__":
  arg_len = len(sys.argv [1:])
  print(arg_len)
  if (arg_len <1):
    print("ERROR\t:exitting...... arguments passed")
    sys.exit()
  print("calling main function")
  main(sys.argv[1])
