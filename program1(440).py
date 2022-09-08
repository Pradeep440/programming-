def two_string(a, b):
  for i in range(min(len(a),len(b))):
    if a[i] == b[i]:
      print(f'{a[i]}')

two_string('sairam', 'sainath')
