import java.io.File
import java.io.FileNotFoundException
import java.util.*
import java.util.stream.Collectors

fun main() {
    val normalized = Scanner(File("src/main/resources/normalized/normalized.txt"))
        .useDelimiter("\\s+")
        .tokens()
        .collect(Collectors.toSet())
    for(file in File("src/main/resources/words").listFiles() ?: throw FileNotFoundException()){
        val topics = Scanner(file)
            .useDelimiter("\\s+")
            .tokens()
            .collect(Collectors.toSet())
        val jaccard = normalized.intersect(topics).size.toDouble() / normalized.union(topics).size.toDouble()
        println(jaccard)
    }
}