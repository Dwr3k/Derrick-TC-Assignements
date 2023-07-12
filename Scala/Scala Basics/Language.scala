class Language{

  private[this] var _LangArticle: Int = -0
  private[this] var _LangName: String = ""

  def this(i:Int, s:String) = {
    this()
     _LangArticle = i
     _LangName = s
  }

  private def setLangArticle(i:Int): Unit = {
    _LangArticle = i
  }

  private def setLangName(s:String): Unit = {
    _LangName = s
  }

  def getLangArticle(): Int = {_LangArticle}
  def getLangName(): String = {_LangName}

  override def toString(): String = {
    return "Total Articles: " + _LangArticle + "\n" + "Name: " + _LangName
  }
}

object LanguageMain {
  def main(args: Array[String]): Unit = {
//    val language: Language = new Language(50, "Scala")
//    print(language.toString())

    case class emp(fnamp: String, age: Int) {
      val a = emp("Derrick", 23)
      a match {
        case emp("Derrick", 23) => println("Hello Drem")
        case emp("Chris", 21) => println("Hello Abhilash")

      }
  }
}


}