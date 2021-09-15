from neuralintents import GenericAssistant
import pandas_datareader as web
import sys

stock_tickers = ['AAPL', 'TSLA']
todos = ['Wash car', 'Code', 'Upload to GitHub']


def greeting():
    print('Hi there!')


def stock_function():
    for ticker in stock_tickers:
        data = web.DataReader(ticker, 'yahoo')
        print(f"The last price of {ticker} was {data['Close'].iloc[-1]}")


def todo_show():
    print('Your ToDo List:')
    for todo in todos:
        print(todo)


def todo_add():
    todo = input('What would you like to add?: ')
    todos.append(todo)


def todo_remove():
    todo = input('What would you like to remove?: ')
    todos.remove(todo)


def bye():
    print('Bye-Bye')
    sys.exit(0)


mappings = {
    'stocks': stock_function,
    'todoshow': todo_show,
    'todoadd': todo_add,
    'todoremove': todo_remove,
    'goodbye': bye,
}

assistant = GenericAssistant('short_intents.json', mappings)

assistant.train_model()
# assistant.save_model()
# assistant.load_model()

while True:
    message = input('Message: ')
    assistant.request(message)
