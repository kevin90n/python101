fo=open("/home/kevin/python/python101/times_of_india_mod.txt", 'w+')
with open("/home/kevin/python/python101/times_of_india.txt", 'r') as json_file:
  formatted_lines=json_file.readlines()
  for lines in formatted_lines:
    pattern_1='-{'
    pattern_2='-\"source\"'
    if pattern_1 in lines:
      fo.write("{")
    elif pattern_2 in lines:
      fo.write('\"source\"')
    elif pattern_1 not in lines:
      fo.write(lines)
    else:
      fo.write(lines)

