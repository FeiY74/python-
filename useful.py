# delete one character from a string
def missing_char(str, n):
  if ( n >= 0 and n <= len(str)):
    return str[:n] + str[n+1:]
