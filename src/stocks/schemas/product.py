from graphene import ObjectType, String, Int, Float

class Product(ObjectType):
    id = Int()
    sku = String()
    name = String()
    price = Float()
    quantity = Int()