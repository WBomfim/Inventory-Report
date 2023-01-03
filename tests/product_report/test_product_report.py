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


def test_relatorio_produto():
    product = mock_product()
    new_product = Product(
        product['id'],
        product['nome_do_produto'],
        product['nome_da_empresa'],
        product['data_de_fabricacao'],
        product['data_de_validade'],
        product['numero_de_serie'],
        product['instrucoes_de_armazenamento'],
    )

    assert new_product.__repr__() == (
        f"O produto {product['nome_do_produto']}"
        f" fabricado em {product['data_de_fabricacao']}"
        f" por {product['nome_da_empresa']} com validade"
        f" até {product['data_de_validade']}"
        f" precisa ser armazenado {product['instrucoes_de_armazenamento']}."
    )
