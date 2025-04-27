# 1) https://www.codewars.com/kata/555086d53eac039a2a000083/train/python
# 2) https://www.codewars.com/kata/53dc54212259ed3d4f00071c/train/python
# 3) https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd/train/python
# 4) https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/train/python
# 5) https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7/train/python


# 2) გააკეთეთ manual_replace ფუნქცია

def Manual_replace(text, old, new):
  result = ""
  i = 0
  while i < len(text):
    if text[i:i + len(old)] == old:
      result += new
      i += len(old)
    else:
      result += text[i]
      i += 1
  return result

# 3) გააკეთეთ manual_len ფუნქცია

def manual_len(string):
  count = 0
  for char in string:
    count += 1