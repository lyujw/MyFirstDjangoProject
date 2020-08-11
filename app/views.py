from django.shortcuts import render, redirect
import pymysql


def restaurant_info(request):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='djangotemplate', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("SELECT id,res_name,address,res_type from restaurant")
    restaurant_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request, 'restaurant_info.html', {'restaurant_list': restaurant_list})


def add_restaurant(request):
    if request.method == "GET":
        return render(request, 'add_restaurant.html')
    else:
        print(request.POST)
        v1 = request.POST.get('name')
        v2 = request.POST.get('address')
        v3 = request.POST.get('type')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='djangotemplate',
                               charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("INSERT INTO restaurant(res_name,address,res_type) values(%s,%s,%s)", [v1, v2, v3, ])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/restaurant_info/')
