import express, { Request, Response } from 'express';
import cookieParser from 'cookie-parser';

const app = express();
app.use(cookieParser());

// Simulation d'une vérification d'authentification simpliste
const authMiddleware = (req: Request, res: Response, next: Function) => {
    if (req.cookies.session_id === 'secret-user-token') {
        next();
    } else {
        res.status(401).send('Non autorisé');
    }
};

// ENDPOINT VULNÉRABLE : Aucune protection contre le CSRF
app.post('/transfer', authMiddleware, (req: Request, res: Response) => {
    const { amount, to } = req.body;
    // Logique de transfert bancaire fictive
    console.log(`Transfert de ${amount} vers ${to} effectué.`);
    res.send(`Transfert de ${amount} effectué.`);
});

app.listen(3000, () => console.log('Serveur démarré sur le port 3000'));
