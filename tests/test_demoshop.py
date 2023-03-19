import allure
from selene import have


def test_auth(app):
    app.open("")
    with allure.step('Проверка успешной авторизации'):
        app.element(".account").should(have.text("neeiraaa@gmail.com"))


def test_delete_product_from_wishlist(demoshop, app):
    app.open("")
    with allure.step('Добавление товара в список желаемого'):
        demoshop.add_product_to_wishlist()
    with allure.step('Проверка удаления товара из списка желаемого'):
        app.element('.ico-wishlist').click()
        app.element('[name="removefromcart"]').click()
        app.element('[name="updatecart"]').click()
        app.element('.wishlist-content').should(have.text('The wishlist is empty!'))


def test_delete_product_from_cart(demoshop, app):
    app.open("")
    with allure.step('Добавление товара в корзину'):
        demoshop.add_product_to_cart()
    with allure.step('Проверка удаления товара из корзины'):
        app.element('.ico-cart').click()
        app.element('[name="removefromcart"]').click()
        app.element('[name="updatecart"]').click()
        app.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


def test_logout(app):
    app.open("")
    with allure.step('Проверка логаута'):
        app.element('.ico-logout').click()
        app.element('.ico-login').should(have.text('Log in'))