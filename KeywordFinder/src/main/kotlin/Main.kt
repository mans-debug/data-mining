import java.io.File
import java.io.FileNotFoundException
import java.util.*
import java.util.stream.Collectors
import kotlin.collections.ArrayList
import kotlin.math.pow
import kotlin.math.sqrt

fun main() {
    //получить все слова
    val normalized: List<String> = Scanner(File("src/main/resources/normalized/normalized.txt"))
        .useDelimiter("\\s+")
        .tokens()
        .collect(Collectors.toList())
    val topics: ArrayList<List<String>> = ArrayList()
    var words: Set<String> = setOf(*(normalized.toTypedArray()))
    for (file in File("src/main/resources/words").listFiles() ?: throw FileNotFoundException()) {
        val topic = Scanner(file)
            .useDelimiter("\\s+")
            .tokens()
            .collect(Collectors.toList())
        topics.add(topic)
        words = words.union(topic.toSet())
    }
    //все слова с индексами
    val wordsIndexed = words.toList()
    var normVector: Array<Double> = wordListToVector(wordsIndexed, targetList = normalized)
    var topicsVector: List<Array<Double>> = topics.map { wordListToVector(wordsIndexed, it) }.toList()

    normVector = normVector.map { it / sqrtSumOfSquares(normVector) }.toTypedArray()
    topicsVector = topicsVector.map { array -> array.map { it / sqrtSumOfSquares(array) }.toTypedArray() }


    val res0 = normVector.asSequence().mapIndexed { index, d -> d * topicsVector[0][index] }.sum()
    val res1 = normVector.asSequence().mapIndexed { index, d -> d * topicsVector[1][index] }.sum()
    val res2 = normVector.asSequence().mapIndexed { index, d -> d * topicsVector[2][index] }.sum()
    val res3 = normVector.asSequence().mapIndexed { index, d -> d * topicsVector[3][index] }.sum()

    println(res0)
    println(res1)
    println(res2)
    println(res3)


}

fun sqrtSumOfSquares(vector: Array<Double>): Double = sqrt(vector.reduce { acc, d -> acc + d.pow(2) })

fun wordListToVector(words: List<String>, targetList: List<String>): Array<Double> {
    val vector = Array(words.size) { 0.0 }//double arr
    targetList.groupBy { it }.forEach { vector[words.indexOf(it.key)] = it.value.size.toDouble() }
    return vector
}