fun main() {
    println("""[а-яА-Я]+""".toRegex().findAll("я ебу, собак!").joinToString { it.value })
}