import org.jsoup.Jsoup
import org.jsoup.nodes.Document
import java.io.File
import java.io.PrintWriter


fun main() {
    val stopWords = File("src/main/resources/stopWords.txt").readLines()
    val urlList = listOf(
        "https://xn--m1abb8a.xn--p1ai/nirs-uirs/"
    )
    val printWriter = PrintWriter(File("src/main/resources/fromLinks/clean-words.txt"))
    for((index, url) in urlList.withIndex()) {
        val doc: Document = Jsoup.connect(url).get()
        with(printWriter){
            doc.select("p")
                .map { """[а-яА-Я]+""".toRegex()
                    .findAll(it.text())
                    .map { match -> match.value.lowercase() }
                    .filter { value -> value !in stopWords }
                    .joinToString(separator = " ")}
                .forEach { this.println(it) }
            this.flush()
        }
    }
}