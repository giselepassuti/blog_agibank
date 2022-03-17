from behave import given, when, then
from pages import home_page
from utils import Utils
from pages.home_page import HomePage
from pages.results_page import ResultsPages
from nose.tools import assert_equal


utils = Utils()
home_page = HomePage()
results_page = ResultsPages()


@given(u'que acesso o blog da Agibank')
def step_impl(context):
    utils.navegar(context, 'https://blogdoagi.com.br/')


@when(u'clico no botão de pesquisa')
def step_impl(self):
    home_page.click_btn_search()


@when(u'preencho o input de pesquisa com uma entrada válida')
def step_impl(context):
    home_page.preenche_input_busca('conta')


@when(u'Clico no botão de pesquisar')
def step_impl(context):
    home_page.click_btn_pesquisar()


@then(u'devo visualizar que os resultados da pesquisa correspondem')
def step_imp(context):
    assert_equal(results_page.get_text_title(), 'Resultados da busca por: conta')


@when(u'preencho o input de pesquisa com uma entrada inválida')
def step_impl(context):
    home_page.preenche_input_busca('oi')


@then(u'devo visualizar uma mensagem de erro')
def step_imp(context):
    assert_equal(results_page.get_text_title_fail(), 'Nenhum resultado')
