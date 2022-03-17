#language: pt

Funcionalidade: fluxo de busca

    @busca_success @busca
    Cenário: realizar busca de valor correto
        Dado que acesso o blog da Agibank
        Quando clico no botão de pesquisa
        E preencho o input de pesquisa com uma entrada válida
        E clico no botão de pesquisar
        Então devo visualizar que os resultados da pesquisa correspondem


    @busca_fail @busca
    Cenário: realizar busca de valor inválido
        Dado que acesso o blog da Agibank
        Quando clico no botão de pesquisa
        E preencho o input de pesquisa com uma entrada inválida
        E clico no botão de pesquisar
        Então devo visualizar uma mensagem de erro