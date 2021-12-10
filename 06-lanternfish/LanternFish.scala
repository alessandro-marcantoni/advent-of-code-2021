import LanternFishSolution._
import Utils._

object LanternFishSolution {
  val path = "06-lanternfish/06-lanternfish-input.txt"

  def toMap(list: List[Int]): Map[Int, Double] = list.groupBy(e => e).map(e => (e._1, e._2.length))

  def update(population: Map[Int, Double]): Map[Int, Double] = population.flatMap {
    case (0, n) => Map(8 -> n, 6 -> n)
    case (k, n) => Map(k - 1 -> (if (k - 1 != 6) n else n + population.getOrElse(0, 0.0)))
  }

  def updateUntil(population: Map[Int, Double], limit: Int): Map[Int, Double] =
    LazyList.iterate(population)(update).take(limit + 1).toList.last

  def count(population: Map[Int, Double]): Double = population.values.sum
}

object LanternFish extends App {
  val list: List[Int] = input(readFromFile(path))
  println(count(updateUntil(toMap(list), 80)))
  println(count(updateUntil(toMap(list), 256)))
}