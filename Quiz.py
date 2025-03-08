def index(req):
  postData = req.form
  json = str(postData['param'].value)
  return json

# if __name__ == "__main__":
#   return main()