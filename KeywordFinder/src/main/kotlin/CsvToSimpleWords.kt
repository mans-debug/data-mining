import java.io.File
import java.io.FileNotFoundException
import java.io.PrintWriter
import java.util.*

fun main(args: Array<String>) {
    val sourceDir = File("src/main/resources/wordCsv/")
    val txts : Array<File> = sourceDir.listFiles() ?: throw FileNotFoundException()
    val targetDir = File("${sourceDir.parent}/words")
    for (txt in txts){
        val sc = Scanner(txt)
        val writer = PrintWriter("${targetDir.path}/${txt.name}")
        while (sc.hasNextLine()){
            val newLine =
                """\W+""".toRegex().find(sc.nextLine())?.value
            writer.println(newLine)
        }
    }

}