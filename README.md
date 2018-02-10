# Generic Risk Model and UI
This app is build on Python, Django, Vue, ES2015,
### ORM Design
*core.models.py RiskType*
```python
class RiskType(models.Model):
  DEFAULT_ATTR_META = [{'field_name': 'first_name', 'display_title': 'First Name', 'field_type': 'text'},
                         {'field_name': 'last_name', 'display_title': 'Last Name', 'field_type': 'text'},
                         {'field_name': 'serial_no', 'display_title': 'Serial NO','field_type': 'text'}]
  risk_type = models.CharField(max_length=50)
  risk_code = models.CharField(max_length=5, unique=True)
  risk_attr_meta = models.TextField(default=DEFAULT_ATTR_META)
```
In this design I have made the risk attributes aka fields to be saved as a JSON serialized object in __risk_attr_meta__ column, Here I have used it as 
a TextField, In more advnced SQL databases like POSTGRES we have JSONFIELD support at db level and thus it can be helpful with this design.

I have overridden the default save of django model to verify the structure and field attributes so as only valid data enters the db store
as seen below:
```python
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
```

This model is just to save the meta data of the Risk Types. In the same fashion we can have another model to save the user data, 
validating against the meta data of the Risk type.

##Running application
```shell
pip install -r requirements.txt
python manage.py runserver

//Another tab
cd frontend/app
npm install
npm run dev 
```

Live Preview available at
https://aqueous-refuge-73233.herokuapp.com/home/
