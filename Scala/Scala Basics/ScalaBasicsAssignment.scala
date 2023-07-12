class ScalaBasicsAssignment {

  var exBoolean:Boolean = false
  var exByte:Byte = 12
  var exShort:Short = 15
  var exLong:Long = 1222144424
  var exDouble:Double = 12.24
  var exString:String = "The String"
}

object HelloWorld {

  var exChar: Char = 'd'
  var exInt: Int = 423

  def combineStringNumber(x: Int, str: String):String = str + x
  def combineAgain(x: Int) = (y: String) => x + y;
  def combine(x: Int)(y: String)(z: Boolean):String = x + y + z;

  def math(x:Double, y:Double, z:Double, f:(Double,Double)=>Double): Double = f(f(x,y), z);
  def main(args: Array[String]): Unit = {
    println("Hello, world!")
    println(s"$exChar is $exInt")

    var result = math(50,20,10,_+_)

    var stringAnon = (x:Int, y:String) => x+y;
    println(stringAnon(12, "This is basically combineStringNumber"))

    var makeDecision:Boolean = false

    if(makeDecision){println("Made Decision")}
    else if(!makeDecision){println("Did not make decision")}
    else{println("This line will never execute")}

    for(i <- 0 to 10){
      print(s"$i ")
    }
    println("")
    for(i <- 0 until 10){
      print(s"$i ")
    }
    println("")
    for(i <- 0 to 5; k <- 6 to 10){println(s"$i $k")}
    println("")
    var counter:Int = 0
    while(counter < 10){
      println(s"While Counter at :$counter")
      counter = counter+1
    }
    counter = 0
    do{
      println(s"Do While Counter at :$counter")
      counter = counter+1
    }while(counter < 10)

    println("")

    var matchString:String = "Green"

    matchString match{
      case "Red" => println("colour red")
      case "Green" => println("colour green (the best colour)")
      case _ => println("Not a valid colour")
    }
    matchString = "Red"
    var resultString = matchString match{
      case "Red" => "colour red"
      case "Green" => "colour green (the best colour)"
      case _ => "Not a valid colour"
    }
    println(resultString)

    println(combineStringNumber(12, "Derrick"))
    println(combineAgain(12)("20"))
    var testDef = combineAgain(144)
    println(testDef("Crazy"))
    var testThree = combine(12)("Tat")_
    println(testThree(true))

    var fname:String = "Derrick"
    var lname:String = "McGlone"

    printf("%s has %d letters in his first name\n", fname, fname.length())
    println("And %d letters in his last name %s".format(lname.length(), lname))


    val tempArray: Array[Int] = new Array[Int](2)
    tempArray(0) = 1
    tempArray(1) = 2
    println(tempArray(1))

    for(x <- tempArray){
      println(x)
    }

    var templist:List[String] = List("1", "2", "3")
    println(1::5::9::Nil)
    println(templist.head)
    println(templist.reverse)
    for(x <- templist.reverse){
      println(x)
    }
    println(List.fill(2)("rabbit"))
    var  sum:String = "String "
    templist.foreach(sum+=_)
    println(sum)

    var tempSet: Set[Int] = Set(1,2,3,4,5,6,7,8,9)
    var evenSet: Set[Int] = Set(2,4,6,8)

    println(tempSet ++ evenSet)
    println(tempSet.intersect(evenSet))
    println(tempSet.union(evenSet))

    var newSet:Set[Int] = Set()
    tempSet.foreach(x => newSet += x)
    println(newSet)

    var tempMap:Map[Int, String] = Map(12 -> "Drem", 13 -> "Chris", 14 -> "Mom")
    println(tempMap ++ Map(1 -> "Test"))

    val tempTuple = (1,2,"hello", true)
    val com = (5, (1, 2),13)
    println(tempTuple._3)
    tempTuple.productIterator.foreach{
      i => println(i)
    }
    println(com._2._2)
    println(1,2,3, 1->"Tom"->true)

    val tempOption: Option[Int] = Some(5)
    val nullOption: Option[Int] = None

    println(tempOption.get)
    println(nullOption.isEmpty)

    print(templist.find(_ > "4").getOrElse("Not found"))

    var intList:List[Int] = List(1,2,3,4,5,6,7,8,9,10)
    println(intList.map(x => x*3))
    println("hello".map(_.toUpper))
    var intMap:Map[Int, String] = Map(1->"Derrick",  2->"Chris")
    println(intMap.mapValues(x => x + "mapped"))
    println(List(List(1,2,3), List(3,4,5)).flatten)
    println(intList.flatMap(x => List(x, x+1)))
    println(intList.filter(x => x%5 == 0))

    println(intList.reduceLeft(_ + _))
    println(templist.reduceRight(_+_))
    println("")
    println(intList.reduceLeft((x,y) => {println(x+" , "+y);x+y}))

    println(intList.foldLeft(10)(_+_))
    println("")

    println(intList)
    println(intList.scanLeft(100)(_+_))







  }
  }



