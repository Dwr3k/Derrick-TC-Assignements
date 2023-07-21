from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.sql.window import Window
from pyspark.sql.functions import sum, col, desc, countDistinct, row_number, when, count

conf = SparkConf()
conf.setMaster("local")
conf.setAppName("PySpark Challenge")
spark = SparkSession.builder.config(conf=conf).getOrCreate()


membersDF = spark.read.schema("customer_id String, join_date date").option("header", True).csv("members.csv")
salesDF = spark.read.schema("customer_id String, order_date date, product_id Int").option("header", True).csv("sales.csv")
menuDF = spark.read.schema("product_id Int, product_name String, price Int").option("header", True).csv("menu.csv")

# membersDF.show()
# salesDF.show()
# menuDF.show()

print("#1 What is the total amount each customer spent at the restaurant?")
salesDF.join(menuDF, menuDF["product_id"] == salesDF["product_id"], "inner").groupBy("customer_id").agg(sum("price").alias("Price Sum")).sort(desc('Price Sum')).show()

print("#2 How many days has each customer visited the restaurant?")
salesDF.groupby("customer_id").agg(countDistinct("order_date").alias("Days Visited")).orderBy(col("Days Visited").desc()).show()

print("#3. What was the first item from the menu purchased by each customer?")
testWindow = Window.partitionBy("customer_id").orderBy("order_date")
salesDF.withColumn("row_number", row_number().over(testWindow)).join(menuDF, menuDF["product_id"] == salesDF["product_id"]).where(col("row_number") == 1).show()

print(" -- 4. What is the most purchased item on the menu and how many times was it purchased by all customers?")
salesDF1 = salesDF.withColumnRenamed("product_id", "spid")
salesDF1.join(menuDF, menuDF["product_id"] == salesDF1["spid"], "inner").groupBy("product_name").agg(count("product_id").alias("amt_ordered")).sort(desc("amt_ordered")).limit(1).show()

print("-- 5. Which item was the most popular for each customer")
salesDF1 = salesDF.withColumnRenamed("product_id", "pid")
salesDF1.groupBy("customer_id").agg(
    count(when(salesDF1["pid"] == 1,1)).alias("Sushi Ordered"),
    count(when(salesDF1["pid"] == 2,1)).alias("Curry Ordered"),
    count(when(salesDF1["pid"] == 3,1)).alias("Ramen Ordered")).sort(("customer_id"))\
    .show()



membersView = membersDF.createTempView("members")
salesView = salesDF.createTempView("sales")
menuView = menuDF.createTempView("menu")

#6 -- Which item was purchased first by the customer after they became a member?
spark.sql("select * from (select members.customer_id, members.join_date, sales.order_date, menu.product_name, "
          "row_number() over (partition by members.customer_id order by sales.order_date asc) as r_count "
          "from members join sales on members.customer_id = sales.customer_id join menu on menu.product_id = sales.product_id"
          " where members.join_date < sales.order_date) as a where r_count = 1").show()


print("-- 7. Which item was purchased just before the customer became a member?")

spark.sql("select * from"
          " (select members.customer_id, members.join_date, sales.order_date, menu.product_name, "
          "row_number() over(partition by members.customer_id order by sales.order_date desc) as r_count "
          "from members join sales on members.customer_id = sales.customer_id join menu on menu.product_id = sales.product_id "
          "where members.join_date > sales.order_date) as a"
          " where r_count = 1").show()

print("-- 8. What is the total items and amount spent for each member before they became a member?")

spark.sql("select mem.customer_id, count(s.product_id) as items_purchased, sum(m.price) as amt_spent from members mem join sales s on mem.customer_id = s.customer_id "
          "join menu m on s.product_id = m.product_id where s.order_date < mem.join_date group by mem.customer_id order by mem.customer_id").show()


print("-- 9.  If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?")

spark.sql("select customer_id, sum(case when m.product_id = 1 then m.price * 20 else m.price * 10 end) as points_earned from "
          "menu m join sales s on m.product_id = s.product_id group by customer_id order by points_earned").show()

print("-- 10. In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at")
print("the end of January?")

spark.sql("select s.customer_id, sum(case when s.order_date between mem.join_date and mem.join_date + interval 6 day then m.price * 20 else "
          "case when m.product_id = 1 then m.price * 20 else m.price * 10 end end) as points_aquired "
          "from members mem join sales s on s.customer_id = mem.customer_id join menu m on m.product_id = s.product_id "
          "where s.order_date < '2021-02-01' group by s.customer_id order by points_aquired desc").show()



