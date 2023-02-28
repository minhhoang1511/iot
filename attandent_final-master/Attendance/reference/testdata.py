
import pymysql

# kết nối tới cơ sở dữ liệu
conn = pymysql.connect(host='localhost', user='root', password='', db='testty', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

# thực hiện câu truy vấn SQL
with conn.cursor() as cursor:
    # ví dụ truy vấn lấy tất cả các bảng trong cơ sở dữ liệu
    sql = "select * from ha;"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

# đóng kết nối
conn.close()