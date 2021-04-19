# coding : utf-8
import sys
sys.path.append('C:\\Users\\Utilisateur\\Documents\\ExerciceOC\\Pur_Beurre')
import Controllers.productController as p

class ProductView:

	def __init__(self):

		self.prodView = p.ProductController()


	def show_products(self,productController):

		print("\n*****************************************")
		print("****          PRODUITS               ****")
		print("*****************************************\n")
		for product in productController:
			print("****      ",product.id, product.product_name,"        ****")

	def describe_product(self, productController):

		# choice = int
		# for product in productController:

		# 	if product.id in productController:

		print("\n*****************************************")
		print("****     Description du produit      ****")
		print("*****************************************\n")
		print("\nNOM : ", productController.product_name)
		print("\nCODE : ", productController.code)
		print("\nNUTRISCORE : ", productController.nutrition_grade)
		print("\nSTORES : ", productController.stores)