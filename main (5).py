def linearSearchProduct(ProductList,targetProduct):
  indices=[]
  for index,product in enumerate(ProductList):
    if product == targetProduct:
      indices.append(index)
  return  indices
product=["shoes","boot","loafer","shoes","sandal","shoes"]
target="shoes"
target2='apple'
result=linearSearchProduct(product,target)
print(result)


      
      
