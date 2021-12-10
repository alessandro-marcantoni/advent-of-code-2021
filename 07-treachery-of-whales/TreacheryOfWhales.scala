import Utils._
import TreacheryOfWhalesSolution._

object TreacheryOfWhalesSolution {
  val path = "07-treachery-of-whales/07-treachery-of-whales-input.txt"

  def distanceFrom(point: Int)(implicit list: List[Int]): Int =
    list.map(i => Math.abs(point - i)).sum

  def notLinearDistanceFrom(point: Int)(implicit list: List[Int]): Int =
    list.flatMap(i => LazyList.iterate(1)(_ + 1).take(Math.abs(point - i))).sum
}

object TreacheryOfWhales extends App {
  implicit val list: List[Int] = input(readFromFile(path))
  println(LazyList.iterate(0)(_ + 1).take(list.max).map(distanceFrom).min)
  println(LazyList.iterate(0)(_ + 1).take(list.max).map(notLinearDistanceFrom).min)
}
