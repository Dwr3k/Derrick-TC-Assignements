trait A {
  def greet(): Unit = println("Hello from A")
}

trait B extends A{
  override def greet():Unit = {
    println("hello from B")
    super.greet()
  }
}

trait C extends A{
  override def greet():Unit = {
    println("hello from C")
    super.greet()
  }
}

class D extends B with C{
  def hello():Unit = greet()
}

trait TraitsDemo extends App {
  val d = new D()
  d.hello()
}
