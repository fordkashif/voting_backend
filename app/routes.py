from flask import Blueprint, jsonify
from .selenium_automation import automate_voting

main = Blueprint('main', __name__)

@main.route('/vote', methods=['POST'])
def vote():
    # Trigger the Selenium script to automate the voting
    automate_voting()
    return jsonify({'message': 'Vote automation complete'})