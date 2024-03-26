from flask import request
from flask.views import MethodView
from uuid import uuid4
from flask_smorest import abort

from schemas import SaleReceiptsSchema
from . import bp

from db import cars, sale_receipts
from models.user_model import UserModel

# @bp.route('/user')
# class UserList(MethodView):
    
#     @bp.response(200, UserSchema(many=True))
#     def get(self):
#         return UserModel.query.all()

    
#     @bp.arguments(UserSchema)
#     @bp.response(201, UserSchema)
#     def post(self, data):
#         try:
#             user = UserModel()
#             user.from_dict(data)
#             user.save_user()
#             return {
#                 'message' : f"user {data['username']}"}, 201
#         except:
#             return {
#                 'error' : "username or email already taken, please try a different one!"
#             }, 400
        

# @bp.route('/user/<int:id>')
# class User(MethodView):
    
#     @bp.response(200, UserSchema)
#     def get(self, id):
#         user = UserModel.query.get(id)
#         if user:
#             return user
#         else:
#             abort(400, message="not a valid user")


#     @bp.arguments(UserSchema)
#     def put(self, data, id):
#         user = UserModel.query.get(id)
#         if user:
#             user.from_dict(data)
#             user.save_user()
#             return { "message": "user updated"}, 200
#         else:
#             abort(400, message="not a valid user")          


#     def delete(self, id):
#         user = UserModel.query.get(id)
#         if user:
#             user.del_user()
#             return { "message": "user GONE GONE GONE"}, 200
#         abort(400, message="not a valid user")
        
        # if id in users:
        #     del users[id]
        #     return { 'user gone': f" is no more. . . " }, 202
        # return { 'err' : "can't delete that user they aren't there. . . " } , 400

@bp.route('/sale_receipt')
class SaleReceiptList(MethodView):
    
    @bp.arguments(SaleReceiptsSchema)
    def post(self, sale_receipt_data):
        if sale_receipt_data['sale'] not in cars:
            return {"message": "user does not exist"}, 400
        sale_receipt_id = uuid4().hex
        sale_receipts[sale_receipt_id] = sale_receipt_data

        return {
            'message': "Sale_receipt created",
            'sale_receipt_id': sale_receipt_id
            }, 201

    @bp.response(200, SaleReceiptsSchema(many=True))
    def get(self):
        return list(sale_receipts.values())

@bp.route('/sale_receipt/<sale_receipt_id>')
class SaleReceipt(MethodView):

    @bp.response(200, SaleReceiptsSchema)
    def get(self, sale_receipt_id):
        try: 
            return sale_receipts[sale_receipt_id]
        except KeyError:
            return {'message':"invalid post"}, 400

    @bp.arguments(SaleReceiptsSchema)
    def put(self, sale_receipt_data, sale_receipt_id):
        if sale_receipt_id in sale_receipts:
            sale_receipts[sale_receipt_id] = {k:v for k,v in sale_receipt_data.items() if k != 'id'} 

            return {'message': f'sale_receipt: {sale_receipt_id} updated'}, 201
        
        return {'message': "invalid sale_receipt"}, 400

    def delete(self, sale_receipt_id):

        if sale_receipt_id not in sale_receipts:
            return { 'message' : "Invalid sale_receipt"}, 400
        
        sale_receipts.pop(sale_receipt_id)
        return {'message': f'Sale_receipt: {sale_receipt_id} deleted'}

