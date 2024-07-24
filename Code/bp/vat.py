product_name=str(input("ชื่อสินค้า : "))
product_price=float(input("ราคาสินค้า : "))
num = int(input("จำวนสินค้า : "))
total_price = product_price*num
vat = total_price*7/100
novat = total_price-vat

print("****************************************")
print("ชื่อสินค้า : {} จำนวน : {} รายการ".format(product_name,num))
print("----------------------------------------")

if total_price >= 5000:
    discount = total_price*10/100
    net_price = total_price-discount
    print("ภาษี 7% = {:.2f}".format(vat))
    print("ราคาจริง = {:.2f}".format(total_price))
    print("ราคาสินค้า = {:.2f}".format(novat))
    print("ราคาส่วนลด 10% = {:.2f}".format(discount))
    print("----------------------------------------")
    print("ราคารวมทั้งสิ้น = {:.2f}".format(net_price))
elif total_price >= 2000:
    discount = total_price*5/100
    net_price = total_price-discount
    print("ภาษี 7% = {:.2f}".format(vat))
    print("ราคาจริง = {:.2f}".format(total_price))
    print("ราคาสินค้า = {:.2f}".format(novat))
    print("ราคาส่วนลด 5% = {:.2f}".format(discount))
    print("----------------------------------------")
    print("ราคารวมทั้งสิ้น = {:.2f}".format(net_price))
else:
    print("ภาษี 7% = {:.2f}".format(vat))
    print("ราคาจริง = {:.2f}".format(total_price))
    print("ราคาสินค้า = {:.2f}".format(novat))
    print("----------------------------------------")
    print("ราคารวมทั้งสิ้น = {:.2f}".format(total_price))
print("----------------------------------------")
