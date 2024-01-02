from behave import given,when,then
from read_restCall import fetch_book_data

@given('I have provided book id {bookId}')
def step_impl(context,bookId):
    context.bookId = bookId

@when('I fetch data')
def step_impl(context):
    context.result = fetch_book_data(context.bookId)

@then('the status should be {status01} which indicate the book is avaliable')
def step_impl(context,status01):
    assert int(context.result.status_code) == int(status01)
    

