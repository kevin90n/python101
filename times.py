fo=open("/home/kevin/python/python101/times_of_india_mod.txt", 'w+')
with open("/home/kevin/python/python101/times_of_india.txt", 'r') as json_file:
  formatted_lines=json_file.readlines()
  for lines in formatted_lines:
    pattern_1='-{'
    pattern_2='-\"source\"'
    if pattern_1 in lines:
     fo.write(lines.replace(pattern_1,pattern_1[1]))
    elif pattern_2 in lines:
     fo.write(lines.replace(pattern_2,pattern_2[1:9]))
    else:
     fo.write(lines)
fo.close()

