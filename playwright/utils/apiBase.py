import time

from playwright.sync_api import Playwright

#order_payload = {"_id":"6a0ca35817ee3e78ba89135f","product":{"_id":"6960eac0c941646b7a8b3e68","productName":"ZARA COAT 3","productCategory":"electronics","productSubCategory":"mobiles","productPrice":11500,"productDescription":"Apple phone","productImage":"https://rahulshettyacademy.com/api/ecom/uploads/productImage_1767959232316.jpeg","productRating":"0","productTotalOrders":"0","productStatus":"true","productFor":"women","productAddedBy":"admin","__v":0}}

order_payload = {"orders":[{"country": "Congo, the Democratic Republic of the","productOrderedId":"6960eae1c941646b7a8b3ed3"}]}
#token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OWZiNmRkN2ViMDMzM2I2ZGIzOGQyMjQiLCJ1c2VyRW1haWwiOiJoZjE3ODhAZ21haWwuY29tIiwidXNlck1vYmlsZSI6NDQ5NzY5NzcyNSwidXNlclJvbGUiOiJjdXN0b21lciIsImlhdCI6MTc3ODA4NTM0NywiZXhwIjoxODA5NjQyOTQ3fQ.OCb4FbKlOcPqlzz5DwNOquELKN-hI8_cZkPsWXrAkkw"
class APIUtils:

    def getToken(self, playwright:Playwright, user_credentials):
        email = user_credentials["userEmail"]
        password = user_credentials["userPassword"]
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_request_context.post(url="/api/ecom/auth/login",
                                 data={"userEmail": email, "userPassword": password})
        #time.sleep(5)
        #print(f"Status: {response.status}, Body: {response.text()}")
        assert response.ok

        print(response.json())
        return response.json()["token"]

    def createOrder(self,playwright:Playwright, user_credentials):
        token = self.getToken(playwright, user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_request_context.post(url="/api/ecom/order/create-order",
                                 data=order_payload,
                                 headers={"Authorization": token,
                                          "Content-Type": "application/json"})
        responseBody = response.json()
        print(responseBody)
        orderid = responseBody["orders"][0]
        return orderid
