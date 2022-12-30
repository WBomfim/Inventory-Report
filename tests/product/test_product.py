from inventory_report.inventory.product import Product


def mock_product():
    return {
        "id": 1,
        "nome_do_produto": "Produto 1",
        "nome_da_empresa": "Empresa 1",
        "data_de_fabricacao": "01/01/2021",
        "data_de_validade": "01/01/2022",
        "numero_de_serie": "123456789",
        "instrucoes_de_armazenamento": "Armazenar em local seco",
    }


def test_cria_produto():
    product_Fake = mock_product()
    new_product = Product(
        product_Fake['id'],
        product_Fake['nome_do_produto'],
        product_Fake['nome_da_empresa'],
        product_Fake['data_de_fabricacao'],
        product_Fake['data_de_validade'],
        product_Fake['numero_de_serie'],
        product_Fake['instrucoes_de_armazenamento'],
    )

    assert new_product.id == product_Fake['id']
    assert new_product.nome_do_produto == product_Fake['nome_do_produto']
    assert new_product.nome_da_empresa == product_Fake['nome_da_empresa']
    assert new_product.data_de_fabricacao == product_Fake['data_de_fabricacao']
    assert new_product.data_de_validade == product_Fake['data_de_validade']
    assert new_product.numero_de_serie == product_Fake['numero_de_serie']
    assert new_product.instrucoes_de_armazenamento == (
        product_Fake['instrucoes_de_armazenamento']
    )
