from flask import Flask, render_template
from flask_ask import Ask, statement, question, convert_errors

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def start_skill():
    welcome_message = 'bem vindo ao capivara voadora'
    return statement(welcome_message)

@ask.intent('HelloIntent')
def hello(firstname):
    text = render_template('hello', firstname=firstname)
    return statement(text).simple_card('Hello', text)

@ask.intent('WeltonIntent')
def welton():
    text = 'Pelos poderes de Grey Skull eu invoco Welton'
    return statement(text)

@ask.intent('SummonIntent', convert={'person': str})
def summon(person):
    if person in convert_errors:
        return question('Poderia repetir o nome de quem deseja invocar?')
    
    if person is None:
        return question('Quem você deseja invocar?')

    return statement('Pelos poderes de Grey Skull, eu invoco {}'.format(person))


if __name__ == '__main__':
    app.run(debug=True)