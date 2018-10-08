models.py:
    - override clean methods to clean inputs. look up model.clean in django docs!

    Refactoring:
    - Remove TYpe and Status classes and use a more django-like method to populate
    identification_type field of Customer
