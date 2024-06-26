from behave import *


@given('I am on the Home Page')
def step_impl(context):
    context.home_page.navigate_to_home_page()


@when('I type "{text}" in the search input')
def step_impl(context, text):
    context.home_page.type_text_in_search_input(text)


@when('I click the search button')
def step_impl(context):
    context.home_page.click_search_button()


@then('Search results are displayed')
def step_impl(context):
    context.search_results_page.are_all_products_displayed()


@then('All the search results contain the word "{text}"')
def step_impl(context, text):
    context.search_results_page.are_all_titles_containing_text(text)
