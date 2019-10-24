from array_stack import ArrayStack

def is_matched_html(raw):
  """Return True if all HTML tags are properly match; False otherwise."""
  S = ArrayStack()
  j = raw.find('<')               # find first '<' character (if any)
  while j != -1:
    k = raw.find('>', j+1)        # find next '>' character
    if k == -1:
      return False                # invalid tag
    tag = raw[j+1:k]              # strip away < >
    if not tag.startswith('/'):   # this is opening tag
      S.push(tag)                 
    else:                         # this is closing tag
      if S.is_empty():
        return False              # nothing to match with
      if tag[1:] != S.pop():   
        return False              # mismatched delimiter
    j = raw.find('<', k+1)        # find next '<' character (if any)
  return S.is_empty()             # were all opening tags matched?


my_html1="<html><head><title>Hello</title></head></html>"
my_html2="<html><title>Hello</title></head><body><p>This appears in the <i>browser</i>.</p></body></html>"

if is_matched_html(my_html1):
  print("HTML Balanced")
else:
  print("Not balanced")

if is_matched_html(my_html2):
  print("HTML Balanced")
else:
  print("Not balanced")