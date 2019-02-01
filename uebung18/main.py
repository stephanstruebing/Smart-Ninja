#!/usr/bin/env python
import os
import random

import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    capitals = {"Austria": "Vienna", "Germany": "Berlin", "France": "Paris", "Japan": "Tokio"}

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))




class MainHandler(BaseHandler):
        def get(self):
            country = random.choice(self.capitals.keys())
            return self.render_template("capital.html", params={"country": country})







class AnswerHandler(BaseHandler):
    def post(self):
        answer = self.request.get("answer")
        country = self.request.get("country")

        if answer == self.capitals[country]:
            result = "Yeah, you are right"
        else:
            result = "Sorry, that is not correct"

        return self.render_template("result.html", params={"result": result})







app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/answer', AnswerHandler),
], debug=True)


# run on localhost server
gae_env = False  # False: non-GAE localhost server; True: GAE on either localhost or on Google Cloud
if not gae_env:
    def main():
        from paste import httpserver
        from paste.cascade import Cascade
        from paste.urlparser import StaticURLParser

        assets_dir = os.path.join(os.path.dirname(__file__))
        static_app = StaticURLParser(directory=assets_dir)

        web_app = Cascade([app, static_app])
        httpserver.serve(web_app, host='localhost', port='8080')


    if __name__ == '__main__':
        main()
