from config import Hosts
from utils.base_session import BaseSession


class DemoQaWithEnv:
    def __init__(self, env):
        self.demoqa = BaseSession(url=Hosts(env).demoqa)
        self.reqres = BaseSession(url=Hosts(env).reqres)

    def login(self, email, password):
        return self.demoqa.post(
            url="/login",
            params={'Email': email, 'Password': password},
            headers={'content-type': "application/x-www-form-urlencoded; charset=UTF-8"},
            allow_redirects=False
        )

    def add_product_to_wishlist(self):
        self.demoqa.post("addproducttocart/details/14/2", json={"addtocart_14.EnteredQuantity": '1'})

    def add_product_to_cart(self):
        self.demoqa.post("addproducttocart/catalog/31/1/1")

    def add_address_user(self):
        self.demoqa.post("customer/addressadd", json={"Address.Id": "0",
                                                      "Address.FirstName": "Irina",
                                                      "Address.LastName": "Rogova",
                                                      "Address.Email": "neeiraaaa@gmail.com",
                                                      "Address.Company": "Minsk",
                                                      "Address.CountryId": "Minsk",
                                                      "Address.StateProvinceId": "0",
                                                      "Address.City": "Gomel",
                                                      "Address.Address1": "Zaslavskaya, 1",
                                                      "Address.Address2": "Nekrasova, 21",
                                                      "Address.ZipPostalCode": "1231231",
                                                      "Address.PhoneNumber": "89167112233",
                                                      "Address.FaxNumber": "12321123"
                                                      })

    @property
    def session_reqres(self):
        return self.reqres

