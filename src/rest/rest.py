#!flask/bin/python
from flask import Flask, jsonify
from ..models.Recipe import Recipe
from ..shared.Authentication import Auth

@app.route('/api/v1/recipes', methods=['GET'])
@Auth.auth_required
def get_recipe():

    query_parameters = request.args

    id = query_parameters.get('id')
    name = query_parameters.get('name')

    if id:
        recipe = Recipe.get_one_recipe_by_id(id)
    elif name:
        recipe = Recipe.get_one_recipe_by_name(name)
    else:
        return custom_response({'error': 'user not found'}, 404)

    return custom_response(recipe, 200)

@app.route('/api/v1/recipes', methods=['POST'])
@Auth.auth_required
def create_recipe():

    req_data = request.get_json()

    recipe = Recipe(req_data)
    recipe.save()

    return custom_response(recipe, 200)

@app.route('/api/v1/recipes', methods=['PUT'])
@Auth.auth_required
def update_recipe():

    req_data = request.get_json()

    recipe = Recipe(req_data)
    recipe.update(req_data)

    return custom_response(recipe, 201)


@app.route('/api/v1/recipes', methods=['DELETE'])
@Auth.auth_required
def delete_recipe():

    query_parameters = request.args

    id = query_parameters.get('id')

    recipe = Recipe.get_one_recipe_by_id(id)
    recipe.delete()

    return custom_response(recipe, 201)


def custom_response(res, status_code):

    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )




