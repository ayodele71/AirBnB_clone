#!/usr/bin/python3
BaseModel = __import__("base_model").BaseModel

my_model = BaseModel()
print(my_model.to_dict())
print(my_model.id)
print(type(my_model.created_at))
print(my_model.updated_at)
print(my_model)
