import os
import time
import requests
from bs4 import BeautifulSoup

URLS = [
    "https://vrising.fandom.com/wiki/Blood",
    "https://vrising.fandom.com/wiki/V_Rising",
    "https://vrising.fandom.com/wiki/Abilities",
    "https://vrising.fandom.com/wiki/Jewels",
    "https://vrising.fandom.com/wiki/Equipment",
    "https://vrising.fandom.com/wiki/Weapons",
    "https://vrising.fandom.com/wiki/Items",
    "https://vrising.fandom.com/wiki/V_Blood_Carriers",
    "https://vrising.fandom.com/wiki/Buildings",
    "https://vrising.fandom.com/wiki/Items",
    "https://vrising.fandom.com/wiki/Vendors",
    "https://vrising.fandom.com/wiki/Servants",
    "https://vrising.fandom.com/wiki/Journal",
    "https://vrising.fandom.com/wiki/Rift_Incursions",
    "https://vrising.fandom.com/wiki/Prison_Cell",
    "https://vrising.fandom.com/wiki/Horse",
    "https://vrising.fandom.com/wiki/Weapon_Skills",
    "https://vrising.fandom.com/wiki/Attributes",
    "https://vrising.fandom.com/wiki/Blood_Homogenizer",
    "https://vrising.fandom.com/wiki/Stats",
    "https://vrising.fandom.com/wiki/Soul_Shard_of_Dracula",
    "https://vrising.fandom.com/wiki/Soul_Shard_of_the_Monster",
    "https://vrising.fandom.com/wiki/Soul_Shard_of_Solarus",
    "https://vrising.fandom.com/wiki/Soul_Shard_of_the_Winged_Horror",
    "https://vrising.fandom.com/wiki/Soul_Shard_of_the_Serpent",
    "https://vrising.fandom.com/wiki/Altar_of_Stygian_Awakening",
    "https://vrising.fandom.com/wiki/Tailor%27s_Flooring",
    "https://vrising.fandom.com/wiki/Library_Flooring",
    "https://vrising.fandom.com/wiki/Forge_Flooring",
    "https://vrising.fandom.com/wiki/Workshop_Flooring",
    "https://vrising.fandom.com/wiki/Jeweller%27s_Chamber_Flooring",
    "https://vrising.fandom.com/wiki/Alchemy_Lab_Flooring",
    "https://vrising.fandom.com/wiki/Crypt_Flooring",
    "https://vrising.fandom.com/wiki/Castle_Flooring",
    "https://vrising.fandom.com/wiki/Emery",
    "https://vrising.fandom.com/wiki/Legendary_Ancestral_Weapon_Shards",
    "https://vrising.fandom.com/wiki/Onyx_Tear",
    "https://vrising.fandom.com/wiki/Stables",
    "https://vrising.fandom.com/wiki/Shadowbolt",
    "https://vrising.fandom.com/wiki/Blood_Rite",
    "https://vrising.fandom.com/wiki/Blood_Rage",
    "https://vrising.fandom.com/wiki/Veil_of_Blood",
    "https://vrising.fandom.com/wiki/Blood_Fountain",
    "https://vrising.fandom.com/wiki/Sanguine_Coil",
    "https://vrising.fandom.com/wiki/Carrion_Swarm",
    "https://vrising.fandom.com/wiki/Crimson_Beam",
    "https://vrising.fandom.com/wiki/Heart_Strike",
    "https://vrising.fandom.com/wiki/Chaos_Volley",
    "https://vrising.fandom.com/wiki/Power_Surge",
    "https://vrising.fandom.com/wiki/Aftershock",
    "https://vrising.fandom.com/wiki/Veil_of_Chaos",
    "https://vrising.fandom.com/wiki/Void",
    "https://vrising.fandom.com/wiki/Chaos_Barrier",
    "https://vrising.fandom.com/wiki/Rain_of_Chaos",
    "https://vrising.fandom.com/wiki/Merciless_Charge",
    "https://vrising.fandom.com/wiki/Chaos_Barrage",
    "https://vrising.fandom.com/wiki/Corrupted_Skull",
    "https://vrising.fandom.com/wiki/Ward_of_the_Damned",
    "https://vrising.fandom.com/wiki/Bone_Explosion",
    "https://vrising.fandom.com/wiki/Veil_of_Bones",
    "https://vrising.fandom.com/wiki/Death_Knight",
    "https://vrising.fandom.com/wiki/Soulburn",
    "https://vrising.fandom.com/wiki/Unholy_Chains",
    "https://vrising.fandom.com/wiki/Army_Of_The_Dead",
    "https://vrising.fandom.com/wiki/Volatile_Arachnid",
    "https://vrising.fandom.com/wiki/Spectral_Wolf",
    "https://vrising.fandom.com/wiki/Phantom_Aegis",
    "https://vrising.fandom.com/wiki/Wraith_Spear",
    "https://vrising.fandom.com/wiki/Veil_of_Illusion",
    "https://vrising.fandom.com/wiki/Mosquito_(Spell)",
    "https://vrising.fandom.com/wiki/Mist_Trance",
    "https://vrising.fandom.com/wiki/Curse",
    "https://vrising.fandom.com/wiki/Spectral_Guardian",
    "https://vrising.fandom.com/wiki/Wisp_Dance",
    "https://vrising.fandom.com/wiki/Frost_Bat",
    "https://vrising.fandom.com/wiki/Cold_Snap",
    "https://vrising.fandom.com/wiki/Ice_Nova",
    "https://vrising.fandom.com/wiki/Veil_of_Frost",
    "https://vrising.fandom.com/wiki/Crystal_Lance",
    "https://vrising.fandom.com/wiki/Frost_Barrier",
    "https://vrising.fandom.com/wiki/Arctic_Storm",
    "https://vrising.fandom.com/wiki/Arctic_Leap",
    "https://vrising.fandom.com/wiki/Ice_Block",
    "https://vrising.fandom.com/wiki/Cyclone",
    "https://vrising.fandom.com/wiki/Discharge",
    "https://vrising.fandom.com/wiki/Ball_Lightning",
    "https://vrising.fandom.com/wiki/Polarity_Shift",
    "https://vrising.fandom.com/wiki/Lightning_Curtain",
    "https://vrising.fandom.com/wiki/Lightning_Tendrils",
    "https://vrising.fandom.com/wiki/Raging_Tempest",
    "https://vrising.fandom.com/wiki/Lightning_Typhoon",
    "https://vrising.fandom.com/wiki/Blood_Spray",
    "https://vrising.fandom.com/wiki/Sanguine_Mastery",
    "https://vrising.fandom.com/wiki/Chaos_Kindling",
    "https://vrising.fandom.com/wiki/Renewing_Flames",
    "https://vrising.fandom.com/wiki/Arcane_Animator",
    "https://vrising.fandom.com/wiki/Soul_Drinker",
    "https://vrising.fandom.com/wiki/Spiritual_Infusion",
    "https://vrising.fandom.com/wiki/Flowing_Sorcery",
    "https://vrising.fandom.com/wiki/Cold_Soul",
    "https://vrising.fandom.com/wiki/Chillweave",
    "https://vrising.fandom.com/wiki/Lightning_Fast_Strikes",
    "https://vrising.fandom.com/wiki/Enhanced_Conductivity",
    "https://vrising.fandom.com/wiki/Hunger_for_Blood",
    "https://vrising.fandom.com/wiki/Overpower",
    "https://vrising.fandom.com/wiki/Lethal_Strikes",
    "https://vrising.fandom.com/wiki/Feral_Hast",
    "https://vrising.fandom.com/wiki/Bastion",
    "https://vrising.fandom.com/wiki/Hunger_for_Power",
    "https://vrising.fandom.com/wiki/Rampage",
    "https://vrising.fandom.com/wiki/Ravenous_Strikes",
    "https://vrising.fandom.com/wiki/Embrace_Mayhem",
    "https://vrising.fandom.com/wiki/Wicked_Power",
    "https://vrising.fandom.com/wiki/Dark_Enchantment",
    "https://vrising.fandom.com/wiki/Turbulent_Velocity",
    "https://vrising.fandom.com/wiki/Summon_Fallen_Angel",
    "https://vrising.fandom.com/wiki/Voidquake_Vortex",
    "https://vrising.fandom.com/wiki/Eye_Of_The_Storm",
    "https://vrising.fandom.com/wiki/Serpent%27s_Kiss",
    "https://vrising.fandom.com/wiki/Blood_Storm",
    "https://vrising.fandom.com/wiki/Blood_Coating",
    "https://vrising.fandom.com/wiki/Chaos_Coating",
    "https://vrising.fandom.com/wiki/Frost_Coating",
    "https://vrising.fandom.com/wiki/Illusion_Coating",
    "https://vrising.fandom.com/wiki/Storm_Coating",
    "https://vrising.fandom.com/wiki/Unholy_Coating",
    "https://vrising.fandom.com/wiki/Elixir_of_the_Twisted",
    "https://vrising.fandom.com/wiki/Elixir_of_the_Blasphemous",
    "https://vrising.fandom.com/wiki/Elixir_of_the_Raven",
    "https://vrising.fandom.com/wiki/Elixir_of_the_Prowler",
    "https://vrising.fandom.com/wiki/Elixir_of_the_Beast",
    "https://vrising.fandom.com/wiki/Elixir_of_the_Werewolf",
    "https://vrising.fandom.com/wiki/Elixir_of_the_Bat",
    "https://vrising.fandom.com/wiki/Elixir_of_the_Crow",
    "https://vrising.fandom.com/wiki/Witch_Potion",
    "https://vrising.fandom.com/wiki/Potion_of_Rage",
    "https://vrising.fandom.com/wiki/Holy_Resistance_Flask",
    "https://vrising.fandom.com/wiki/Irradiant_Gruel",
    "https://vrising.fandom.com/wiki/Major_Explosive_Box",
    "https://vrising.fandom.com/wiki/Dusk_Caller",
    "https://vrising.fandom.com/wiki/Wrangler%27s_Potion",
    "https://vrising.fandom.com/wiki/Silver_Resistance_Potion",
    "https://vrising.fandom.com/wiki/Garlic_Resistance_Potion",
    "https://vrising.fandom.com/wiki/Holy_Resistance_Potion",
    "https://vrising.fandom.com/wiki/Minor_Explosive_Box",
    "https://vrising.fandom.com/wiki/Silver_Resistance_Brew",
    "https://vrising.fandom.com/wiki/Enchanted_Brew",
    "https://vrising.fandom.com/wiki/Brew_of_Ferocity",
    "https://vrising.fandom.com/wiki/Minor_Sun_Resistance_Brew",
    "https://vrising.fandom.com/wiki/Minor_Garlic_Resistance_Brew",
    "https://vrising.fandom.com/wiki/Fire_Resistance_Brew",
    "https://vrising.fandom.com/wiki/Blood_Rose_Brew",
    "https://vrising.fandom.com/wiki/Vermin_Salve",
    "https://vrising.fandom.com/wiki/Alchemy_Table",
    "https://vrising.fandom.com/wiki/Treasury_Flooring?so=search",
    "https://vrising.fandom.com/wiki/Simple_Workbench",
    "https://vrising.fandom.com/wiki/Woodworking_Bench",
    "https://vrising.fandom.com/wiki/Leatherworking_Station",
    "https://vrising.fandom.com/wiki/Artisan_Table",
    "https://vrising.fandom.com/wiki/Gem_Cutting_Table",
    "https://vrising.fandom.com/wiki/Jewelcrafting_Table",
    "https://vrising.fandom.com/wiki/Tailoring_Bench",
    "https://vrising.fandom.com/wiki/Smithy",
    "https://vrising.fandom.com/wiki/Anvil",
    "https://vrising.fandom.com/wiki/Ancestral_Forge",
    "https://vrising.fandom.com/wiki/Fusion_Forge",
    "https://vrising.fandom.com/wiki/Sawmill",
    "https://vrising.fandom.com/wiki/Advanced_Sawmill",
    "https://vrising.fandom.com/wiki/Grinder",
    "https://vrising.fandom.com/wiki/Advanced_Grinder",
    "https://vrising.fandom.com/wiki/The_Devourer",
    "https://vrising.fandom.com/wiki/Tannery",
    "https://vrising.fandom.com/wiki/Advanced_Tannery",
    "https://vrising.fandom.com/wiki/Furnace",
    "https://vrising.fandom.com/wiki/Advanced_Furnace",
    "https://vrising.fandom.com/wiki/Fabricator",
    "https://vrising.fandom.com/wiki/Loom",
    "https://vrising.fandom.com/wiki/Advanced_Loom",
    "https://vrising.fandom.com/wiki/Blood_Press",
    "https://vrising.fandom.com/wiki/Advanced_Blood_Press",
    "https://vrising.fandom.com/wiki/Paper_Press",
    "https://vrising.fandom.com/wiki/Vermin_Nest",
    "https://vrising.fandom.com/wiki/Tomb",
    "https://vrising.fandom.com/wiki/Stygian_Summoning_Circle",
    "https://vrising.fandom.com/wiki/Castle_Throne",
]

OUTPUT_FILE = "V_Rising_Wiki.txt"
DELAY = 1


def clean_content(div):
    for tag in div(['script', 'style']):
        tag.decompose()
    return div.get_text('\n', strip=True)


def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return None, None

    soup = BeautifulSoup(response.text, 'html.parser')
    title_tag = soup.find('h1', id='firstHeading')
    content_div = soup.find('div', id='mw-content-text')
    if not title_tag or not content_div:
        return None, None
    title = title_tag.get_text(strip=True)
    content = clean_content(content_div)
    return title, content


def main():
    visited = set()
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
        for url in URLS:
            if url in visited:
                continue
            visited.add(url)
            print(f"Fetching {url}")
            title, content = fetch_page(url)
            if title and content:
                out.write(title + '\n\n')
                out.write(content + '\n\n')
            time.sleep(DELAY)
    print(f"Pages processed: {len(visited)}")
    print(f"Output file: {os.path.abspath(OUTPUT_FILE)}")


if __name__ == "__main__":
    main()
