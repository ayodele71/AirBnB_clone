# Tests
![N|Solid](../images/)
This directory contains all unit tests for this project.

* [BaseModel Tests](./test_models/test_base_model.py):

| Test                       		                               | Status|
| -----------------------------------------                    | ------|
| Model is an instance of `BaseModel`                          | `OK`  |
| Model contains `id` attribute                                | `OK`  |
| Model `id` attribute is a string                             | `OK`  |
| Model instances have unique `id`                             | `OK`  |
| Model contains `created_at` attribute                        | `OK`  |
| Model `created_at` attribute is a datetime object            | `OK`  |
| Model contains `updated_at` attribute                        | `OK`  |
| Model `updated_at` attribute is a datetime object            | `OK`  |
| Model `__str__` method prints the correct output             | `OK`  |
| Model `save()` method changes the updated_at attribute       | `OK`  |
| Model to_dict return object has `__class__` attribute        | `OK`  |
| Model to_dict object `created_at` & `updated_at` are strings | `OK`  |
| Model can be instantiated & reinstantiated with dict kwargs  | `OK`  |
| Model instance attribute `created_at` is in ISO format       | `OK`  |
| Model instance attribute `updated_at` is in ISO format       | `OK`  |
