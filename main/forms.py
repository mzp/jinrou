# -*- coding: utf-8 -*-
# main.views
from kay.i18n import lazy_gettext as _
from kay.utils import forms

class VillageForm(forms.Form):
  name        = forms.TextField(_("Village name"),required=True)
  description = forms.TextField(_("Village description"))
  capacity    = forms.IntegerField(_("Max capacity"),required=True)
  daytime     = forms.FloatField(_("day time"),required=True)
  nighttime   = forms.FloatField(_("night time"),required=True)
