# IPTV Premium — README de livraison

## 🌐 Site web : iptvpremium.se

Site IPTV en français, ciblant la France. Construit en HTML/CSS/JS natif, mobile-first, optimisé SEO Yoast 2026.

---

## 📁 Structure des fichiers

```
khadma/
├── index.html                    ← Page d'accueil (H1 cible : IPTV France)
├── avantages.html                ← Avantages & technologie Anti-Freeze
├── tarifs.html                   ← Tarifs 3/6/12 mois (Schema Product)
├── chaines.html                  ← Catalogue chaînes & VOD
├── installation.html             ← Guide multi-appareils
├── essai-gratuit.html            ← CTA essai 24h WhatsApp
├── faq.html                      ← FAQ (Schema FAQPage)
├── avis.html                     ← Avis (Schema AggregateRating)
├── a-propos.html                 ← E-E-A-T & équipe
├── contact.html                  ← Contact WhatsApp
│
├── smart-tv.html                 ← Landing page Samsung & LG
├── android-tv.html               ← Landing page Android TV
├── firestick.html                ← Landing page Fire TV Stick
├── ios.html                      ← Landing page iPhone & Apple TV
├── mag-box.html                  ← Landing page MAG Box
├── pc-mac.html                   ← Landing page PC & Mac
├── formuler-enigma.html          ← Landing page Formuler & Enigma2
│
├── blog.html                     ← Index du blog
├── blog/
│   ├── meilleur-iptv-france.html        ← KW: meilleur IPTV France
│   ├── abonnement-iptv-premium.html     ← KW: abonnement IPTV Premium
│   ├── iptv-france-legal.html           ← KW: IPTV légal France
│   ├── installer-iptv-smart-tv.html     ← KW: installer IPTV Smart TV (HowTo schema)
│   └── tutoriel-iptv-firestick.html     ← KW: IPTV Firestick (HowTo schema)
│
├── merci.html                    ← Confirmation commande (noindex)
├── 404.html                      ← Page d'erreur personnalisée
├── plan-du-site.html             ← HTML Sitemap
│
├── conditions-generales.html     ← CGU
├── politique-confidentialite.html ← RGPD Privacy Policy
├── politique-remboursement.html  ← Refund Policy
├── politique-cookies.html        ← Cookie Policy (ePrivacy)
├── clause-non-responsabilite.html ← Disclaimer
│
├── sitemap.xml                   ← XML Sitemap (28 URLs)
├── robots.txt                    ← Directives crawl
├── manifest.json                 ← PWA Web App Manifest
├── logo.svg                      ← Logo vectoriel IPTV Premium
├── favicon.png                   ← Favicon (à générer ou remplacer)
└── style.css                     ← Feuille de style globale
```

---

## 🚀 Mise en ligne — Liste de vérification

### 1. Hébergement & DNS

- [ ] Pointer le domaine `iptvpremium.se` vers votre serveur d'hébergement.
- [ ] Activer le certificat SSL/TLS (HTTPS) — obligatoire pour le SEO Google.
- [ ] Configurer les redirections 301 : `www.iptvpremium.se` → `iptvpremium.se`.
- [ ] Configurer la page d'erreur 404 : pointer vers `404.html`.

### 2. Google Search Console

1. Connectez-vous à [search.google.com/search-console](https://search.google.com/search-console).
2. Ajoutez la propriété `https://iptvpremium.se` (méthode préférée : balise HTML meta ou fichier TXT).
3. Soumettez le sitemap : `https://iptvpremium.se/sitemap.xml`.
4. Vérifiez l'absence d'erreurs dans le rapport « Couverture ».
5. Utilisez l'outil d'inspection d'URL pour demander l'indexation de la page d'accueil.

### 3. Google Analytics 4 (GA4)

1. Créez une propriété GA4 sur [analytics.google.com](https://analytics.google.com).
2. Copiez votre ID de mesure (format : `G-XXXXXXXXXX`).
3. Ajoutez le snippet de tracking dans le `<head>` de chaque page HTML (ou via Google Tag Manager) :

```html
<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

4. Configurez un événement de conversion sur les clics WhatsApp.

### 4. Bing Webmaster Tools

1. Connectez-vous à [bing.com/webmasters](https://www.bing.com/webmasters).
2. Ajoutez votre site et vérifiez la propriété.
3. Importez depuis Google Search Console (option disponible dans le tableau de bord Bing).
4. Soumettez le sitemap XML.

### 5. Favicon

- Le fichier `favicon.png` est référencé dans toutes les pages mais doit être généré (recommandé : 512×512 px minimum).
- Utilisez [realfavicongenerator.net](https://realfavicongenerator.net) pour générer tous les formats nécessaires.

---

## 💬 WhatsApp — Liens de conversion

Tous les CTAs du site pointent vers : `https://wa.me/212688017429`

Les messages sont pré-remplis selon le contexte :
- Essai gratuit : `?text=Bonjour%2C%20je%20souhaite%20obtenir%20un%20essai%20gratuit%20de%2024h%20pour%20IPTV%20Premium.`
- Commande : `?text=Bonjour%2C%20je%20souhaite%20souscrire%20%C3%A0%20un%20abonnement%20IPTV%20Premium.`
- Info générale : `?text=Bonjour%2C%20je%20souhaite%20avoir%20des%20informations%20sur%20vos%20abonnements%20IPTV%20Premium.`

---

## 🔧 Performance & Maintenance

- Toutes les images utilisent `loading="lazy"` et des attributs `alt` descriptifs.
- Le CSS utilise des variables CSS natives pour faciliter les modifications de couleurs.
- Les animations utilisent `will-change: transform` pour l'accélération GPU.
- **Pas de framework JavaScript** — le site charge en < 1 seconde sur réseau 4G.

---

## 📊 Résumé du contenu SEO

| Page | Mot-clé Cible | Schema |
|------|--------------|--------|
| index.html | IPTV France Premium | Organization, WebSite, Product |
| tarifs.html | abonnement IPTV prix | Product, Offer |
| faq.html | IPTV FAQ France | FAQPage |
| avis.html | IPTV Premium avis | AggregateRating, Review |
| blog/meilleur-iptv-france.html | meilleur IPTV France | BlogPosting |
| blog/installer-iptv-smart-tv.html | installer IPTV Smart TV | HowTo, BlogPosting |
| blog/tutoriel-iptv-firestick.html | IPTV Firestick | HowTo, BlogPosting |

---

*Livré par IPTV Premium — Juin 2026*
