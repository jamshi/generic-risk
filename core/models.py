# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import json
# Create your models here.

class RiskType(models.Model):

    DEFAULT_ATTR_META = [{'field_name': 'first_name', 'display_title': 'First Name', 'field_type': 'text'},
                         {'field_name': 'last_name', 'display_title': 'Last Name', 'field_type': 'text'},
                         {'field_name': 'serial_no', 'display_title': 'Serial NO','field_type': 'text'}]

    risk_type = models.CharField(max_length=50)
    risk_code = models.CharField(max_length=5, unique=True)
    risk_attr_meta = models.TextField(default=DEFAULT_ATTR_META)

    @property
    def fields(self):
        return self._get_risk_fields()

    def deliver_formatted(self):
        '''
           for api exposure
        '''
        return {'risk_type': self.risk_type, 'risk_code': self.risk_code, 'attrs': self.fields}


    def _get_risk_fields(self):
        _fields = json.loads(self.risk_attr_meta)
        return _fields

    def save(self, *args, **kwargs):
        '''
        Overriding Django model default save
        '''
        _fields = self._get_risk_fields()
        for index, fld in enumerate(_fields):
            field_missing = set(self.DEFAULT_ATTR_META[0].keys()) - set(fld.keys())
            assert len(field_missing) == 0, ( "%s missing  field attribute(s) %s." %
                (str(index) + ': ' + str(fld), ','.join(list(field_missing)))
            )
            assert 'field_type' in fld.keys() and fld['field_type'] in ['text', 'date', 'enum'], \
                            ( "%s is unsupported field type" % (fld['field_type'] ))
        super(RiskType, self).save(*args, **kwargs)


# class Risk(models.Model):

#     DEFAULT_ATTR_META = [{'field_name': 'first_name', 'display_title': 'First Name', 'field_type': 'text'},
#                          {'field_name': 'last_name', 'display_title': 'Last Name', 'field_type': 'text'},
#                          {'field_name': 'serial_no', 'display_title': 'Serial NO','field_type': 'text'}]

#     risk_type = models.CharField(max_length=50)
#     risk_code = models.CharField(max_length=5, unique=True)
#     risk_attr_meta = models.TextField(default=DEFAULT_ATTR_META)

#     @property
#     def fields(self):
#         return self._get_risk_fields()


#     def _get_risk_fields(self):
#         _fields = json.loads(self.risk_attr_meta)
#         return _fields

#     def save(self, *args, **kwargs):
#         '''
#         Overriding Django model default save
#         '''
#         _fields = self._get_risk_fields()
#         for index, fld in enumerate(_fields):
#             field_missing = set(DEFAULT_ATTR_META[0].keys()) - set(fld.keys())
#             assert len(field_missing) == 0, ( "%s missing  field attribute(s) %s." %
#                 (str(index) + ': '  + str(fld), ','.join(list(field_missing)))
#             )
#             assert 'field_type' in fld.keys() and fld['field_type'] in ['text', 'date', 'enum'], \
#                             ( "%s is unsupported field type" % (fld['field_type'] ))
#         super(RiskType, self).save(*args, **kwargs)