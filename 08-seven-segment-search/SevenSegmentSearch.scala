import SevenSegmentSearchSolution._
import Utils._

import scala.io.BufferedSource

object SevenSegmentSearchSolution {
  case class Input(input: List[String], output: List[String])

  val path: String = "08-seven-segment-search/08-seven-segment-search-input.txt"

  def readStructure(s: BufferedSource): List[Input] =
    s.getLines().toList
      .map(s => s.split("\\|").map(_.strip).toList)
      .map(a => Input(a.head.split(" ").toList, a.last.split(" ").toList))

  def uniqueDigitsNumber(list: List[Input]): Int =
    list.map(_.output).map(_.count(unique)).sum

  def unique(string: String): Boolean = Set(2, 3, 4, 7).contains(string.length)

  def decode(string: Set[Char])(list: List[Set[Char]]): Int = string match {
    case s if s.size == 2 => 1
    case s if s.size == 4 => 4
    case s if s.size == 3 => 7
    case s if s.size == 7 => 8
    case s if s.size == 6 && list.find(e => e.size == 4).get.subsetOf(s) => 9
    case s if s.size == 6 && list.find(e => e.size == 3).get.subsetOf(s) => 0
    case s if s.size == 6 => 6
    case s if s.size == 5 && list.find(e => e.size == 3).get.subsetOf(s) => 3
    case s if s.size == 5 && s.subsetOf(list.find(e => decode(e)(list.diff(List(s))) == 6).get) => 5
    case s if s.size == 5 => 2
  }

  def getOutputNumber(input: Input): Int =
    input.output.map(e => decode(e.toSet)(input.input.map(_.toSet))).foldLeft(0)((acc, d) => acc * 10 + d)
}

object SevenSegmentSearch extends App {
  val list: List[Input] = input(readFromFile(path)(readStructure))
  println(uniqueDigitsNumber(list))
  println(list.map(getOutputNumber).sum)
}
