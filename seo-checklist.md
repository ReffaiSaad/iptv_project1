# SEO Checklist — IPTV Premium (Yoast 2026)

> Utilisez ce document pour valider chaque page avant mise en ligne.  
> ✅ = Conforme | ❌ = À corriger | ⚠️ = À vérifier

---

## Checklist globale (toutes les pages)

### Balises techniques
- [ ] `<title>` unique, entre 50-60 caractères, contient le mot-clé principal.
- [ ] `<meta name="description">` unique, entre 120-160 caractères, attrayante.
- [ ] `<link rel="canonical">` pointe vers l'URL exacte de la page.
- [ ] `hreflang="fr-FR"` et `hreflang="x-default"` présents.
- [ ] `<meta name="robots" content="index, follow">` (sauf pages noindex).
- [ ] `<html lang="fr" dir="ltr">` présent.
- [ ] `<meta name="viewport">` présent.

### Open Graph & Twitter Cards
- [ ] `og:title`, `og:description`, `og:image`, `og:url`, `og:type` présents.
- [ ] `twitter:card`, `twitter:title`, `twitter:description`, `twitter:image` présents.
- [ ] L'image OG pointe vers une image réelle (minimum 1200×630 px recommandé).

### Contenu & Structure
- [ ] Un seul `<h1>` par page contenant le mot-clé cible.
- [ ] Hiérarchie H1 → H2 → H3 respectée (pas de sauts).
- [ ] Longueur de contenu ≥ 300 mots (pages légales) / ≥ 800 mots (blog).
- [ ] Mot-clé cible présent dans H1, premier paragraphe, et au moins un H2.
- [ ] Liens internes vers pages pertinentes (minimum 3 par page de contenu).
- [ ] Lien externe de qualité vers source autoritaire (blog articles).
- [ ] Images avec attribut `alt` descriptif contenant le mot-clé si pertinent.
- [ ] Aucune page orpheline (toutes reliées par la navigation ou des liens internes).

### Performance
- [ ] Score Lighthouse Performance ≥ 90 (tester via Chrome DevTools).
- [ ] Toutes les images optimisées (WebP recommandé, < 100 Ko chacune).
- [ ] Pas de render-blocking resources inutiles.
- [ ] CSS critique inliné ou en `<head>`.

### Accessibilité (WCAG AA)
- [ ] `skip-link` "Passer au contenu principal" présent et fonctionnel.
- [ ] Tous les boutons ont un `aria-label` ou un texte visible.
- [ ] Ratio de contraste couleur/fond ≥ 4.5:1.
- [ ] Navigation au clavier fonctionnelle sur tous les éléments interactifs.
- [ ] `<main id="main-content">` présent.

---

## Checklist par type de page

### Pages de contenu (Avantages, Chaînes, Installation…)

- [ ] Schema BreadcrumbList implémenté.
- [ ] Image hero avec attribut `alt`.
- [ ] CTA WhatsApp visible sans scroll (above the fold) sur mobile.
- [ ] Sticky CTA mobile visible au scroll.

### Pages tarifs

- [ ] Schema `Product` + `Offer` avec `price`, `priceCurrency`, `availability`.
- [ ] Prix 3 mois (199€), 6 mois (299€), 12 mois (499€) correctement renseignés.
- [ ] Tableau de comparaison lisible sur mobile.

### Page FAQ

- [ ] Schema `FAQPage` avec `Question` et `Answer` pour chaque entrée.
- [ ] Au minimum 8 questions/réponses.
- [ ] Réponses complètes (≥ 50 mots chacune).

### Page Avis

- [ ] Schema `AggregateRating` avec `ratingValue`, `ratingCount`, `reviewCount`.
- [ ] Au minimum 6 avis individuels avec `Review` schema.
- [ ] Note ≥ 4.5/5 affichée visuellement.

### Articles de blog

- [ ] Schema `BlogPosting` avec `headline`, `datePublished`, `dateModified`, `author`, `publisher`.
- [ ] Auteur identifié (nom réel).
- [ ] Date de publication visible dans l'article.
- [ ] Image mise en avant (og:image).
- [ ] BreadcrumbList : Accueil → Blog → Titre de l'article.
- [ ] Lien vers tarifs.html ou essai-gratuit.html en conclusion.

### Articles tutoriels (Smart TV, Firestick)

- [ ] Schema `HowTo` avec `step` listés individuellement.
- [ ] Instructions numérotées avec `<ol>`.
- [ ] Temps estimé de réalisation indiqué.
- [ ] Troubleshooting section présente.

### Pages légales (CGU, RGPD, Cookies…)

- [ ] `<meta name="robots" content="index, follow">` (sauf merci.html).
- [ ] Date de dernière mise à jour visible.
- [ ] Liens croisés entre les pages légales.

### Page merci.html

- [ ] `<meta name="robots" content="noindex, nofollow">`.
- [ ] Instructions claires sur les prochaines étapes.
- [ ] Lien vers WhatsApp pour suivi.

---

## Vérification des données structurées

Utilisez ces outils pour valider chaque page :

| Outil | URL | Usage |
|-------|-----|-------|
| Rich Results Test | [search.google.com/test/rich-results](https://search.google.com/test/rich-results) | Valider Schema.org |
| Schema Markup Validator | [validator.schema.org](https://validator.schema.org) | Valider JSON-LD |
| Open Graph Debugger | [developers.facebook.com/tools/debug](https://developers.facebook.com/tools/debug) | Valider OG tags |
| Twitter Card Validator | [cards-dev.twitter.com/validator](https://cards-dev.twitter.com/validator) | Valider Twitter Cards |
| PageSpeed Insights | [pagespeed.web.dev](https://pagespeed.web.dev) | Score Performance |
| W3C HTML Validator | [validator.w3.org](https://validator.w3.org) | Valider HTML |

---

## Pages validées

| Page | Title OK | Meta OK | H1 OK | Schema OK | Perf OK | Liens internes |
|------|----------|---------|-------|-----------|---------|----------------|
| index.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| avantages.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| tarifs.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| chaines.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| installation.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| essai-gratuit.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| faq.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| avis.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| a-propos.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| contact.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| smart-tv.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| android-tv.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| firestick.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| ios.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| mag-box.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| pc-mac.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| formuler-enigma.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| blog.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| blog/meilleur-iptv-france.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| blog/abonnement-iptv-premium.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| blog/iptv-france-legal.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| blog/installer-iptv-smart-tv.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| blog/tutoriel-iptv-firestick.html | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

---

*Checklist générée le 19 Juin 2026 — IPTV Premium*
