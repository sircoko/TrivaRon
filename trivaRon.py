import urllib2
from bs4 import BeautifulSoup as bs
import csv
#pagination
# https://compraenlinea.excelsiorgama.com/BEBIDAS/c/003?q=%3Aprice-asc&page=0
# https://compraenlinea.excelsiorgama.com/BEBIDAS/c/003?sort=name-asc&q=%3Arelevance#

articulos = []
page_count = 0

while (page_count != -1):
    print '######    pagina: ' + str(page_count) + '    ######'
    excel = "https://compraenlinea.excelsiorgama.com/BEBIDAS/c/003?q=%3Aprice-asc&page="+str(page_count)
    page = urllib2.urlopen(excel)
    soup = bs(page)
    
    count = 0
    count_enabled = 0
    page_items = soup.find_all('li', class_='product__list--item')
    for i in page_items:
        count = count + 1
        if (i.button.get("class") == ['btn', 'btn-primary', 'btn-block', 'glyphicon', 'glyphicon-shopping-cart', 'js-enable-btn']):
            count_enabled += 1
    print 'Se encontraron: '+str(count_enabled)+' articulos.\n'
        
    if(count>0):
        for item in page_items:
            if (item.button.get("class") == ['btn', 'btn-primary', 'btn-block', 'glyphicon', 'glyphicon-shopping-cart', 'js-enable-btn']):
                name = item.find('a', class_='product__list--name').string
                price = (item.find('div', class_='from-price-value')).string
                articulos.append([[name],[price]])
        page_count += 1
    else:
        page_count = 0-1
        
print articulos

ofile  = open('Reporte TrivaRon.csv', "wb")
#writer = csv.writer(ofile, delimiter='', quotechar='"', quoting=csv.QUOTE_ALL)
 
writer = csv.writer(ofile)
    

for articulo in articulos:
    writer.writerow( (articulo[0], articulo[1]) )
 
ofile.close()