import scala.io.{BufferedSource, Source}
import scala.util.{Success, Try, Using}

object Utils {
  def readFromFile[T](path: String)(implicit f: BufferedSource => T): Try[T] =
    Using(Source.fromFile(path)) { f(_) }

  implicit val readList: BufferedSource => List[Int] =
    s => s.bufferedReader().readLine().split(",").toList.map(_.toInt)

  def input[T](raw: Try[T]): T = raw match {
    case Success(v) => v
  }
}
