from flask import request, jsonify, json
from flask.views import MethodView
from flask_smorest import abort
from uuid import uuid4

from . import bp
from schemas import PostSchema
from db import users, posts
from schemas import CarSchema
from models.post_model import UserModel

# @bp.route('/post')
# class PostList(MethodView):
    
#     @bp.arguments(PostSchema)
#     def post(self, post_data):
#         if post_data['author'] not in users:
#             return {"message": "user does not exist"}, 400
#         post_id = uuid4().hex
#         posts[post_id] = post_data

#         return {
#             'message': "Post created",
#             'post-id': post_id
#             }, 201

#     @bp.response(200, PostSchema(many=True))
#     def get(self):
#         return list(posts.values())

# @bp.route('/post/<post_id>')
# class Post(MethodView):

#     @bp.response(200, PostSchema)
#     def get(self, post_id):
#         try: 
#             return posts[post_id]
#         except KeyError:
#             return {'message':"invalid post"}, 400

#     @bp.arguments(PostSchema)
#     def put(self, post_data, post_id):
#         if post_id in posts:
#             posts[post_id] = {k:v for k,v in post_data.items() if k != 'id'} 

#             return {'message': f'post: {post_id} updated'}, 201
        
#         return {'message': "invalid post"}, 400

#     def delete(self, post_id):

#         if post_id not in posts:
#             return { 'message' : "Invalid Post"}, 400
        
#         posts.pop(post_id)
#         return {'message': f'Post: {post_id} deleted'}

@bp.route('/car')
class CarList(MethodView):
    
    @bp.response(200, CarSchema(many=True))
    def get(self):
        return list(cars.values())
    
    @bp.arguments(CarSchema)
    @bp.response(201, CarSchema)
    def post(self, data):
        try:
            car = UserModel()
            car.from_dict(data)
            car.save_car()
            return {
                'success' : f'{car.make} {car.model} added'

            },201
        except:
            return {
                'error' : 'forgot to add make and model'
            },400
 

@bp.route('/car/<int:id>')
class Car(MethodView):
    
    @bp.response(200, CarSchema)
    def get(self, id):
        car = UserModel.query.get(id)
        if car:
            return car
        else:
            abort(400, message = 'invalid car id')

    @bp.arguments(CarSchema)
    def put(self, data, id):
        car = UserModel.query.get(id)
        if car:
            car.from_dict(data)
            car.save_car()
            return { 'message': 'user updated'}, 200
        else:
            abort(400, message='invalid car id')    

    def delete(self, id):
        car = UserModel.query.get(id)
        if car:
            car.del_car()
            return { 'message': 'Car is gone now'}, 200
        else:
            abort(400, message='invalid car id')    