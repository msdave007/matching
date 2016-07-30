import json;

#Developer: Maharshi Dave
#Phone: 647-234-2731

if __name__ == "__main__":
    
    listingsForProduct = []
    products= open("products.txt",'r+')
    listings= open("listings.txt",'r+')
    listedItems = listings.readlines()
    
    for product in products:
        ''''for every product, we want to see how many listings there are'''
        curProd = json.loads(product)
        curModel = curProd["model"]
        curManufac = curProd["manufacturer"]

        '''we have a model and manufacturer'''
        for listing in listedItems:
            
            curList = json.loads(listing)
            curListManu = curList["manufacturer"]
            curListTitle = curList["title"]
            
            if curManufac == curListManu and (curModel in curListTitle):
                '''we have product from same manufacturer and
                they are of same model'''
                listingsForProduct.append(curList)
                #data = {"product_name":curProd["product_name"], "listings":listingsForProduct}
        xprime = str(listingsForProduct) 
        listingsstr = [x.encode('utf-8') for x in xprime] #encode data for string representation 
        with open("result.txt", "a") as result:
            result.write("{\"product_name\":\""+curProd["product_name"]+"\",\"listings\":"+json.dumps(listingsForProduct)+"}")
            result.write("\n") #newline separator 
        listingsForProduct = [] 
    products.close()
    listings.close()