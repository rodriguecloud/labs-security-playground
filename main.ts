// Exemple de configuration simple
const config = {
  port: 3000,
  // DANGER : Ne jamais faire cela en production
  apiKey: "mon_secret_tres_confidentiel_12345" 
};

function startServer() {
  console.log(`Le serveur démarre sur le port ${config.port}...`);
  console.log(`Clé API chargée : ${config.apiKey}`);
}

startServer();
