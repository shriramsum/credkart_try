from tkinter.tix import Select

from selenium.webdriver.common.by import By


class VerifyOrderAmount_Class:
    Click_AppleMocBook_XPath = (By.XPATH, "//h3[normalize-space()='Apple Macbook Pro']")  # //button[@type='submit']
    Click_AddToCart_XPath = (By.XPATH, "//input[@value='Add to Cart']")  # //button[@type='submit']
    Click_ContinueSHopping_XPath = (By.XPATH, "//a[@class='btn btn-primary btn-lg']")  # //button[@type='submit']
    Click_AppleIPad_XPath = (By.XPATH, "//h3[normalize-space()='Apple iPad Retina']")  # //button[@type='submit']
    Click_HeadPhone_XPath = (By.XPATH, "//h3[normalize-space()='Headphones']")  # //button[@type='submit']

    # DropDown_Quanity_XPATH =

    def __init__(self, driver):
        self.driver = driver

    def Click_AppleMocBook(self):
        self.driver.find_element(*VerifyOrderAmount_Class.Click_AppleMocBook_XPath).click()

    def Click_AppleIPad(self):
        self.driver.find_element(*VerifyOrderAmount_Class.Click_AppleIPad_XPath).click()

    def Click_HeadPhone(self):
        self.driver.find_element(*VerifyOrderAmount_Class.Click_HeadPhone_XPath).click()

    def Click_AddToCart(self):
        self.driver.find_element(*VerifyOrderAmount_Class.Click_AddToCart_XPath).click()

    def Click_ContinueShoppingButton(self):
        self.driver.find_element(*VerifyOrderAmount_Class.Click_ContinueSHopping_XPath).click()

    def Validate_Amount(self):

        l = len(self.driver.find_elements(By.CSS_SELECTOR, "tbody tr"))
        # print(l)

        Price_List = []
        for r in range(1, l - 2):
            Var = self.driver.find_element(By.CSS_SELECTOR,
                                           "tbody tr:nth-child(" + str(r) + ") td:nth-child(4)").text  # $1150
            Product_Price = (Var[1:])  # 1150
            Price_List.append(float(Product_Price))  # 1150.00

        var2 = sum(Price_List)
        Exp_SubTotal = round(var2, 2)
        # print(Exp_SubTotal)
        Exp_Tax = round((Exp_SubTotal * 0.13), 2)
        # print(Exp_Tax)
        Exp_Total = Exp_SubTotal + Exp_Tax
        # print(Exp_Total)
        # Product Price
        Amount_List = []
        for r in range(l - 2, l + 1):
            Var = self.driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(" + str(r) + ") td:nth-child(4)").text
            # print(Var) # $11,150
            var2 = (Var[1:])  # 11,150
            Amounts = var2.replace(',', '')  # 11150
            # Amount_List.append(Amounts)
            Amount_List.append(float(Amounts))  # 11150.00

        Act_SubTotal = Amount_List[0]
        # print(Act_SubTotal)
        Act_Tax = Amount_List[1]
        # print(Act_Tax)
        Act_Total = Amount_List[2]
        # print(Act_Total))
        print("Exp_SubTotal" + str(Exp_SubTotal))
        print("Act_SubTotal" + str(Act_SubTotal))
        print("Exp_Tax" + str(Exp_Tax))
        print("Act_Tax" + str(Act_Tax))
        print("Exp_Total" + str(Exp_Total))
        print("Act_Total" + str(Act_Total))
        if Exp_SubTotal == Act_SubTotal and Exp_Tax == Act_Tax and Exp_Total == Act_Total:
            print("Amount is Matched")
            return "Amount is Matched"
        else:
            print("Amount is Not Matched")
            return "Amount is Not Matched"
