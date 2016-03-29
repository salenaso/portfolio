#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import logging
import jinja2

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class IndexHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    	self.response.write(template.render({'title': 'HOME'}))

class FamilyHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/portfolio.html')
    	self.response.write(template.render({'title': 'PORTFOLIO'}))


class FoodHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/resume.html')
    	self.response.write(template.render({'title': 'RESUME'}))

class TravelsHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/travels.html')
        self.response.write(template.render({'title': 'TRAVELS'}))   

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
        self.response.write(template.render({'title': 'CONTACT'}))
    def post(self):
        stguess=self.request.get('name')
        logging.info(stguess)
        name=str(stguess)

        yo=self.request.get('pw')
        logging.info(yo)
        pw=str(yo)

        hey=self.request.get('message')
        logging.info(hey)
        message=str(hey)
        
        if name !="Colleen" and pw!="pass":
            msg='bad credentials try again'

            template = JINJA_ENVIRONMENT.get_template('templates/login.html')
            outstr=template.render({'hint':msg})
            self.response.write(outstr)
        else:
            template = JINJA_ENVIRONMENT.get_template('templates/success.html')
            self.response.write(template.render())

       



app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/index.html', IndexHandler),
    ('/portfolio.html', FamilyHandler),
    ('/resume.html', FoodHandler),
    ('/travels.html', TravelsHandler),
    ('/contact.html', LoginHandler)
], debug=True)
