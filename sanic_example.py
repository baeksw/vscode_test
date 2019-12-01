from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import json, text 

app = Sanic()



class SimpleView(HTTPMethodView):
  def get(self, request):
    return text('i an get method')
  def post(self, request):
    return text('i an post method')


@app.route("/")
async def test(request):
  return json({"hello": "world"})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)
  
  
  





























