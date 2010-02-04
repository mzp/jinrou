# -*- coding: utf-8 -*-
# main.views

"""
import logging

from google.appengine.api import users
from google.appengine.api import memcache
from werkzeug import (
  unescape, redirect, Response,
)
from werkzeug.exceptions import (
  NotFound, MethodNotAllowed, BadRequest
)

from kay.utils import (
  render_to_response, reverse,
  get_by_key_name_or_404, get_by_id_or_404,
  to_utc, to_local_timezone, url_for, raise_on_dev
)
from kay.i18n import gettext as _
from kay.auth.decorators import login_required

"""

from kay.utils import render_to_response
from werkzeug import (
  unescape, redirect, Response,
)
import forms
import models

def index(request):
  villages = models.Village.gql("WHERE playing = false ORDER BY created DESC").fetch(100)
  form = forms.VillageForm()
  if request.method == "POST":
    if form.validate(request.form):
      village = models.Village(name=form['name'],
                               description = form['description'],
                               capacity    = form['capacity'],
                               daytime     = form['daytime'],
                               nighttime   = form['nighttime'])
      village.put()
      return redirect("/")
  return render_to_response('main/index.html', { 'form': form.as_widget(),
                                                 'villages': villages})
