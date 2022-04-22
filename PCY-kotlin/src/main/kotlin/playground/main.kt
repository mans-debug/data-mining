package playground

import java.io.File


fun main(args: Array<String>) {
    val path = "src\\main\\resources\\transactions.csv"
    val support = 2
    val itemCountMap: Map<String, Int> = countItems(path)
    val itemKey = itemCountMap.keys

    val hashBucket = HashMap<Int, ArrayList<Pair<String, String>>>()
    for ((basket, items) in getBaskets(path)) {
        for (pair in getDoubleTones(items)) {
            val hash = (itemKey.indexOf(pair.first) + itemKey.indexOf(pair.second) + 2) % itemKey.size
            if (hashBucket.putIfAbsent(hash, arrayListOf(pair)) === null) else hashBucket[hash]!!.add(pair)
        }
    }
    val finalPairs: List<Pair<String, String>> = secondPass(hashBucket, support= support)
    val pairs = finalPairs.map { it.toString() }
    val singles = itemCountMap.filter { it.value >= support }

    val destructured = pairs + itemCountMap.filter { it.value >= support }
    for (pair in destructured)
        println(pair)
    println("SinglesQuantity: ${singles.size}\tPairsQuantity: ${pairs.size}")
}

private fun countItems(path: String) = File(path)
    .readLines()
    .map { it.split(";") }
    .map { it[0] }
    .groupBy { it }
    .mapValues { it.value.count() }

fun getBaskets(filePath: String): Map<String, List<String>> = File(filePath)
    .readLines()
    .map { it.split(";") }
    .groupBy { it[1] }
    .mapValues { it.value.map { pb -> pb[0] } }

fun getDoubleTones(list: List<String>): List<Pair<String, String>> {
    val doubletones = ArrayList<Pair<String, String>>()
    for (value in list) {
        for (i in list.indexOf(value) + 1 until list.size) {
            doubletones += value to list[i]
        }
    }
    return doubletones
}

private fun secondPass(
    hashBucket: HashMap<Int, ArrayList<Pair<String, String>>>,
    support: Int = 3
) = hashBucket
    .filter { it.value.size >= support }
    .flatMap {
        it.value
            .groupBy { pair -> pair }
            .filter { pairMap -> pairMap.value.size >= support }
            .flatMap { pairMap -> pairMap.value }
            .distinct()
    }



