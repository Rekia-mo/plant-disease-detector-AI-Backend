# from enum import IntEnum
# from typing import List, Optional

# from pydantic import BaseModel, Field





# class Priority(IntEnum):
#     high = 1
#     medium = 2
#     low = 3

# class TodoBase(BaseModel):
#     name: str = Field(..., min_length=1, max_length=100, description="The name of the todo item")
#     description: str = Field(..., description="The description of the todo item")
#     priority : Priority = Field(default=Priority.low, description="The priority of the todo item") # type: ignore

# class Todo(TodoBase): 
#     id: int = Field(..., description="The unique identifier of the todo item")

# class TodoCreate(TodoBase):
#     pass

# class TodoUpdate(BaseModel):
#     name: Optional[str] = Field(None, min_length=1, max_length=100, description="The name of the todo item")
#     description: Optional[str] = Field(None, description="The description of the todo item")
#     priority: Optional[Priority] = Field(None, description="The priority of the todo item") # type: ignore

# all_todos =[
#     Todo(id=1, name="sports", description="play football", priority=Priority.high),
#     Todo(id=2, name="work", description="do work", priority=Priority.medium),
#     Todo(id=3, name="study", description="do study", priority=Priority.low)
# ]








# @api.get ('/todos/{id}', response_model=Todo)
# def get_todo(id: int):
#     for todo in all_todos:
#         if(todo.id ==id):
#             return todo
#     raise HTTPException(status_code=404, detail="Todo not found")

# @api.get('/todos', response_model=List[Todo])
# def get_all_todos(first_n:int = None):
#     if first_n:
#         return all_todos[:first_n]
#     return all_todos

# @api.post('/todos', response_model=Todo)
# def create_todo(todo: TodoCreate):
#     new_id = max(todo.id for todo in all_todos) + 1

#     new_todo = {
#         "id": new_id,
#         "name": todo.name,
#         "description": todo.description,
#         "priority": todo.priority
#     }

#     all_todos.append(new_todo)
#     return new_todo

# @api.put('/todos/{id}', response_model=Todo)
# def update_todo(id:int , updated_todo: TodoUpdate):
#     for todo in all_todos:
#         if(todo.id == id):
#             todo.name = updated_todo.name
#             todo.description = updated_todo.description
#             return todo
#     raise HTTPException(status_code=404, detail="Todo not found")

# @api.delete('/todos/{id}', response_model=Todo)
# def delete_todo(id: int):
    # for index, todo in enumerate(all_todos):
    #     if(todo.id == id):
    #         deleted_todo = all_todos.pop(index)
    #         return deleted_todo
    # raise HTTPException(status_code=404, detail="Todo not found")