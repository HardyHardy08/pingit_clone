views.py:
    - create API for models
models.py:
    - override clean methods to validate inputs. first_name, last_name, identification_number and
    contact_number CANNOT be empty
    *look up model.clean in django docs!
    
    Customer Model:
    -tests show that Customer can still be saved with empty identification_number field as
    django.db.models' blank=False only apply to form level validation. Add method or something
    in model/manager to overload default save to keep that from passing
    Refactoring:
    - Remove IdentificationType class and use a more django-like method to populate
    identification_type field of Customer