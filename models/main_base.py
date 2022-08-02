#!/usr/bin/python3
BaseModel = __import__("base_model").BaseModel

my_model = BaseModel()
print(type(my_model))
print(my_model.id)
print(my_model.created_at)
print(my_model.updated_at)
