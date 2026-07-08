import org.springframework.jdbc.core.JdbcTemplate
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RequestParam
import org.springframework.web.bind.annotation.RestController

@RestController
class UserController(private val jdbcTemplate: JdbcTemplate) {

    // VULNÉRABLE : Ne jamais faire ceci en production
    @GetMapping("/user")
    fun getUser(@RequestParam("id") id: String): String {
        // La concaténation directe permet à un attaquant d'injecter du SQL 
        // (ex: ?id=1 OR 1=1)
        val sql = "SELECT username FROM users WHERE id = '" + id + "'"
        
        return try {
            jdbcTemplate.queryForObject(sql, String::class.java) ?: "Utilisateur non trouvé"
        } catch (e: Exception) {
            "Erreur lors de la récupération"
        }
    }
}
