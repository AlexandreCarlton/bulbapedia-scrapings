import logging
from pathlib import Path

from bulbascraper.pokemon_factory import PokemonFactory
from bulbascraper.image_downloader import ImageDownloader
from bulbascraper.pokemon_list_by_national_pokedex_number import PokemonListByNationalPokedexNumber
from bulbascraper.pokemon_list_by_ability import PokemonListByAbility

logging.basicConfig(level=logging.DEBUG)

wikimedia_path = Path('wikimedia')
image_path = Path('images')

factory = PokemonFactory(wikimedia_path / 'pokemon')
pokemon_list = PokemonListByNationalPokedexNumber(wikimedia_path)
pokemon_abilities = PokemonListByAbility(wikimedia_path)
official_artwork_downloader = ImageDownloader(image_path / 'official_artwork')
menu_sprite_downloader = ImageDownloader(image_path / 'menu_sprites')


for pokemon_name in pokemon_list:
    # Downloads the wiki file if not present.
    logging.info("Loading page for %s...", pokemon_name)
    pokemon_wiki_page = factory.make_pokemon_wiki_page(pokemon_name)

    # Grab official artwork
    for image_filename in pokemon_wiki_page.images.values():
        image_path = official_artwork_downloader.directory / image_filename
        logging.info("Checking image filename %s", image_filename)
        if not image_path.exists():
            logging.info("Attemting to download filename %s", image_filename)
            official_artwork_downloader.download_image(image_filename)

# Download menu sprites
for ability in pokemon_abilities:
    menu_sprite_filename = ability.menu_sprite + 'MS.png'
    menu_sprite_path = menu_sprite_downloader.directory / menu_sprite_filename
    logging.info("Checking menu sprite filename %s", menu_sprite_filename)
    if not menu_sprite_path.exists():
        logging.info("Attempting to download filename %s", menu_sprite_filename)
        menu_sprite_downloader.download_image(menu_sprite_filename)
