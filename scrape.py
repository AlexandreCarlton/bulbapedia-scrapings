import logging
from pathlib import Path

from bulbascraper.pokemon_factory import PokemonFactory
from bulbascraper.image_downloader import ImageDownloader
from bulbascraper.pokemon_list_by_national_pokedex_number import PokemonListByNationalPokedexNumber

logging.basicConfig(level=logging.DEBUG)

wikimedia_path = Path('wikimedia')
image_path = Path('images')

factory = PokemonFactory(wikimedia_path / 'pokemon')
pokemon_list = PokemonListByNationalPokedexNumber(wikimedia_path)
image_downloader = ImageDownloader(image_path)


for pokemon_name in list(pokemon_list)[717:]:
    # Downloads the wiki file if not present.
    logging.info("Downloading %s...", pokemon_name)
    pokemon_wiki_page = factory.make_pokemon_wiki_page(pokemon_name)

    # Grab images
    for image_filename in pokemon_wiki_page.images.values():
        logging.info("Checking image filename %s", image_filename)
        if not (image_path / image_filename).exists():
            logging.info("Attemting to download filename %s", image_filename)
            image_downloader.download_image(image_filename)
