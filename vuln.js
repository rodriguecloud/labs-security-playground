import express, { Request, Response } from 'express';
import cookieParser from 'cookie-parser';
import csrf from 'csurf';
import session from 'express-session';

const app = express();

// Configuration de la session
app.use(session({
    secret: 'your-secret-key-change-this-in-production',
    resave: false,
    saveUninitialized: true,
    cookie: { 
        secure: true, // HTTPS only
        httpOnly: true,
        sameSite: 'strict'
    }
}));

app.use(cookieParser());
app.use(express.urlencoded({ extended: false }));

// Protection CSRF avec csurf middleware
const csrfProtection = csrf({ cookie: false });

// Simulation d'une vérification d'authentification simpliste
const authMiddleware = (req: Request, res: Response, next: Function) => {
    if (req.cookies.session_id === 'secret-user-token') {
        next();
    } else {
        res.status(401).send('Non autorisé');
    }
};

// ENDPOINT SÉCURISÉ : Protection CSRF activée
app.post('/transfer', authMiddleware, csrfProtection, (req: Request, res: Response) => {
    const { amount, to } = req.body;
    
    // Validation du token CSRF
    try {
        // Le token CSRF a été validé automatiquement par le middleware
        console.log(`Transfert de ${amount} vers ${to} effectué.`);
        res.send(`Transfert de ${amount} effectué.`);
    } catch (err) {
        res.status(403).send('Token CSRF invalide');
    }
});

// Route pour obtenir le token CSRF (à appeler avant le formulaire)
app.get('/csrf-token', csrfProtection, (req: Request, res: Response) => {
    res.json({ csrfToken: req.csrfToken() });
});

app.listen(3000, () => console.log('Serveur démarré sur le port 3000'));
