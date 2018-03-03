# Bulbapedia Scrapings

Scrapings of [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Main_Page) so
that I may consistently test [`bulbascraper`](https://github.com/AlexandreCarlton/bulbascraper)
against a static source.

This uses [`git lfs`](https://git-lfs.github.com/) to store the images, so
cloning should be done with:

```
$ git lfs clone ssh://git@github.com:AlexandreCarlton/bulbapedia-scrapings.git
```

## Tweaks
I've had to make a few fixes to the articles in question.
However, I have not been able to make changes to some articles (as I lack the
necessary privileges), so I have recorded the changes here to allow scraping to
function normally.

### [List of Pokémon by National Pokédex Number](https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number)

```diff
	{{rdex|149|643|Reshiram|2|Dragon|Fire}}
-	{{rdex|150|644|Zekrom |2|Dragon|Electric}}
+	{{rdex|150|644|Zekrom|2|Dragon|Electric}}
	{{rdex|151|645|Landorus|2|Ground|Flying}}
```

### [Hoopa](https://bulbapedia.bulbagarden.net/wiki/Hoopa_%28Pokémon%29)

```diff
	===Stats===
+	====Base stats====
	=====Hoopa Confined=====
```
